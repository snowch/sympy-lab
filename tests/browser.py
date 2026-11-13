# Copyright © 2026 Christopher Snow
"""Real Wasm mathematics, refresher UX, provenance, recovery and responsive reading."""
import json,math,os,re,subprocess,sys,time
from pathlib import Path
from playwright.sync_api import sync_playwright
from quiet_checks import check_quiet_layout
ROOT=Path(__file__).resolve().parents[1]
COURSE=json.loads((ROOT/'src/course.json').read_text())
LESSONS=COURSE['lessons'];ALL=LESSONS+COURSE['applications'];CAPSTONE=LESSONS[-1]
WORKED=json.loads((ROOT/'.cache/worked.json').read_text())['lessons']
RESULTS=ROOT/'test-results';RESULTS.mkdir(exist_ok=True)
BASE='http://127.0.0.1:5184/sympy-lab/'
NUM=r'[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?'
def visit(page,url):
    page.goto(url);page.wait_for_selector('html[data-ready=true]')
def wait_result(page):
    page.wait_for_function("document.querySelector('#status').textContent.startsWith('Completed') || /error|could not/.test(document.querySelector('#status').textContent)",timeout=150000)
    assert page.locator('#status').inner_text().startswith('Completed'),page.locator('#status').inner_text()+'\n'+page.locator('#output').text_content()
def open_optional(page,identifier):
    details=page.locator('#'+identifier)
    if not details.evaluate('e=>e.open'):details.locator(':scope > summary').click()

def restore_example(page):
    open_optional(page,'editor-tools')
    page.locator('#restore').click()

def download(page,selector,path):
    if selector=='#download-code':open_optional(page,'editor-tools')
    with page.expect_download() as result:page.locator(selector).click()
    result.value.save_as(path)
def compare(actual,expected,label):
    assert re.sub(NUM,'#',actual).split()==re.sub(NUM,'#',expected).split(),(label,actual,expected)
    a,b=re.findall(NUM,actual),re.findall(NUM,expected)
    assert len(a)==len(b),(label,a,b)
    for x,y in zip(a,b):assert math.isclose(float(x),float(y),rel_tol=2e-11,abs_tol=2e-13),(label,x,y)
def no_overflow(page,label):
    assert page.evaluate('document.documentElement.scrollWidth<=innerWidth'),label
server=subprocess.Popen([sys.executable,'-m','http.server','5184','--bind','127.0.0.1','--directory',str(ROOT/'.preview')],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
try:
    import urllib.request
    for _ in range(50):
        try:urllib.request.urlopen(BASE,timeout=1);break
        except Exception:time.sleep(.1)
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=None if os.environ.get('CI') else os.environ.get('CHROMIUM_PATH','/usr/bin/chromium'),headless=True,args=['--no-sandbox'])
        context=browser.new_context(viewport={'width':1440,'height':1000},accept_downloads=True)
        context.route('**/*',lambda route:route.continue_() if route.request.url.startswith(('http://127.0.0.1:5184/','data:','blob:')) else route.abort())
        page=context.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
        visit(page,BASE)
        assert page.locator('.lesson-row').count()==52
        assert page.locator('.symbol-demo .katex').count()>=3
        assert page.locator('.katex-error').count()==0
        assert page.locator('.lesson-row h4').first.evaluate('e=>parseFloat(getComputedStyle(e).fontSize)')>=17
        assert 'Sora' in page.locator('h1').evaluate('e=>getComputedStyle(e).fontFamily')
        assert page.evaluate('getComputedStyle(document.documentElement).backgroundColor')=='rgb(246, 249, 247)'
        page.screenshot(path=str(RESULTS/'overview-desktop.png'),full_page=True)
        page.locator('#search').fill('fractions')
        assert 0<page.locator('.lesson-row:visible').count()<52
        page.locator('#search').fill('no-such-topic-zzzz');assert page.locator('#search-empty').is_visible()
        page.locator('#search').fill('')
        page.evaluate("localStorage.setItem('syl:v1:read:your-first-symbolic-expression','true')")
        visit(page,BASE);assert page.locator('#start-label').inner_text()=='Continue learning'
        assert page.locator('#start-course').get_attribute('href')=='lessons/'+LESSONS[1]['slug']+'.html'
        visit(page,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        assert not page.locator('#maths-refresher').evaluate('e=>e.open')
        page.locator('#maths-refresher summary').click()
        assert page.locator('#maths-refresher .katex-mathml').count()==1
        assert page.locator('.refresher-example').is_visible()
        page.reload();page.wait_for_selector('html[data-ready=true]')
        assert page.locator('#maths-refresher').evaluate('e=>e.open')
        assert not page.locator('#run-result').is_visible()
        assert not page.locator('#stop').is_visible()
        assert not page.locator('#export-run').is_visible()
        assert page.locator('.outcome,.on-this-page,.mobile-course-bar').count()==0
        assert page.locator('.explanation p').first.evaluate('e=>parseFloat(getComputedStyle(e).fontSize)')>=20
        assert page.locator('#code').evaluate('e=>parseFloat(getComputedStyle(e).fontSize)')>=16
        assert page.locator('#code').evaluate('e=>getComputedStyle(e).lineHeight')==page.locator('.code-gutter').evaluate('e=>getComputedStyle(e).lineHeight')
        assert page.locator('#code-highlight .token-keyword').count()>0
        # Every source runs in the real worker with fresh variables. Actual
        # pages, refreshers and static worked examples are checked below too.
        for i,lesson in enumerate(ALL):
            source=(ROOT/'python'/lesson['code']).read_text()
            page.locator('#code').fill(source)
            assert page.locator('#code-highlight code').text_content()==source+'\n'
            page.locator('#run').click();wait_result(page)
            record=WORKED[lesson['slug']]
            compare(page.locator('#output').text_content().strip(),record['stdout'].strip(),lesson['slug'])
            assert page.locator('#symbolic-output .math-card').count()==len(record['maths'])
            assert page.locator('#symbolic-output .katex-error').count()==0
            actual_tex=page.locator('#symbolic-output annotation[encoding="application/x-tex"]').all_text_contents()
            assert len(actual_tex)==len(record['maths'])
            for tex,native in zip(actual_tex,record['maths']):compare(tex,native['latex'],lesson['slug'])
            assert page.locator('#plots img').count()==len(record['figures'])
            if i==0:page.screenshot(path=str(RESULTS/'lesson-desktop.png'),full_page=True)
            if i==43:
                with page.expect_popup() as popup:page.locator('#plots a').click()
                popup.value.wait_for_load_state();assert popup.value.url.startswith('blob:');popup.value.close()
            print(f'PASS Wasm {i+1:02d}: {lesson["slug"]}',flush=True)
        page.locator('#code').fill("assert 'radius' not in globals()\nresults={'Fresh namespace':True}\nprint('fresh namespace')")
        page.locator('#run').click();wait_result(page)
        assert 'fresh namespace' in page.locator('#output').text_content()
        print('PASS fresh namespace and real symbolic/plot output',flush=True)
        # Exercise all three capstone starters, then preserve the exact last run.
        visit(page,BASE+'lessons/'+CAPSTONE['slug']+'.html')
        original=page.locator('#code').input_value()
        for task in ['optimisation','ode','integral']:
            page.locator('#code').fill(original.replace('task = "optimisation"',f'task = "{task}"'))
            page.locator('#run').click();wait_result(page)
        page.locator('#report-question').fill('Does this authored density have total probability one?')
        page.locator('#report-plan').fill('Use support [0,1], nonnegative density and exact integration.')
        download(page,'#export-run',RESULTS/'run.json')
        record=json.loads((RESULTS/'run.json').read_text())
        assert record['versions']['sympy']=='1.13.3'
        assert record['symbolic_results'][0]['text']=='1'
        old_source=record['source'];page.locator('#code').fill(old_source+'\n# changed after execution\n')
        assert 'changed' in page.locator('#output-provenance').inner_text()
        download(page,'#export-run',RESULTS/'run-after-edit.json')
        assert json.loads((RESULTS/'run-after-edit.json').read_text())['source']==old_source
        download(page,'#export-report',RESULTS/'investigation.md')
        report=(RESULTS/'investigation.md').read_text()
        assert 'changed after this run' in report and 'Symbolic results (LaTeX)' in report
        assert 'task = "integral"' in report and 'total probability one' in report
        print('PASS all capstone starters and exact-source run/report exports',flush=True)
        # A Python error opens text details; Stop kills a runaway worker.
        visit(page,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        page.locator('#code').fill("print('before failure')\nraise ValueError('deliberate test error')")
        page.locator('#run').click()
        page.wait_for_function("document.querySelector('#status').textContent.includes('reported an error')",timeout=150000)
        assert page.locator('#output').is_visible()
        assert 'before failure' in page.locator('#output').inner_text()
        assert 'deliberate test error' in page.locator('#output').inner_text()
        page.locator('#code').fill('while True: pass');page.locator('#run').click()
        page.wait_for_function("document.querySelector('#status').textContent==='Running your Python…'",timeout=30000)
        assert page.locator('#stop').is_visible()
        page.locator('#stop').click();assert 'Stopped' in page.locator('#status').inner_text()
        assert page.evaluate('document.activeElement.id')=='run'
        restore_example(page);page.locator('#run').click();wait_result(page)
        page.locator('#quiz button').click();assert 'Choose an answer' in page.locator('#quiz-feedback').inner_text()
        page.locator('input[name=answer][value="1"]').check();page.locator('#quiz button').click()
        assert 'Reconsider' in page.locator('#quiz-feedback').inner_text()
        page.locator('input[name=answer][value="0"]').check();page.locator('#quiz button').click()
        assert 'reasoning fits' in page.locator('#quiz-feedback').inner_text()
        open_optional(page,'prediction-notes')
        page.locator('#prediction').fill('My saved prediction')
        open_optional(page,'lesson-notes')
        page.locator('#notes').fill('A note to preserve')
        page.locator('#code').fill(page.locator('#code').input_value()+'\n# saved draft')
        page.locator('#mark-read').check()
        download(page,'#download-code',RESULTS/'downloaded.py')
        assert '# saved draft' in (RESULTS/'downloaded.py').read_text()
        page.reload();page.wait_for_selector('html[data-ready=true]')
        assert page.locator('#notes').input_value()=='A note to preserve'
        assert page.locator('#prediction').input_value()=='My saved prediction'
        assert '# saved draft' in page.locator('#code').input_value()
        assert page.locator('#mark-read').is_checked()
        assert page.locator('#maths-refresher').evaluate('e=>e.open')
        page.locator('#code').evaluate('e=>{e.scrollTop=50;e.scrollLeft=20;e.dispatchEvent(new Event("scroll"))}')
        assert page.locator('#code').evaluate('e=>e.scrollLeft')==page.locator('#code-highlight').evaluate('e=>e.scrollLeft')
        print('PASS error/Stop recovery, feedback and saved drafts/refresher state',flush=True)
        page.locator('#theme').click();page.reload()
        assert page.locator('html').get_attribute('data-theme')=='dark'
        assert page.evaluate('getComputedStyle(document.documentElement).backgroundColor')=='rgb(16, 28, 23)'
        page.screenshot(path=str(RESULTS/'lesson-dark.png'),full_page=True)
        for width in [390,320]:
            page.set_viewport_size({'width':width,'height':844})
            for lesson in ALL:
                visit(page,BASE+'lessons/'+lesson['slug']+'.html')
                assert page.locator('h1').inner_text()==lesson['title']
                assert page.locator('.explanation p').first.evaluate('e=>parseFloat(getComputedStyle(e).fontSize)')>=18
                page.locator('#maths-refresher').evaluate('e=>e.open=false')
                no_overflow(page,(width,lesson['slug'],'closed'))
                page.locator('#maths-refresher').evaluate('e=>e.open=true')
                no_overflow(page,(width,lesson['slug'],'refresher open'))
                assert page.locator('#maths-refresher .katex-error').count()==0
                page.locator('.worked').evaluate('e=>e.open=true')
                no_overflow(page,(width,lesson['slug'],'worked maths open'))
                page.locator('#mark-read').check()
            visit(page,BASE);no_overflow(page,('overview',width))
            if width==390:page.screenshot(path=str(RESULTS/'overview-mobile-dark.png'),full_page=True)
        print('PASS every lesson/refresher/worked result at 390px and 320px',flush=True)
        page.set_viewport_size({'width':390,'height':844});page.locator('#theme').click()
        visit(page,BASE+'lessons/'+LESSONS[3]['slug']+'.html')
        page.locator('#course-menu-toggle').click();assert page.locator('#course-sidebar').is_visible()
        page.keyboard.press('Escape');assert not page.locator('#course-sidebar').is_visible()
        assert page.evaluate('document.activeElement.id')=='course-menu-toggle'
        page.locator('#maths-refresher').scroll_into_view_if_needed()
        page.screenshot(path=str(RESULTS/'refresher-mobile.png'),full_page=True)
        for width in [1440,390,320]:
            page.set_viewport_size({'width':width,'height':1000})
            for route in ['', 'lessons/'+LESSONS[0]['slug']+'.html', 'lessons/'+LESSONS[41]['slug']+'.html','field-notes.html']:
                visit(page,BASE+route);page.evaluate("document.documentElement.style.fontSize='200%'")
                if page.locator('#maths-refresher').count():page.locator('#maths-refresher').evaluate('e=>e.open=true')
                no_overflow(page,('200% text',width,route))
        print('PASS mobile menu, 200% text and mathematical overflow regions',flush=True)
        visit(page,BASE);page.locator('.portable-progress summary').click()
        download(page,'#export-progress',RESULTS/'progress.json')
        assert page.locator('#progress-count').inner_text()=='48 / 48 read'
        fresh=browser.new_context(viewport={'width':1440,'height':1000})
        second=fresh.new_page();visit(second,BASE)
        assert second.locator('#progress-count').inner_text()=='0 / 48 read'
        second.locator('.portable-progress summary').click()
        second.locator('#import-progress').set_input_files(str(RESULTS/'progress.json'))
        second.wait_for_function("document.querySelector('#progress-status').textContent.startsWith('Imported')")
        assert second.locator('#progress-count').inner_text()=='48 / 48 read'
        visit(second,BASE+'lessons/'+LESSONS[0]['slug']+'.html')
        assert second.locator('#notes').input_value()=='A note to preserve'
        assert second.locator('#maths-refresher').evaluate('e=>e.open')
        # Avoid smooth-scroll timing races in the separate static reader.
        reading=browser.new_context(java_script_enabled=False,reduced_motion='reduce');static=reading.new_page();requests=[]
        static.on('request',lambda req:requests.append(req.url))
        for lesson in ALL:
            response=static.goto(BASE+'lessons/'+lesson['slug']+'.html');assert response.status==200
            assert static.locator('.explanation p').first.inner_text()==lesson['explain'][0]
            static.locator('#maths-refresher summary').click()
            assert static.locator('.refresher-example').is_visible()
            static.locator('.worked summary').first.click()
            assert static.locator('.worked .katex-mathml').count()==len(WORKED[lesson['slug']]['maths'])
        assert not any('/engine/' in url for url in requests)
        assert errors==[],errors
        check_quiet_layout(browser,ROOT,BASE,LESSONS)
        browser.close()
        print('PASS: 52 real Wasm sources; native text/LaTeX agreement; all refresher panels; reports and provenance; error/Stop recovery; drafts/progress; 320/390px and 200% reflow; both themes; no-JavaScript reading.',flush=True)
finally:
    server.terminate();server.wait(timeout=10)

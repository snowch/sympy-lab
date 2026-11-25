import functools,http.server,json,pathlib,shutil,threading
from playwright.sync_api import sync_playwright
from runtime_startup import check_runtime_startup
root=pathlib.Path(__file__).resolve().parent.parent
slug=json.loads((root/'package.json').read_text())['name']
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(root/'.preview')))
threading.Thread(target=server.serve_forever,daemon=True).start()
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path=shutil.which('chromium'),headless=True,args=['--no-sandbox'])
  check_runtime_startup(browser,f'http://127.0.0.1:{server.server_port}/{slug}/',json.loads((root/'src/course.json').read_text())['lessons'][0]['slug'])
  browser.close()
 print('PASS real preparation, warm run, namespace/reset, stop during loading and persistent missing-worker recovery')
finally:server.shutdown();server.server_close()

import {renderRich} from './rich-text.mjs';
import {areaModelSvg} from './area-model.mjs';
import katex from './vendor/katex.mjs';
// Copyright © 2026 Christopher Snow
import {attachEditor} from './editor.mjs';
const root=new URL('.',import.meta.url);
const $=id=>document.getElementById(id);
const prefix='syl:v1:';
let storageAvailable=true;
function get(key,fallback=''){
 try{return localStorage.getItem(prefix+key)??fallback}catch{storageAvailable=false;return fallback}
}
function put(key,value){
 try{localStorage.setItem(prefix+key,String(value));return true}catch{return false}
}
function storageMessage(message){
 const target=$('storage-error');
 target.textContent=message;target.hidden=!message;
}
function download(name,body,type='application/json'){
 const url=URL.createObjectURL(new Blob([body],{type}));
 const anchor=document.createElement('a');anchor.href=url;anchor.download=name;anchor.click();
 setTimeout(()=>URL.revokeObjectURL(url),1000);
}
function updateReadMarks(){
 document.querySelectorAll('[data-read]').forEach(el=>el.textContent=get('read:'+el.dataset.read)==='true'?'✓ Read':'');
}
$('theme')?.addEventListener('click',()=>{
 const theme=document.documentElement.dataset.theme==='dark'?'light':'dark';
 document.documentElement.dataset.theme=theme;
 try{localStorage.setItem('syl:theme',theme)}catch{}
 setThemeLabel();
});
function setThemeLabel(){const dark=document.documentElement.dataset.theme==='dark';$('theme')?.setAttribute('aria-label',`Switch to ${dark?'light':'dark'} theme`)}
setThemeLabel();
const menu=$('course-menu-toggle'),sidebar=$('course-sidebar');
if(menu&&sidebar){
 const close=()=>{sidebar.classList.remove('is-open');menu.setAttribute('aria-expanded','false')};
 menu.addEventListener('click',()=>{const open=sidebar.classList.toggle('is-open');menu.setAttribute('aria-expanded',String(open))});
 document.addEventListener('keydown',event=>{if(event.key==='Escape'&&sidebar.classList.contains('is-open')){close();menu.focus()}});
 matchMedia('(min-width: 961px)').addEventListener('change',event=>{if(event.matches)close()});
}
const rich=text=>renderRich(text,tex=>katex.renderToString(tex,{displayMode:false,throwOnError:false,trust:false,strict:'warn'}));
const course=await fetch(new URL('course.json',root),{cache:'no-cache'}).then(response=>{if(!response.ok)throw new Error('Course data could not load. Please reload.');return response.json()}).catch(error=>{
 const target=$('status')||$('progress-status');if(target)target.textContent=error.message;return null;
});
if(course){
 updateReadMarks();
 if($('search'))initializeOverview(course);
 const lesson=[...course.lessons,...course.applications].find(l=>l.slug===document.querySelector('[data-slug]')?.dataset.slug);
 if(lesson)initializeLesson(lesson);
 document.documentElement.dataset.ready='true';
}
function initializeOverview({lessons,applications}){
 function progress(){
  const read=lessons.filter(l=>get('read:'+l.slug)==='true').length;
  $('progress-count').textContent=`${read} / ${lessons.length} read`;
  $('course-progress').value=read;
  const next=lessons.find(l=>get('read:'+l.slug)!=='true');
  $('start-course').href=next?'lessons/'+next.slug+'.html':'#course';
  $('start-label').textContent=next?(read?'Continue learning':'Start lesson 1'):'Review course contents';
  updateReadMarks();
 }
 progress();
 if(!storageAvailable)$('progress-status').textContent='This browser could not open saved progress.';
 const modules=[...document.querySelectorAll('.module')];
 const savedOpen=new Map();let searching=false;
 const revealModule=()=>{
  let id;
  try{id=decodeURIComponent(location.hash.slice(1))}catch{return}
  const module=document.getElementById(id);
  if(module?.classList.contains('module'))module.open=true;
 };
 revealModule();window.addEventListener('hashchange',revealModule);
 $('search').addEventListener('input',()=>{
  const words=$('search').value.toLowerCase().trim().split(/\s+/).filter(Boolean);
  if(words.length&&!searching){for(const module of modules)savedOpen.set(module,module.open);searching=true}
  let count=0;
  document.querySelectorAll('.lesson-row').forEach(row=>{const match=words.every(word=>row.dataset.search.includes(word));row.hidden=!match;if(match)count++});
  for(const module of modules){
   module.hidden=![...module.querySelectorAll('.lesson-row')].some(row=>!row.hidden);
   if(words.length)module.open=!module.hidden;
   else if(searching)module.open=savedOpen.get(module)??false;
  }
  if(!words.length){searching=false;savedOpen.clear()}
  $('search-count').textContent=`${count} investigation${count===1?'':'s'}`;
  $('search-empty').hidden=count!==0;
 });
 $('export-progress').addEventListener('click',()=>{
  const data={};
  try{
   for(let i=0;i<localStorage.length;i++){
    const key=localStorage.key(i);
    if(key?.startsWith(prefix))data[key.slice(prefix.length)]=localStorage.getItem(key);
   }
  }catch{
   $('progress-status').textContent='This browser could not read saved progress. No file was downloaded.';
   return;
  }
  download('sympy-lab-progress.json',JSON.stringify({course:'sympy-lab',schema:1,exported_at:new Date().toISOString(),data},null,2));
  $('progress-status').textContent='Exported saved reading marks, attempts and drafts. Completed run results require their own exports.';
 });
 $('import-progress').addEventListener('change',async()=>{
  const file=$('import-progress').files[0];if(!file)return;
  try{
   if(file.size>1_000_000)throw new Error('Progress file must be smaller than 1 MB.');
   const record=JSON.parse(await file.text());
   if(record.course!=='sympy-lab'||record.schema!==1||!record.data||typeof record.data!=='object'||Array.isArray(record.data))throw new Error('Not a version 1 SymPy Lab progress file.');
   const slugs=new Set([...lessons,...applications].map(l=>l.slug));
   const fields=new Set(['code','restore-backup','prediction','notes','quiz','report-question','report-plan','report-source','report-finding','report-limits','refresher']);
   const entries=Object.entries(record.data);
   for(const[key,value]of entries){
    const [type,slug,field,...extra]=key.split(':');
    if(extra.length||!slugs.has(slug)||typeof value!=='string'||value.length>300_000||!((type==='read'&&!field&&(value==='true'||value==='false'))||(type==='draft'&&fields.has(field))))throw new Error('Progress file contains an invalid record. Nothing has been imported.');
   }
   let saved=0;for(const[key,value]of entries)if(put(key,value))saved++;
   progress();$('progress-status').textContent=saved===entries.length?`Imported ${saved} saved records. Matching records in this browser were replaced.`:`Saved ${saved} of ${entries.length} records. Keep the import file and check browser storage before retrying.`;
  }catch(error){$('progress-status').textContent=error.message}
  $('import-progress').value='';
 });
}
function initializeLesson(lesson){
 const slug=lesson.slug;
 function renderMaths(records){
  const region=$('symbolic-output');region.replaceChildren();
  if(!records.length){const note=document.createElement('p');note.className='math-placeholder';note.textContent='No labelled expressions in results. Read text output below.';region.append(note);return}
  const grid=document.createElement('div');grid.className='math-results';
  for(const record of records){
   const card=document.createElement('div');card.className='math-card';
   const label=document.createElement('span');label.textContent=record.label;
   const expression=document.createElement('div');expression.className='math-display';
   katex.render(record.latex,expression,{displayMode:true,throwOnError:false,trust:false,strict:'warn'});
   card.append(label,expression);grid.append(card);
  }
  region.append(grid);
 }

 const refresher=$('maths-refresher');
 refresher.open=get(`draft:${slug}:refresher`)==='true';
 refresher.addEventListener('toggle',()=>put(`draft:${slug}:refresher`,refresher.open));
 const initialCode=$('code').value;
 let worker=null,timer=null,busy=false,lastSuccessfulRun=null,revision=0;
 let plotUrls=[];
 function clearPlotUrls(){for(const url of plotUrls)URL.revokeObjectURL(url);plotUrls=[]}
 const initialQuiz=get(`draft:${slug}:quiz`);
 const draftKey=id=>`draft:${slug}:${id}`;
 $('code').value=get(draftKey('code'),initialCode);
 let recoverableDraft=get(draftKey('restore-backup'),null);
 $('saved-draft-note').hidden=$('code').value===initialCode;
 const refreshEditor=attachEditor($('code'));
 const unsavedReportFields=new Set();
 function updatePreparation(){
  document.querySelector('.editor-prepare').hidden=$('code').value!==initialCode;
 }
 function saveField(el){
  const saved=put(draftKey(el.dataset.save),el.value);
  if(el.id==='notes'){
   $('save-note').textContent=saved?'Notes saved in this browser.':'The browser could not save these edits. Copy the open notes before leaving. Reloading may show older notes.';
  }else if(el.id.startsWith('report-')){
   if(saved)unsavedReportFields.delete(el.id);
   else unsavedReportFields.add(el.id);
   $('report-draft-status').textContent=unsavedReportFields.size
    ?'The browser could not save some report edits. Export the investigation to keep the text currently open.'
    :'Report fields saved in this browser.';
  }else{
   $('prediction-status').textContent=saved?'':'This browser could not save your prediction. Copy it before leaving.';
  }
 }
 updatePreparation();
 document.querySelectorAll('[data-save]').forEach(el=>{
  el.value=get(draftKey(el.dataset.save));
  if(el.value&&el.closest('details'))el.closest('details').open=true;
  el.addEventListener('input',()=>saveField(el));
 });
 $('mark-read').checked=get('read:'+slug)==='true';
 if(!storageAvailable)storageMessage('This browser could not open your saved work. Python can still run. To keep edits, copy them or export a record before leaving.');
 $('mark-read').addEventListener('change',()=>{
  const saved=put('read:'+slug,$('mark-read').checked);
  if(!saved)$('mark-read').checked=get('read:'+slug)==='true';
  $('read-status').textContent=saved?'':'This browser could not save the reading mark.';
  updateReadMarks();
 });
 function updateProvenance(){
  if(!lastSuccessfulRun)return;
  const changed=$('code').value!==lastSuccessfulRun.source;
  $('output-provenance').textContent=busy
   ?'A new run is in progress. This result is from the last successful run.'
   :changed
    ?'The code changed. The result and export show the last successful run.'
    :`Last successful run at ${new Date(lastSuccessfulRun.executed_at).toLocaleTimeString()}.`;
  $('output-provenance').classList.toggle('stale',changed||busy);
 }
 function updateRecovery(){
  $('recover-draft').hidden=recoverableDraft===null||recoverableDraft===$('code').value;
 }
 function showCode(code){
  const previous=$('code').value;
  let canSave=true;
  if(previous!==initialCode&&previous!==code){
   recoverableDraft=previous;
   canSave=put(draftKey('restore-backup'),previous);
  }
  $('code').value=code;
  refreshEditor();
  const saved=canSave&&put(draftKey('code'),code);
  storageMessage(saved?'':'This browser could not save the open code. Use Tools → Download Python to keep a copy.');
  $('saved-draft-note').hidden=true;
  updatePreparation();
  updateRecovery();
  updateProvenance();
  $('editor-tools').open=false;
  $('code').focus();
  return saved;
 }
 updateRecovery();
 $('code').addEventListener('input',()=>{
  const saved=put(draftKey('code'),$('code').value);
  storageMessage(saved?'':'This browser could not save the open code. Use Tools → Download Python to keep a copy.');
  $('saved-draft-note').hidden=true;
  updatePreparation();
  updateRecovery();
  updateProvenance();
 });
 $('code').addEventListener('keydown',event=>{
  if((event.ctrlKey||event.metaKey)&&event.key==='Enter'){event.preventDefault();if(!busy)run()}
 });
 $('restore').addEventListener('click',()=>{
  const saved=showCode(initialCode);
  $('status').textContent=recoverableDraft===null
   ?'Published example opened.'
   :saved?'Published example opened. Use Recover draft in Tools to get your code back.'
    :'Published example opened. Use Recover draft in Tools before leaving to bring back the draft currently available in this tab.';
 });
 $('recover-draft').addEventListener('click',()=>{
  if(recoverableDraft===null)return;
  const saved=showCode(recoverableDraft);
  $('status').textContent=saved?'Draft recovered in the editor.':'Draft recovered in the open editor. Download it before leaving.';
 });
 $('back-to-editor').addEventListener('click',event=>{
  event.preventDefault();
  $('code').focus({preventScroll:true});
  $('code-editor').scrollIntoView({block:'start'});
 });
 $('download-code').addEventListener('click',()=>download(slug+'.py',$('code').value,'text/x-python'));
 $('export-run').addEventListener('click',()=>{
  if(!lastSuccessfulRun)return;
  const notes={prediction:$('prediction').value,notes:$('notes').value};
  download(slug+'-run.json',JSON.stringify({...lastSuccessfulRun,notes},null,2));
 });
 function controls(running){
  const returnFocus=!running&&document.activeElement===$('stop');
  busy=running;document.querySelector('.experiment').classList.toggle('is-running',running);$('code-editor').setAttribute('aria-busy',String(running));$('run').disabled=running;$('stop').disabled=!running;$('stop').hidden=!running;$('restore').disabled=running;
  $('recover-draft').disabled=running;
  if(returnFocus)$('run').focus({preventScroll:true});
 }
 function terminate(message){
  revision++;clearTimeout(timer);worker?.terminate();worker=null;controls(false);$('status').textContent=message;
  updateProvenance();
 }
 function showRunError(message,stdout=''){
  const traceback=message.trim();
  const details=[stdout.trimEnd(),traceback].filter(Boolean).join('\n\n');
  $('error-summary').textContent=traceback.split('\n').at(-1)||'Python could not finish.';
  $('error-trace').textContent=details;
  $('error-details').hidden=!details.includes('\n');
  $('run-error').hidden=false;
  updateProvenance();
 }
 $('stop').addEventListener('click',()=>terminate('Stopped. Select Run Python to start a fresh run.'));
 async function run(){
  if(busy)return;
  const source=$('code').value,runRevision=++revision;
  const runWasFocused=document.activeElement===$('run');
  $('editor-tools').open=false;
  $('run-error').hidden=true;
  $('error-details').open=false;
  controls(true);
  if(runWasFocused)$('stop').focus({preventScroll:true});
  $('status').textContent=worker?'Starting your Python…':'Loading Python and SymPy. This can take a moment…';
  updateProvenance();
  const fail=message=>{
   if(runRevision!==revision)return;
   terminate('Python could not finish. Check the message, then edit or run again.');
   showRunError(message);
  };
  timer=setTimeout(()=>fail('Python initialization exceeded two minutes. Check your connection and run again.'),120000);
  if(!worker){try{worker=new Worker(new URL('worker.js',root))}catch(error){fail(error.message);return}}
  worker.onerror=event=>fail(event.message||'The Python worker could not load.');
  worker.onmessage=({data})=>{
   if(runRevision!==revision)return;
   if(data.type==='running'){
    clearTimeout(timer);$('status').textContent='Running your Python…';
    timer=setTimeout(()=>fail('Execution exceeded 45 seconds and was stopped. Reduce the work or fix a loop, then run again.'),45000);return;
   }
   if(data.type==='error'){fail(data.message);return}
   if(data.type!=='result')return;
   clearTimeout(timer);controls(false);
   const {stdout,error,figures,versions,maths=[],visual=null}=data.value;
   if(error){
    $('status').textContent='Python reported an error. Check the error message before running again.';
    showRunError(error,stdout);
    return;
   }
   $('run-result').hidden=false;
   lastSuccessfulRun={schema:1,course:'sympy-lab',lesson:slug,executed_at:new Date().toISOString(),source,input_csv:null,input_name:null,stdout,error:null,symbolic_results:maths,visual_model:visual,figures_svg_base64:figures,versions,environment:{user_agent:navigator.userAgent,timing_scope:'Local browser Pyodide; see executed source for boundaries.'}};
   $('output').textContent=stdout||'No text was printed.';
   $('output').closest('details').open=!maths.length||slug==='export-an-expression-as-code';
   renderMaths(maths);
   const visualRegion=$('result-visual');visualRegion.replaceChildren();visualRegion.hidden=!visual;
   if(visual){
    const figure=document.createElement('figure');figure.innerHTML=areaModelSvg(visual,320);
    const caption=document.createElement('figcaption');caption.textContent=visual.caption;
    figure.append(caption);visualRegion.append(figure);
   }
   clearPlotUrls();
   $('plots').replaceChildren(...figures.map((svg,i)=>{
    const figure=document.createElement('figure');figure.className='worked-figure';
    const image=document.createElement('img');image.className='plot';
    const bytes=Uint8Array.from(atob(svg),c=>c.charCodeAt(0));
    const url=URL.createObjectURL(new Blob([bytes],{type:'image/svg+xml'}));plotUrls.push(url);
    image.src=url;image.alt=`Plot ${i+1} from your actual Python execution. Read its labelled axes and the text output together.`;
    const caption=document.createElement('figcaption'),link=document.createElement('a');
    link.href=url;link.target='_blank';link.rel='noopener';link.textContent='Open full-size figure ↗';
    caption.append(link);figure.append(image,caption);return figure;
   }));
   $('status').textContent='Completed. Inspect the result below.';
   $('export-run').disabled=false;$('export-run').hidden=false;updateProvenance();
  };
  worker.postMessage({source});
 }
 $('run').addEventListener('click',run);
 window.addEventListener('pagehide',()=>{clearTimeout(timer);worker?.terminate();clearPlotUrls()});
 let quizAttempt=null;
 try{quizAttempt=JSON.parse(initialQuiz)}catch{}
 if(quizAttempt&&Number.isInteger(quizAttempt.answer)&&quizAttempt.answer>=0&&quizAttempt.answer<lesson.options.length){
  const choice=document.querySelector(`input[name=answer][value="${quizAttempt.answer}"]`);if(choice)choice.checked=true;
 }
 $('quiz').addEventListener('submit',event=>{
  event.preventDefault();const selected=document.querySelector('input[name=answer]:checked');
  if(!selected){$('quiz-feedback').textContent='Choose an answer first, then check your reasoning.';return}
  const answer=Number(selected.value),correct=answer===lesson.correct;
  const saved=put(draftKey('quiz'),JSON.stringify({answer,correct,at:new Date().toISOString()}));
  const feedback=$('quiz-feedback');feedback.replaceChildren();feedback.classList.toggle('incorrect',!correct);
  const title=document.createElement('b');title.textContent=correct?'That reasoning fits.':'Reconsider the comparison.';
  const text=document.createElement('span');text.innerHTML=rich(lesson.feedback);
  feedback.append(title,text);
  if(!saved)feedback.append(document.createTextNode(' This browser could not save your answer.'));
  feedback.focus({preventScroll:true});
 });
 if($('export-report'))$('export-report').addEventListener('click',()=>{
  function codeBlock(language,text){
   const longest=(text.match(/`+/g)||[]).reduce((length,run)=>Math.max(length,run.length),2);
   const fence='`'.repeat(longest+1);
   return `${fence}${language}\n${text}\n${fence}`;
  }
  const fields=[['question','Question & intended result'],['plan','Assumptions, domain & method'],['source','Inputs, units & provenance'],['finding','Derivation & verification'],['limits','Limitations & next check']];
  const body=['# SymPy Lab · Investigation',`Exported ${new Date().toISOString()}`];
  for(const[id,label]of fields)body.push(`## ${label}\n\n${$('report-'+id).value||'[Not recorded]'}`);
  body.push('## Execution record');
  if(lastSuccessfulRun){
   const {executed_at,versions,source,stdout,symbolic_results}=lastSuccessfulRun;
   body.push(`Last successful run at ${executed_at}. Runtime versions ${JSON.stringify(versions)}`);
   body.push('### Exact executed Python\n\n'+codeBlock('python',source));
   body.push('### Actual output\n\n'+codeBlock('text',stdout));
   if(symbolic_results.length)body.push('### Symbolic results (LaTeX)\n\n'+symbolic_results.map(r=>r.label+'\n\n$$\n'+r.latex+'\n$$').join('\n\n'));
   if($('code').value!==source)body.push('The editor changed after this run. The record preserves the last successful execution.');
  }else body.push('No successful execution was recorded on this page. Worked results are available in the lesson.');
  body.push('## Field notes\n\n'+($('notes').value||'[Not recorded]'));
  download('sympy-investigation.md',body.join('\n\n')+'\n','text/markdown');
  $('report-status').textContent=lastSuccessfulRun?'Investigation exported. Use Export run to keep figures and structured symbolic results alongside it.':'Report text exported. It contains no successful run yet.';
 });
 controls(false);
}

document.addEventListener('click',event=>{
 for(const details of document.querySelectorAll('.header-help[open],.editor-tools[open]'))if(!details.contains(event.target))details.open=false;
});
document.addEventListener('keydown',event=>{
 if(event.key!=='Escape')return;
 const open=[...document.querySelectorAll('.header-help[open],.editor-tools[open]')];
 const target=open.find(d=>d.contains(document.activeElement))||open.at(-1);
 if(target){target.open=false;target.querySelector('summary').focus()}
});

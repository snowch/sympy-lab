// Copyright © 2026 Christopher Snow
importScripts('./engine/pyodide.js');
let ready;
async function initialize(){
 const py=await loadPyodide({indexURL:'./engine/'});
 await py.loadPackage(['sympy','numpy','matplotlib']);
 await py.runPythonAsync(`import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'figure.figsize':(6,3.8),'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white','axes.labelcolor':'#243f34','text.color':'#243f34','savefig.bbox':'tight'})`);
 return py;
}
self.onmessage=async({data})=>{
 try{
  ready ||= initialize().catch(error=>{ready=null;throw error});
  const py=await ready;
  py.globals.set('_source',data.source);
  postMessage({type:'running'});
  const value=await py.runPythonAsync(`import io,json,platform,traceback,base64
import sympy,numpy,mpmath,matplotlib
from contextlib import redirect_stdout,redirect_stderr
plt.close('all')
_buffer=io.StringIO()
_namespace={'__name__':'__main__'}
_failure=None
with redirect_stdout(_buffer),redirect_stderr(_buffer):
    try:
        exec(compile(_source,'investigation.py','exec'),_namespace)
    except Exception:
        _failure=traceback.format_exc()
_math=[]
_results=_namespace.get('results',{})
if isinstance(_results,dict):
    for _label,_expression in list(_results.items())[:50]:
        try:
            _latex=sympy.latex(_expression)
            if len(_latex)<=12000:
                _math.append({'label':str(_label),'latex':_latex,'text':str(_expression)})
        except Exception:
            pass
_images=[]
for _number in plt.get_fignums():
    _image=io.StringIO()
    plt.figure(_number).savefig(_image,format='svg',metadata={'Date':None})
    _images.append(base64.b64encode(_image.getvalue().encode()).decode())
plt.close('all')
json.dumps({'stdout':_buffer.getvalue(),'error':_failure,'maths':_math,'figures':_images,'versions':{'python':platform.python_version(),'pyodide':'0.27.7','sympy':sympy.__version__,'mpmath':mpmath.__version__,'numpy':numpy.__version__,'matplotlib':matplotlib.__version__}})`);
  postMessage({type:'result',value:JSON.parse(value)});
 }catch(error){postMessage({type:'error',message:String(error.message||error)})}
};

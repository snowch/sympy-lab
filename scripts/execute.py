# Copyright © 2026 Christopher Snow
"""Execute exact published sources; collect real text, symbolic results and figures."""
import contextlib,io,json,platform,sys
from pathlib import Path
import sympy,numpy,matplotlib,mpmath
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from display_model import area_model
from visuals import illustration
ROOT=Path(__file__).resolve().parents[1]
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'figure.figsize':(6,3.8),
 'axes.spines.top':False,'axes.spines.right':False,'figure.facecolor':'white','axes.facecolor':'white',
 'axes.labelcolor':'#243f34','text.color':'#243f34','svg.hashsalt':'sympy-lab','savefig.bbox':'tight'})

def execute(lesson,index=None):
    source=(ROOT/'python'/lesson['code']).read_text()
    namespace={'__name__':'__main__'}
    output=io.StringIO();plt.close('all')
    with contextlib.redirect_stdout(output),contextlib.redirect_stderr(output):
        exec(compile(source,lesson['code'],'exec'),namespace)
    maths=[{'label':str(label),'latex':sympy.latex(value),'text':str(value)}
           for label,value in namespace.get('results',{}).items()]
    figures=[]
    for number in plt.get_fignums():
        image=io.StringIO();plt.figure(number).savefig(image,format='svg',metadata={'Date':None})
        figures.append(image.getvalue())
    plt.close('all')
    return {'stdout':output.getvalue(),'maths':maths,'figures':figures,'visual':area_model(namespace),
            'illustration':illustration(index,namespace) if index else None}

if __name__=='__main__':
    course=json.loads((ROOT/'src/course.json').read_text())
    records={l['slug']:execute(l,i+1) for i,l in enumerate(course['lessons']+course['applications'])}
    destination=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'.cache/worked.json'
    destination.parent.mkdir(parents=True,exist_ok=True)
    destination.write_text(json.dumps({'environment':{'python':platform.python_version(),
      'sympy':sympy.__version__,'mpmath':mpmath.__version__,'numpy':numpy.__version__,
      'matplotlib':matplotlib.__version__,'kind':'Executed from exact published Python during the build; separate from browser execution.'},'lessons':records}))
    print(f'Executed {len(records)} published sources; generated {sum(len(r["maths"]) for r in records.values())} symbolic records and {sum(len(r["figures"]) for r in records.values())} figures.')

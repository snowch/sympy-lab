# Copyright © 2026 Christopher Snow
"""Check every complete source, mathematical references and all capstone starters."""
import contextlib,io,json,unittest,warnings
from pathlib import Path
import sympy as sp
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
COURSE=json.loads((ROOT/'src/course.json').read_text())
LESSONS=COURSE['lessons'];ALL=LESSONS+COURSE['applications']
def run(lesson,source=None):
    stream=io.StringIO();namespace={'__name__':'__main__'};plt.close('all')
    with contextlib.redirect_stdout(stream),contextlib.redirect_stderr(stream),warnings.catch_warnings():
        warnings.simplefilter('ignore',DeprecationWarning)
        warnings.simplefilter('error',RuntimeWarning)
        exec(compile(source or (ROOT/'python'/lesson['code']).read_text(),lesson['code'],'exec'),namespace)
    plt.close('all');return namespace,stream.getvalue()
class CourseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runs={l['slug']:run(l) for l in ALL}
        print(f'Executed all {len(cls.runs)} complete published sources.',flush=True)
    def ns(self,index):return self.runs[LESSONS[index-1]['slug']][0]
    def test_course_and_refreshers_are_complete(self):
        self.assertEqual(len(LESSONS),48);self.assertEqual(len(ALL),52)
        self.assertEqual(len({l['slug'] for l in ALL}),52)
        for m in range(8):self.assertEqual(sum(l['module']==m for l in LESSONS),6)
        for l in ALL:
            with self.subTest(lesson=l['slug']):
                self.assertEqual(len(l['explain']),3)
                self.assertGreater(sum(len(p.split()) for p in l['explain']),85)
                self.assertEqual(len(l['options']),3)
                self.assertIn(l['correct'],range(3));self.assertEqual(len(l['hints']),2)
                self.assertTrue(all(l[k] for k in ['goal','predict','look','change','feedback','limit','kind','source']))
                self.assertTrue(all(l['refresher'].get(k) for k in ['title','body','tex','example']))
                namespace,output=self.runs[l['slug']]
                self.assertTrue(output.strip());self.assertNotIn('Warning',output)
                self.assertTrue(namespace['results'])
                for v in namespace['results'].values():self.assertTrue(sp.latex(v))
    def test_exact_inputs_and_symbol_domains(self):
        ns=self.ns(2)
        self.assertEqual(ns['exact'],sp.Rational(1,3))
        self.assertNotEqual(sp.Rational(ns['early_float']),ns['exact'])
        ns=self.ns(4)
        self.assertEqual(sp.sqrt(ns['x']**2),sp.Abs(ns['x']))
        self.assertEqual(sp.sqrt(ns['p']**2),ns['p'])
        ns=self.ns(5)
        self.assertEqual(ns['swapped'],2*ns['x']+ns['y'])
        self.assertNotEqual(ns['swapped'],ns['sequential'])
    def test_cancelled_domain_and_solver_checks(self):
        ns=self.ns(9)
        self.assertEqual(ns['original'].subs(ns['x'],1),sp.nan)
        self.assertEqual(ns['reduced'].subs(ns['x'],1),2)
        ns=self.ns(14)
        self.assertEqual(sp.solveset(ns['expression'],ns['x'],domain=sp.S.Reals),sp.S.EmptySet)
        ns=self.ns(15);pair=next(iter(ns['solutions']))
        self.assertEqual(pair,sp.Tuple(6,4))
        ns=self.ns(16)
        self.assertEqual(ns['solutions'],sp.FiniteSet((-1,-2),(2,1)))
        self.assertTrue(all(all(c==0 for c in row) for row in ns['checks']))
        ns=self.ns(17)
        self.assertEqual(ns['region'].subs(ns['x'],1),sp.true)
        self.assertEqual(ns['region'].subs(ns['x'],3),sp.false)
    def test_calculus_and_linear_algebra_references(self):
        ns=self.ns(27);x,y=ns['x'],ns['y']
        self.assertEqual(ns['slope'],-x/y)
        ns=self.ns(29)
        self.assertEqual(ns['defined'].doit(),9)
        self.assertEqual(sp.diff(ns['antiderivative'],ns['x'])-ns['rate'],0)
        ns=self.ns(32)
        self.assertEqual(ns['A'].rank(),1)
        self.assertEqual(ns['A'].row_join(ns['bad_b']).rank(),2)
        ns=self.ns(35)
        self.assertEqual(ns['P']*ns['D']*ns['P'].inv(),ns['A'])
        self.assertFalse(ns['J'].is_diagonalizable())
        ns=self.ns(36)
        self.assertEqual(ns['A'].T*ns['residual'],sp.zeros(2,1))
        self.assertEqual(ns['coefficients'],sp.Matrix([sp.Rational(7,6),sp.Rational(1,2)]))
    def test_models_and_numerical_stability(self):
        ns=self.ns(37);self.assertEqual(ns['best'],4)
        for index in [39,40]:
            ns=self.ns(index)
            self.assertEqual(sp.checkodesol(ns['equation'],ns['solution']),(True,0))
        ns=self.ns(41)
        self.assertEqual(ns['mass'],1);self.assertEqual(ns['mean'],sp.Rational(2,3))
        self.assertEqual(ns['variance'],sp.Rational(1,18))
        ns=self.ns(45)
        reference=float(ns['direct'].evalf(40,subs={ns['x']:ns['exact_input']}))
        self.assertAlmostEqual(ns['stable_fn'](float(ns['exact_input']))/reference,1,places=12)
        self.assertGreater(abs(ns['direct_fn'](float(ns['exact_input']))-reference),reference*.5)
    def test_all_final_starters(self):
        lesson=LESSONS[-1];source=(ROOT/'python'/lesson['code']).read_text()
        for task in ['optimisation','ode','integral']:
            with self.subTest(task=task):
                ns,output=run(lesson,source.replace('task = "optimisation"',f'task = "{task}"'))
                self.assertTrue(ns['results']);self.assertTrue(output.strip())
        with self.assertRaises(ValueError):run(lesson,source.replace('task = "optimisation"','task = "unknown"'))
    def test_workshop_optimum_and_monte_carlo_reference(self):
        ns=self.runs[COURSE['applications'][0]['slug']][0]
        self.assertTrue(0<ns['best']<4)
        self.assertEqual(sp.simplify(sp.diff(ns['volume'],ns['x']).subs(ns['x'],ns['best'])),0)
        self.assertLess(float(sp.diff(ns['volume'],ns['x'],2).subs(ns['x'],ns['best'])),0)
        ns=self.runs[COURSE['applications'][3]['slug']][0]
        self.assertEqual(ns['exact_mean'],7*sp.pi/3)
        self.assertEqual(ns['exact_variance'],34*sp.pi**2/45)
        self.assertLess(abs(ns['estimate']-float(ns['exact_mean'])),6*ns['mcse'])
if __name__=='__main__':unittest.main()

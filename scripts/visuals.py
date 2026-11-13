# Copyright © 2026 Christopher Snow
"""Reference mathematical illustrations, calculated from explicit teaching models.

These accompany the explanation; they are never presented as the learner's run.
SVGs inherit the page's palette and have separate narrow/wide compositions.
"""
import html, math
import numpy as np
import sympy as sp

# expression(s), x domain, y range, formula, caption, optional markers/shading
GRAPHS = {
4: (['Abs(x)','x'],[-4,4],[-4.5,4.5],r'\sqrt{x^2}=|x|\quad(x\in\mathbb R)', 'The distance from zero is nonnegative. For negative real inputs, the two curves differ.'),
7: (['x**2+x-6'],[-4,3],[-7,8],r'x^2+x-6=(x+3)(x-2)', 'The two factors locate the two crossings of the horizontal axis.'),
9: (['x+1'],[-2,4],[-2,6],r'\frac{x^2-1}{x-1}=x+1\quad(x\ne1)', 'The open point preserves the original exclusion. The line approaches 2 at x = 1; the original fraction has no value there.'),
10: (['1/(x*(x+1))','1/x','-1/(x+1)'],[-3,2],[-5,5],r'\frac1{x(x+1)}=\frac1x-\frac1{x+1}', 'The green curve is the sum of the other two. All three are shown only away from their poles; x = 0 and x = −1 are excluded.'),
13: (['3*x+2','11'],[0,5],[0,18],r'3x+2=11\;\Longrightarrow\;x=3', 'Solving means finding an input where both sides have the same height.'),
15: (['10-x','8-2*x/3'],[0,10],[0,11],r'x+y=10,\quad2x+3y=24', 'The invented ticket constraints hold together at the intersection (6, 4).'),
18: (['x**3-x'],[-1.5,1.5],[-2,2],r'x^3-x=x(x-1)(x+1)', 'This teaching cubic has three crossings. Finding one numerically does not establish that all have been found.'),
19: (['x**2+1','(x+1)**2'],[-2,3],[-1,17],r'f(g(x))=x^2+1,\quad g(f(x))=(x+1)^2', 'Green: square then add one. Amber: add one then square. The order changes the rule.'),
22: (['Abs(x)'],[-3,3],[-.5,3.8],r'f(x)=\begin{cases}-x&x<0\\x&x\ge0\end{cases}', 'The two branches meet at zero. The condition determines which rule applies.'),
23: (['(x-1)**2*(x+2)'],[-3,2.4],[-5,8],r'p(x)=(x-1)^2(x+2)', 'At −2 the curve crosses the axis; at the double root 1 it touches and turns.'),
25: (['sin(x)/x'],[-5,5],[-.4,1.3],r'\lim_{x\to0}\frac{\sin x}{x}=1', 'The open point is a missing value, not a missing limit. The curve approaches 1 from both sides.'),
26: (['exp(x**2)','exp(1)+2*exp(1)*(x-1)'],[-.5,1.5],[-2,11],r'f(x)=e^{x^2},\quad f\prime(1)=2e', 'Green: the function. Amber: its tangent at x = 1. A derivative describes local slope.'),
29: (['2*x'],[0,3.5],[-.3,7.5],r'\int_0^3 2x\,dx=9', 'The shaded triangle has base 3 and height 6, so its area is 9. This agrees with the exact integral.'),
30: (['sin(x)','x-x**3/6+x**5/120'],[-4,4],[-2.5,2.5],r'\sin x\approx x-\frac{x^3}{6}+\frac{x^5}{120}', 'Green: sine. Amber: the degree-five polynomial about zero. Accuracy is local and deteriorates away from the expansion point.'),
32: (['3-x','3.5-x'],[-1,5],[-2,5],r'x+y=3,\quad2x+2y=7', 'The compatible equations describe the same line. Changing the second right side to 7 produces the parallel amber line, with no joint solution.'),
36: (['7/6+x/2'],[-.3,2.5],[0,3],r'\widehat y=\frac76+\frac12x', 'The three points are invented. Vertical segments show residuals from the least-squares line; a fitted line need not pass through each point.'),
37: (['x*(10-x)'],[0,7],[-2,28],r'\max_{0\le x\le4}\;x(10-x)', 'Shading marks the feasible interval. The unconstrained stationary point at 5 lies outside it; compare admissible candidates and endpoints.'),
38: (['x+x**2/2'],[0,4],[-.5,13],r's(t)=t+\frac12t^2\quad(a=1,\;v_0=1,\;s_0=0)', 'Illustrative motion with acceleration 1 m/s², initial velocity 1 m/s and initial position 0 m. Horizontal: time (s); vertical: position (m).'),
39: (['exp(-x)'],[0,4],[-.05,1.15],r'\frac{N(t)}{N_0}=e^{-u},\quad u=kt', 'A normalised decay curve. After u = log 2, half the initial amount remains; k sets the physical time scale.'),
40: (['1-exp(-x)'],[0,5],[-.05,1.15],r'\frac{v(t)}V=1-e^{-u},\quad u=\frac{t}{RC}', 'A normalised ideal charging curve. At one time constant, it reaches about 63% of the final voltage.'),
41: (['2*x'],[0,1.1],[-.1,2.3],r'f(x)=2x\;(0\le x\le1),\quad\int_0^1 f(x)\,dx=1', 'The density is zero outside [0, 1]. Probability is area: the shaded mass is one, while the height at a point is not its probability.'),
44: (['exp(-x)'],[0,4],[-.05,1.15],r'f(x)=e^{-x},\quad x\ge0', 'A reference curve for the authored model. Running the Python below produces a separate plot from your own numerical array.'),
48: (['x*(12-2*x)**2'],[0,6],[-5,140],r'V(x)=x(12-2x)^2,\quad0<x<6', 'Reference for the default open-box starter, using generic length units. Switching starter tasks changes your run below; this diagram remains the published reference.'),
50: (['12*x-9.81*x**2/2'],[0,24/9.81],[-.3,8.3],r'h(t)=12t-\tfrac12(9.81)t^2', 'Authored numerical illustration: launch speed 12 m/s, gravity 9.81 m/s², no drag. Horizontal: time (s); vertical: height (m). Only the physical flight is shown.'),
51: (['5*(1-exp(-10*x))','2.5'],[0,.5],[-.2,5.6],r'v(t)=5(1-e^{-10t}),\quad t_{1/2}=\frac{\log2}{10}', 'Authored circuit illustration with RC = 0.1 s and V = 5 V. Horizontal: time (s); vertical: voltage (V). The amber line is the half-voltage threshold.')
}
NARROW_FORMULAS={
19:r'\begin{gathered}f(g(x))=x^2+1\\g(f(x))=(x+1)^2\end{gathered}',
27:r'\begin{gathered}x^2+y^2=25\\\frac{dy}{dx}=-\frac xy\quad(y\ne0)\end{gathered}',
38:r'\begin{gathered}s(t)=t+\frac12t^2\\a=1,\;v_0=1,\;s_0=0\end{gathered}',
41:r'\begin{gathered}f(x)=2x\quad(0\le x\le1)\\\int_0^1 f(x)\,dx=1\end{gathered}',
48:r'\begin{gathered}V(x)=x(12-2x)^2\\0<x<6\end{gathered}',
49:r'\begin{gathered}V(x)=x(12-2x)(8-2x)\\0<x<4\end{gathered}',
51:r'\begin{gathered}v(t)=5(1-e^{-10t})\\t_{1/2}=\frac{\log2}{10}\end{gathered}'
}
MARKERS={7:[(-3,0,'−3'),(2,0,'2')],9:[(1,2,'excluded',True)],13:[(3,11,'(3, 11)')],15:[(6,4,'(6, 4)')],18:[(-1,0,''),(0,0,''),(1,0,'')],23:[(-2,0,''),(1,0,'')],25:[(0,1,'limit 1',True)],26:[(1,math.e,'')],37:[(4,24,'(4, 24)'),(5,25,'',True)],39:[(math.log(2),.5,'')],40:[(1,1-math.exp(-1),'')],51:[(math.log(2)/10,2.5,'')]}
# A transformation diagram exposes mathematical relationships rather than pretending to be a plot.
FLOWS={
3: ('Names and objects', [('Build',r'x\mapsto\operatorname{Symbol}(x)'),('Keep',r'\mathrm{expression}=x+1'),('Reassign Python name',r'x\mapsto10'),('Stored expression',r'\mathrm{expression}=x+1')], 'Assignment changes a Python name’s binding. The existing expression still refers to its original symbol object.'),
5: ('Swap both roles together',[('Original',r'x+2y'),('Simultaneous swap',r'x\mapsto y,\;y\mapsto x'),('New expression',r'y+2x')],'A simultaneous substitution uses the original roles for both replacements; it does not feed one replacement into the next.'),
8: ('Group by powers of x',[('Quadratic term',r'2a\;\cdot x^2'),('Linear term',r'(a+b)\;\cdot x'),('Constant term',r'b')], 'Read each variable term as coefficient × power. The coefficients are 2a and a + b; the constant term is b. The symbols a and b stay as parameters.'),
11: ('Make the denominators match',[('Two fractions',r'\frac1x+\frac1{x+1}'),('Same denominator',r'\frac{x+1+x}{x(x+1)}'),('One numerator',r'\frac{2x+1}{x(x+1)}')], 'Each numerator is multiplied by the missing factor. The original exclusions x = 0 and x = −1 still apply.'),
21: ('Principal logarithms keep a branch',[('Multiply first',r'(-1)(-1)=1'),('Then take log',r'\log1=0'),('Take logs first',r'\log(-1)+\log(-1)=2\pi i')], 'Over complex inputs, principal logarithms need not split across a product. The two paths differ by a full turn.'),
24: ('Build a sum from its steps',[('First term',r'1'),('Add the second',r'1+2=3'),('Add the third',r'3+3=6'),('Add the fourth',r'6+4=10')], 'At n = 4, the finite sum contains four terms. The closed form n(n + 1)/2 gives the same total.'),
33: ('An inverse reverses a map',[('Illustrative vector',r'v=\binom12'),('Apply A',r'Av=\binom43'),('Apply its inverse',r'A^{-1}Av=\binom12')], 'Here A has rows (2, 1) and (1, 1), so its determinant is 1. A singular matrix cannot undo every input this way.'),
35: ('Change coordinates, scale, return',[('Eigenvector coordinates',r'P^{-1}v'),('Scale coordinates',r'DP^{-1}v'),('Original coordinates',r'PDP^{-1}v=Av')], 'Columns of P are an eigenvector basis. This route requires an invertible P; not every matrix has such a basis.'),
43: ('Argument order changes the value',[('Symbolic rule',r'a x^2+1'),('Input order (x, a)',r'(3,2)\mapsto19'),('Swapped inputs',r'(2,3)\mapsto13')], 'The same formula receives different assignments when arguments are swapped. Keep the argument order with the callable.'),
45: ('Avoid subtracting nearly equal roots',[('Direct expression',r'\sqrt{x+1}-\sqrt{x}'),('Equivalent for x > 0',r'\frac1{\sqrt{x+1}+\sqrt{x}}'),('At x = 10¹⁶',r'\text{reference}\approx5\times10^{-9}')], 'The second form avoids subtracting two rounded square roots. Inspect the actual scalar calculations below; exact equivalence does not guarantee identical floating-point behaviour.'),
46: ('Input construction comes first',[('Exact mathematical tenth',r'\operatorname{Rational}(1,10)=\frac1{10}'),('Python float error',r'\begin{gathered}\operatorname{float}(0.1)-\frac1{10}\\\approx5.55\times10^{-18}\end{gathered}'),('Decimal text input',r'\operatorname{Float}(\text{“0.1”},50)')], 'Extra precision applied after a Python float retains its earlier rounding. A decimal string avoids that initial conversion but still creates a finite-precision value.'),
47: ('Code generation stops at source text',[('Derive in SymPy',r'x^2+\frac13'),('Generate C text',r'\texttt{pow(x, 2) + 1.0/3.0}'),('Next, outside this lab',r'\text{compile and validate}')], 'The build executes Python and prints C source. The C is not compiled, run or benchmarked here.')
}

class Canvas:
 def __init__(self,width,alt,height=300):self.w=width;self.h=height;self.parts=[];self.alt=alt
 def add(self,s):self.parts.append(s)
 def text(self,x,y,t,anchor='middle',cls=''):self.add(f'<text x="{x:g}" y="{y:g}" text-anchor="{anchor}" class="{cls}">{html.escape(str(t))}</text>')
 def line(self,x,y,X,Y,cls='axis'):self.add(f'<path d="M{x:g},{y:g} L{X:g},{Y:g}" class="{cls}"/>')
 def arrow(self,x,y,X,Y,cls='curve'):
  self.line(x,y,X,Y,cls);angle=math.atan2(Y-y,X-x)
  for delta in [-.45,.45]:self.line(X,Y,X-9*math.cos(angle+delta),Y-9*math.sin(angle+delta),cls)
 def circle(self,x,y,r=4,open=False):self.add(f'<circle cx="{x:g}" cy="{y:g}" r="{r}" class="{"hole" if open else "point"}"/>')
 def finish(self):return f'<svg class="concept-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.w} {self.h}" role="img" aria-label="{html.escape(self.alt,quote=True)}">'+''.join(self.parts)+'</svg>'

def graph(spec,width,index):
 expressions,xd,yd,formula,caption=spec
 c=Canvas(width,caption); L,R,T,B=64,width-28,42,254
 X=lambda x:L+(x-xd[0])/(xd[1]-xd[0])*(R-L)
 Y=lambda y:B-(y-yd[0])/(yd[1]-yd[0])*(B-T)
 if index==37:c.add(f'<rect x="{X(0)}" y="{T}" width="{X(4)-X(0)}" height="{B-T}" class="feasible"/>')
 # Ticks stay legible in the narrow composition.
 for x in np.linspace(*xd,5):
  c.line(X(x),T,X(x),B,'grid');c.text(X(x),B+22,f'{x:.3g}')
 for y in np.linspace(*yd,5):
  c.line(L,Y(y),R,Y(y),'grid');c.text(L-9,Y(y)+5,f'{y:.3g}','end')
 c.line(L,B,R,B);c.line(L,T,L,B)
 if yd[0]<0<yd[1]:c.line(L,Y(0),R,Y(0))
 if xd[0]<0<xd[1]:c.line(X(0),T,X(0),B)
 labels={38:('t (s)','s (m)'),39:('u = kt','N / N₀'),40:('u = t / RC','v / V'),50:('t (s)','h (m)'),51:('t (s)','v (V)')}
 xlab,ylab=labels.get(index,('x','y'));c.text((L+R)/2,294,xlab);c.text(L,28,ylab,'start')
 xs=np.linspace(*xd,321);x=sp.Symbol('x')
 for k,expression in enumerate(expressions):
  f=sp.lambdify(x,sp.sympify(expression),'numpy')
  with np.errstate(all='ignore'):ys=np.asarray(f(xs));ys=np.full_like(xs,ys) if ys.ndim==0 else ys
  if index in (29,41):
   bound=3 if index==29 else 1
   pts=[(X(0),Y(0))]+[(X(a),Y(b)) for a,b in zip(xs,ys) if 0<=a<=bound]+[(X(bound),Y(0))]
   c.add('<polygon class="area-fill" points="'+' '.join(f'{a:.2f},{b:.2f}' for a,b in pts)+'"/>')
  paths=[];current=[];previous=None
  for a,b in zip(xs,ys):
   good=np.isfinite(b) and yd[0]<=b<=yd[1]
   if index==41 and a>1:good=False
   if not good or (previous is not None and abs(b-previous)>(yd[1]-yd[0])*.5):
    if current:paths.append(current)
    current=[]
   if good:current.append((X(a),Y(b)));previous=b
   else:previous=None
  if current:paths.append(current)
  for path in paths:
   c.add('<path class="curve curve-'+str(k)+'" d="'+' '.join(('M' if j==0 else 'L')+f'{a:.2f},{b:.2f}' for j,(a,b) in enumerate(path))+'"/>')
 for p in MARKERS.get(index,[]):
  a,b,label,*hole=p;c.circle(X(a),Y(b),5,bool(hole and hole[0]))
  if label:c.text(min(R-34,max(L+35,X(a))),max(T+18,Y(b)-15),label)
 if index==36:
  for a,b in [(0,1),(1,2),(2,2)]:c.line(X(a),Y(b),X(a),Y(7/6+a/2),'residual');c.circle(X(a),Y(b),5)
 return c.finish()

def special(index,width,ns):
 caption='';formula=''; c=Canvas(width,'')
 if index==2:
  caption='Three exact thirds fill one whole. A rounded decimal is a nearby number, even when its printed sum looks like one.';formula=r'\frac13+\frac13+\frac13=1'
  for k in range(3):
   left=28+k*(width-56)/3;c.add(f'<rect x="{left}" y="84" width="{(width-56)/3}" height="94" class="tile tile-{k}"/>');c.text(left+(width-56)/6,139,'⅓')
  c.line(28,199,width-28,199);c.text(width/2,230,'one whole')
 elif index==6:
  caption='A zoomed number line separates the exact square root from rounded displays. More digits refine the numerical approximation, not the evidence behind an input.';formula=r'1.41<\sqrt2<1.42'
  X=lambda a:35+(a-1.40)/.03*(width-70)
  c.line(35,160,width-35,160)
  for a in [1.40,1.41,1.42,1.43]:c.line(X(a),152,X(a),168);c.text(X(a),195,f'{a:.2f}')
  c.circle(X(math.sqrt(2)),160,6);c.text(X(math.sqrt(2)),117,'√2');c.line(X(math.sqrt(2)),128,X(math.sqrt(2)),149,'residual')
 elif index==17:
  caption='A filled endpoint includes 1; an open endpoint excludes 3. The result is the intersection of both original inequalities.';formula=r'1\le x<3'
  X=lambda a:35+a/4*(width-70)
  c.line(25,150,width-25,150)
  for a in range(5):c.line(X(a),143,X(a),157);c.text(X(a),189,str(a))
  c.line(X(1),150,X(3),150,'interval');c.circle(X(1),150,7);c.circle(X(3),150,7,True)
 elif index in (12,20):
  angle=math.pi/4 if index==12 else math.pi/6
  caption='On the unit circle, horizontal and vertical coordinates are cosine and sine. The right triangle has hypotenuse 1; angles are in radians.'
  formula=r'\cos^2\theta+\sin^2\theta=1' if index==12 else r'\theta=\frac\pi6,\quad\sin\theta=\frac12'
  radius=min(100,(width-100)/2);cx=width/2;cy=148;xx=cx+radius*math.cos(angle);yy=cy-radius*math.sin(angle)
  c.add(f'<circle cx="{cx}" cy="{cy}" r="{radius}" class="circle-outline"/>');c.line(cx-radius-12,cy,cx+radius+12,cy);c.line(cx,cy-radius-12,cx,cy+radius+12);c.line(cx,cy,xx,yy,'curve');c.line(xx,yy,xx,cy,'residual');c.line(cx,cy,xx,cy,'curve curve-1');c.circle(xx,yy);c.text(cx+28,cy-9,'θ');c.text(width/2,284,'radius = 1')
 elif index==14:
  caption='The roots lie on the imaginary axis, not the real number line. An empty real solution set is consistent with two complex solutions.';formula=r'x^2+1=0\quad\Longrightarrow\quad x=\pm i'
  cx=width/2;c.line(35,150,width-35,150);c.line(cx,30,cx,270);c.text(width-40,180,'Re');c.text(cx+15,30,'Im','start')
  for y,label in [(75,'i'),(225,'−i')]:c.circle(cx,y,6);c.text(cx+18,y+6,label,'start')
 elif index in (16,27):
  r=math.sqrt(5) if index==16 else 5;scale=min((width-110)/(2*r+2),210/(2*r+2));cx=width/2;cy=146
  X=lambda x:cx+x*scale;Y=lambda y:cy-y*scale
  c.add(f'<circle cx="{cx}" cy="{cy}" r="{r*scale}" class="circle-outline"/>');c.line(X(-r-1),cy,X(r+1),cy);c.line(cx,Y(-r-1),cx,Y(r+1))
  if index==16:
   c.line(X(-2.1),Y(-3.1),X(3),Y(2),'curve curve-1')
   for a,b in [(-1,-2),(2,1)]:c.circle(X(a),Y(b),5);c.text(X(a)+(24 if a<0 else -16),Y(b)+(25 if a<0 else -10),f'({a}, {b})')
   caption='A line and circle intersect at two complete coordinate pairs. Both satisfy the original equations; selecting a branch needs an additional constraint.';formula=r'x^2+y^2=5,\quad y=x-1'
  else:
   c.line(X(0),Y(6.25),X(6),Y(1.75),'curve curve-1');c.circle(X(3),Y(4),5);c.text(X(3)-22,Y(4)-15,'(3, 4)');caption='At (3, 4), the circle has tangent slope −3/4. The formula −x/y requires y ≠ 0; at the horizontal extremes the tangents are vertical.';formula=r'x^2+y^2=25,\quad\frac{dy}{dx}=-\frac xy\;(y\ne0)'
 elif index in (28,31,34,42):
  if index==28:
   caption='Contours of x² + xy + y². The arrow from (1, 2) follows the gradient (4, 5); its length is scaled for display.';formula=r'\nabla f(1,2)=\binom45';lim=4;lines=[]
   # Eigenvectors of [[1,.5],[.5,1]] parametrise exact quadratic contours.
   eig,Q=np.linalg.eigh(np.array([[1,.5],[.5,1.]]));ts=np.linspace(0,2*np.pi,129)
   for level in [1,4,9,16]:lines.append((Q@np.diag(np.sqrt(level/eig))@np.array([np.cos(ts),np.sin(ts)])).T)
   arrows=[((1,2),(2,3.25),'gradient')]
  elif index==42:
   caption='Local covariance geometry for the invented rectangle inputs, in standardised output coordinates. The outline is not a confidence region; it shows the strong positive relationship from shared inputs.';formula=r'\Sigma_{\rm out}\approx J\Sigma_{\rm in}J^T';lim=2;ts=np.linspace(0,2*np.pi,129)
   cov=np.array(ns['output_covariance']).astype(float);scale=np.sqrt(np.diag(cov));corr=cov/np.outer(scale,scale);eig,Q=np.linalg.eigh(corr);lines=[(Q@np.diag(np.sqrt(eig))@np.array([np.cos(ts),np.sin(ts)])).T];arrows=[]
  else:
   lim=12 if index==31 else 4;lines=[]
   arrows=[((0,0),(3,4),'v'),((0,0),(11,4),'Av')] if index==31 else [((0,0),(1,1),'v'),((0,0),(3,3),'Av'),((0,0),(1,-1),'w = Aw')]
   caption='The map shears (3, 4) into (11, 4). Its vertical coordinate is unchanged.' if index==31 else 'Along v = (1, 1), the matrix scales by 3. Along w = (1, −1), it scales by 1. Both directions stay on their own lines.'
   formula=r'\begin{pmatrix}1&2\\0&1\end{pmatrix}\binom34=\binom{11}4' if index==31 else r'A=\begin{pmatrix}2&1\\1&2\end{pmatrix}'
  lo=-1 if index==31 else -lim;scale=min((width-90)/(lim-lo),205/(lim-lo));cx=(width-(lim+lo)*scale)/2;cy=145+(lim+lo)*scale/2;X=lambda a:cx+a*scale;Y=lambda b:cy-b*scale
  c.line(X(lo),Y(0),X(lim),Y(0));c.line(X(0),Y(lo),X(0),Y(lim))
  for pts in lines:c.add('<path class="curve" d="'+' '.join(('M' if j==0 else 'L')+f'{X(a):.2f},{Y(b):.2f}' for j,(a,b) in enumerate(pts))+'"/>')
  for k,(start,end,label) in enumerate(arrows):
   a,b=start;d,e=end;c.arrow(X(a),Y(b),X(d),Y(e),'curve curve-'+str(k));c.circle(X(a),Y(b),3);c.text(X(d)-12,Y(e)-12,label)
  c.text(width/2,287,'area (standard deviations)' if index==42 else 'equal axis scale')
  if index==42:c.text(18,22,'perimeter (standard deviations)','start')
 elif index==49:
  caption='An unfolded 12 cm × 8 cm sheet with illustrative cuts x = 1.5 cm. Remove the four amber corners, then fold along the dashed lines. Dimensions are schematic.';formula=r'V(x)=x(12-2x)(8-2x),\quad0<x<4'
  s=(width-68)/12;left=34;top=45;cut=1.5*s
  c.add(f'<rect x="{left}" y="{top}" width="{12*s}" height="{8*s}" class="tile tile-0"/>')
  for xx in [left,left+12*s-cut]:
   for yy in [top,top+8*s-cut]:c.add(f'<rect x="{xx}" y="{yy}" width="{cut}" height="{cut}" class="tile tile-1"/>')
  for xx in [left+cut,left+12*s-cut]:c.line(xx,top,xx,top+8*s,'residual')
  for yy in [top+cut,top+8*s-cut]:c.line(left,yy,left+12*s,yy,'residual')
  c.text(width/2,top+4*s+6,'base');c.text(width/2,28,'12 cm');c.text(left+cut/2,top+cut+23,'x')
  c.h=top+8*s+35;c.text(width/2,c.h-6,'fold on dashed lines')
 elif index==52:
  caption='Distribution from the published seeded simulation: 20,000 independent radii uniform on [1, 2], transformed into area. The amber marker is the exact model mean; this is a worked reference, not your run.';formula=r'E[\pi r^2]=\frac{7\pi}3,\quad r\sim U(1,2)'
  counts,edges=np.histogram(ns['simulated'],bins=15);left=40;right=width-24;top=35;bottom=242
  X=lambda a:left+(a-math.pi)/(3*math.pi)*(right-left)
  for n,a,b in zip(counts,edges,edges[1:]):h=n/counts.max()*180;c.add(f'<rect x="{X(a)}" y="{bottom-h}" width="{max(1,X(b)-X(a)-1)}" height="{h}" class="hist-bar"/>')
  c.line(left,bottom,right,bottom);c.line(X(7*math.pi/3),top,X(7*math.pi/3),bottom,'residual');c.text(X(7*math.pi/3),22,'exact mean');c.text(left,bottom+24,'π');c.text(right,bottom+24,'4π');c.text(width/2,291,'area (squared length units)')
 else:raise ValueError(f'No illustration for lesson {index}')
 c.alt=caption;return dict(caption=caption,formula=formula,svg=c.finish())

def illustration(index,namespace):
 if index==1:return {'kind':'area','title':'See the expansion','caption':'A square with side x + 1 contains one x² square, two x rectangles and a unit square. This geometric interpretation uses x ≥ 0; the polynomial identity also holds beyond that geometric domain. Dimensions are schematic.','formula':r'(x+1)^2=x^2+\underbrace{x+x}_{2x}+1'}
 if index in FLOWS:
  title,steps,caption=FLOWS[index];return {'kind':'flow','title':title,'steps':steps,'caption':caption,'mode':'parts' if index==8 else 'comparison' if index in (21,43,46) else 'sequence'}
 if index in GRAPHS:
  spec=GRAPHS[index];return {'kind':'graph','title':'See the mathematics','caption':spec[4],'formula':spec[3],'narrow_formula':NARROW_FORMULAS.get(index),'legend':[sp.latex(sp.sympify(e).subs(sp.Symbol('x'),sp.Symbol('t'))) if index==51 else sp.latex(sp.sympify(e)) for e in spec[0]] if len(spec[0])>1 else [],**{key:graph(spec,w,index) for key,w in [('wide',640),('narrow',320)]}}
 wide=special(index,640,namespace);narrow=special(index,320,namespace)
 return {'kind':'diagram','title':'See the mathematics','caption':wide['caption'],'formula':wide['formula'],'narrow_formula':NARROW_FORMULAS.get(index),'wide':wide['svg'],'narrow':narrow['svg']}

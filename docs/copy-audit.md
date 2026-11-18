# SymPy Lab wording and interface audit

## Opening check

Reviewed the 48 lessons, four optional workshops, overview and field notes on
`dc25b22`. A learner should be able to read basic Python assignments,
functions, lists and a loop. At entry the course supplies the algebra it needs.
The module map states what later calculus and linear algebra lessons build on.
The optional refresher brings back a particular prerequisite. The main route
still explains the mathematical idea required to carry out the current task.

The earlier review covered cancellation, one-sided limits and matrix inverses
plus run and draft recovery. For this review I read the authored headings,
goals, explanations, predictions, labels, evidence prompts, editor changes,
questions, options, hints, feedback, limitations, refreshers and illustration
captions against the Python and worked result. I checked the overview, field
notes and what the browser shows before a run, after a run, during a later
action and on returning with a saved draft. The learning-design and UX skills
guided the opening check, implementation and closing check.

The main gap was between a meaningful mathematical change and the specific
Python action needed to make it. Some exercises also had a second formula,
label or bound that would remain unchanged after the edit. Typical examples
were a plot stopping at the old projectile return time and a circuit residual
that still subtracted half the final voltage. The shared notes status could
also imply a save before a write, and a blocked progress read could yield an
empty download described as a successful export.

## Route checks

Each row records the main evidence compared after the literal editor task.
Original results and edited variants were executed in Python. The browser
walkthrough used the editable source on each actual route, ran the original,
applied the edits, ran them and compared labelled output with native results.
For tasks with intermediate runs, the checks use each named setting.

| Route | Evidence from the checked comparison |
| --- | --- |
| Overview | The start link goes to the first unread core lesson, or opens course contents when all 48 are marked read. Search and the worked assumption example remain available. A blocked progress read reports that no file was downloaded. |
| Field notes | The prerequisite map links to each module. Runtime notes distinguish the browser, the build-executed reference, generated C text, local storage and portable records. The import description matches replacement of same-key entries. |
| [Your first symbolic expression](https://snowch.github.io/sympy-lab/lessons/your-first-symbolic-expression.html) | The expanded square changes to x² + 4x + 4, and the strip and corner dimensions follow the edited offset. |
| [Keep numbers exact](https://snowch.github.io/sympy-lab/lessons/keep-numbers-exact.html) | The written tenth is exact. Extra digits in the Float expose the stored Python value rather than recovering the tenth. |
| [A symbol is an object](https://snowch.github.io/sympy-lab/lessons/a-symbol-is-an-object.html) | The original expression retains x. Changing another symbol does not change the expression or make the objects equal. |
| [Tell SymPy what a symbol means](https://snowch.github.io/sympy-lab/lessons/tell-sympy-what-a-symbol-means.html) | The square root returns p for nonnegative p and -p for negative p. |
| [Substitute deliberately](https://snowch.github.io/sympy-lab/lessons/substitute-deliberately.html) | Sequential replacement simplifies to 1, whereas the simultaneous swap gives y/x, within the specified domain. |
| [Choose when to approximate](https://snowch.github.io/sympy-lab/lessons/choose-when-to-approximate.html) | The exact symbolic pi becomes an approximate Python float. More output digits preserve that approximation. |
| [Expand or factor?](https://snowch.github.io/sympy-lab/lessons/expand-or-factor.html) | The rational factor call leaves the polynomial unchanged. The complex extension factors it into x−i and x+i with zero residual. |
| [Collect the terms you need](https://snowch.github.io/sympy-lab/lessons/collect-the-terms-you-need.html) | The x² coefficient is 2a+b. |
| [Cancel with the domain in view](https://snowch.github.io/sympy-lab/lessons/cancel-with-the-domain-in-view.html) | The excluded input becomes 2. The reduced polynomial equals 4 there and the original remains undefined. |
| [Separate partial fractions](https://snowch.github.io/sympy-lab/lessons/separate-partial-fractions.html) | The decomposition has coefficients 1/2 and −1/2, with 0 and −2 excluded. |
| [Build a common denominator](https://snowch.github.io/sympy-lab/lessons/build-a-common-denominator.html) | The new numerator is 3x−1. Both −1 and 1 are excluded. |
| [Simplify towards a goal](https://snowch.github.io/sympy-lab/lessons/simplify-towards-a-goal.html) | The expressions agree at 0 and 1, but disagree at 2. The difference factors as x(x−1). |
| [Write an equation, then solve it](https://snowch.github.io/sympy-lab/lessons/write-an-equation-then-solve-it.html) | The exact candidate is 9/5 with original residual 0. |
| [State the solution domain](https://snowch.github.io/sympy-lab/lessons/state-the-solution-domain.html) | Both sets contain −1 and 1, and both residuals are zero. |
| [Solve a linear system](https://snowch.github.io/sympy-lab/lessons/solve-a-linear-system.html) | The new tuple is (5,5) and satisfies both the equations and integer-count condition. |
| [Solve a nonlinear system](https://snowch.github.io/sympy-lab/lessons/solve-a-nonlinear-system.html) | The pairs become (0,−1) and (1,0), each with two zero residuals. |
| [Solve an inequality as a region](https://snowch.github.io/sympy-lab/lessons/solve-an-inequality-as-a-region.html) | The right boundary x=3 becomes included. |
| [A numerical root needs a check](https://snowch.github.io/sympy-lab/lessons/a-numerical-root-needs-a-check.html) | The candidate is approximately 0.7391 with a small original residual, an observation about that run. |
| [Compose functions in the right order](https://snowch.github.io/sympy-lab/lessons/compose-functions-in-the-right-order.html) | At input 2 the two orders give 8 and 16. |
| [Use a trigonometric identity](https://snowch.github.io/sympy-lab/lessons/use-a-trigonometric-identity.html) | The converted angle is π/3, with exact cosine 1/2. |
| [Respect logarithm branches](https://snowch.github.io/sympy-lab/lessons/respect-logarithm-branches.html) | The square variant gives 2 log(a) for the positive input and retains log(z²) for the unrestricted input. |
| [Define a piecewise rule](https://snowch.github.io/sympy-lab/lessons/define-a-piecewise-rule.html) | The invented tariff gives 5 below 20 and 0 at and above 20. |
| [Read a polynomial and its roots](https://snowch.github.io/sympy-lab/lessons/read-a-polynomial-and-its-roots.html) | Degree becomes 4 and the root at 1 has multiplicity 3. |
| [Sum a family of terms](https://snowch.github.io/sympy-lab/lessons/sum-a-family-of-terms.html) | The square sum at 3 is 14. |
| [A limit is not a substitution](https://snowch.github.io/sympy-lab/lessons/a-limit-is-not-a-substitution.html) | The one-sided values are −1 and 1, so the two-sided limit does not exist. |
| [Differentiate a composed expression](https://snowch.github.io/sympy-lab/lessons/differentiate-a-composed-expression.html) | The inner derivative becomes the constant 3. |
| [Differentiate an implicit curve](https://snowch.github.io/sympy-lab/lessons/differentiate-an-implicit-curve.html) | The new slope is −x/(4y), and both new test points lie on the ellipse. |
| [Take one partial derivative at a time](https://snowch.github.io/sympy-lab/lessons/take-one-partial-derivative-at-a-time.html) | The components gain 3y and 3x respectively. |
| [Integrate and check by differentiating](https://snowch.github.io/sympy-lab/lessons/integrate-and-check-by-differentiating.html) | The new antiderivative is x³+C and the definite integral is 8. |
| [Keep the remainder in a series](https://snowch.github.io/sympy-lab/lessons/keep-the-remainder-in-a-series.html) | The series is centred at 1. Removing the order term leaves a polynomial with the stated local scope. |
| [A matrix acts on a vector](https://snowch.github.io/sympy-lab/lessons/a-matrix-acts-on-a-vector.html) | The two basis inputs select columns (1,0) and (2,1). |
| [Rank explains a family of solutions](https://snowch.github.io/sympy-lab/lessons/rank-explains-a-family-of-solutions.html) | Both compatible ranks rise to 2. The new equation selects the pair (2,1). |
| [Check an inverse by multiplication](https://snowch.github.io/sympy-lab/lessons/check-an-inverse-by-multiplication.html) | The determinant becomes zero, so the code reports no inverse without an execution error. |
| [Find directions that keep their line](https://snowch.github.io/sympy-lab/lessons/find-directions-that-keep-their-line.html) | The alternate direction has eigenvalue 1 and zero residual. |
| [Use a different coordinate basis](https://snowch.github.io/sympy-lab/lessons/use-a-different-coordinate-basis.html) | The power residual remains zero for A. J has only one independent eigenvector. |
| [Fit a small line exactly](https://snowch.github.io/sympy-lab/lessons/fit-a-small-line-exactly.html) | A line with intercept and slope both 1 fits every point, leaving zero residual and squared error. |
| [Optimise inside the permitted region](https://snowch.github.io/sympy-lab/lessons/optimise-inside-the-permitted-region.html) | The solution x=5 becomes feasible and gives the best value 25. |
| [Derive motion from an acceleration](https://snowch.github.io/sympy-lab/lessons/derive-motion-from-an-acceleration.html) | The zero-velocity time changes from 2.5 to 2 seconds, both admissible. |
| [Solve a decay equation](https://snowch.github.io/sympy-lab/lessons/solve-a-decay-equation.html) | Doubling the rate halves the half-life and reduces the fraction remaining at 5 seconds. |
| [Derive a charging response](https://snowch.github.io/sympy-lab/lessons/derive-a-charging-response.html) | The transient coefficient changes while the ideal long-time voltage remains V. |
| [Integrate a probability density](https://snowch.github.io/sympy-lab/lessons/integrate-a-probability-density.html) | The multiplier is 3, mass remains 1 and the mean moves from 2/3 to 3/4. |
| [Propagate small input uncertainty](https://snowch.github.io/sympy-lab/lessons/propagate-small-input-uncertainty.html) | The approximate area variance increases from 1/4 to 37/100. |
| [Turn a formula into a numerical function](https://snowch.github.io/sympy-lab/lessons/turn-a-formula-into-a-numerical-function.html) | The third position controls b. Both evaluation routes give 22, while swapping the first two positions gives 16. |
| [Evaluate a curve on an array](https://snowch.github.io/sympy-lab/lessons/evaluate-a-curve-on-an-array.html) | The plot covers a full sine period. Both grid sizes use the same endpoints, while the lower count samples fewer points between them. |
| [Rewrite a cancellation-prone calculation](https://snowch.github.io/sympy-lab/lessons/rewrite-a-cancellation-prone-calculation.html) | The direct evaluation loses accuracy as the input grows. At 10¹⁶ it gives zero, while the rewrite remains near 5×10⁻⁹. |
| [Precision starts with the input](https://snowch.github.io/sympy-lab/lessons/precision-starts-with-the-input.html) | Starting with the Python literal loses decimal information before the 50-digit Float is constructed. |
| [Export an expression as code](https://snowch.github.io/sympy-lab/lessons/export-an-expression-as-code.html) | The code prints C exp calls and SymPy’s symbolic derivative. No C compilation or execution is part of this calculation. |
| [Publish a checked symbolic investigation](https://snowch.github.io/sympy-lab/lessons/publish-a-checked-symbolic-investigation.html) | Switching to the differential equation replaces the domain and boundary evidence with an equation residual and initial-value check. |
| [Design an open box](https://snowch.github.io/sympy-lab/lessons/design-an-open-box.html) | The open domain moves to (0,9/2). Both limiting volumes stay zero, and the optimiser still selects a strictly interior cut. |
| [Check a projectile model](https://snowch.github.io/sympy-lab/lessons/check-a-projectile-model.html) | The elevated launch gives one negative and one positive root. The plot uses the positive crossing after launch. |
| [Plan a circuit threshold time](https://snowch.github.io/sympy-lab/lessons/plan-a-circuit-threshold-time.html) | The fixed threshold requires V>2 and the time now depends on V, with zero symbolic residual on the stated domain. |
| [Benchmark a Monte Carlo estimate](https://snowch.github.io/sympy-lab/lessons/benchmark-a-monte-carlo-estimate.html) | The fourfold draw count roughly halves estimated MCSE. The particular simulated means depend on the seed. |


## Closing check

- **Clear action and evidence.** Every change starts with named source text or a
  setting, makes the runnable action explicit and names an output to compare.
  The linked return control focuses the editor without requiring the learner to
  scroll past the result. The unchanged-code cue appears with the published
  code. A saved edit has its own cue and recovery instructions.
- **Mathematical scope.** The editable fraction, rational transforms and solver
  comparisons keep domain restrictions visible. The domain and residual labels
  describe the actual inputs. Exact values, early Python floats, numerical
  results, finite grids and generated C source have distinct labels. Static
  illustrations say they describe the starter. The three modelling workshops
  tie the edited bounds, crossing check and plot back to the same source
  settings.
- **Reading path.** From the goal and prediction, the prominent Run Python
  button leads to its real output, then the edit and fresh case. Refresher,
  tools, notes, published worked output and hints can remain closed.
  The C-generation lesson opens its essential text output after execution.
  Labels distinguish mathematical checks from execution errors and the
  retained previous result. The capstone reports whether an export includes a
  successful run.
- **Saved work.** The storage schema and keys, including refresher and replaced
  draft entries, remain compatible. Failed notes writes explain where the open
  text remains. The code warning appears on the reading surface. An older
  durable draft reloads unchanged after a quota error. Progress export
  reports a blocked read instead of offering an empty success. Local draft
  recovery and failed-run exports still use the most recent applicable
  saved draft or successful execution.
- **Interface.** Checked keyboard exit from the editor, keyboard activation of
  Run, Stop and return-to-editor, reflow with relevant panels closed and open,
  phone/tablet/desktop widths, both themes, 200% text, runtime error recovery
  and JavaScript-free reading. Worked result and actual output preserve
  separate labels. No changes rely on an optional refresher just to reach the
  editor or complete the primary action.

### Functional evidence and scope

Native tests cover all 52 published sources and 58 literal editor changes. The
Playwright gate checks shared controls, exact LaTeX and numeric comparisons,
storage and exports. A separate learner walkthrough followed the same 52
routes and 58 edits with the original code, real Python execution, labelled
results and keyboard return to the editor. Original and edited values agreed
with the native executions under the supplied teaching assumptions.

The curve and circuit outputs are idealised model calculations. The simulation
uses an authored uniform distribution and seeded draws. The project-source
exercise prints C text without compiling or executing it. These checks show
that the examples and interface behave as described. Learner interpretation
and transfer remain unmeasured.

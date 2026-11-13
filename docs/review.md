# Review record

## Scope and mathematical sources

48 core investigations across eight modules, plus four integrated workshops. Each has an optional maths refresher with a plain explanation, equation and worked prerequisite example. The route covers expressions, exact numbers, assumptions, domains, algebraic representation, solving, functions, calculus, matrices, small models and numerical evaluation.

Official SymPy tutorials and guides support the methods. Executable SymPy is pinned to 1.13.3; documentation links use the public latest documentation, which may describe newer releases. Examples are authored for this course and executed against the pinned version. Invented observations, dimensions, component values and probability models are labelled at point of use.

Explicit boundaries: cancellation retains original exclusions; principal complex logarithms need branch conditions; numerical roots are local candidates; derivative-zero conditions do not alone classify or establish a feasible optimum; improper integration needs convergence; exact least squares is not statistical validation; Jacobian covariance is first order; generated C is printed, not compiled; an exact model reference is not empirical model validation.

## Learning-design review

With optional panels closed, the route states one outcome, explains an idea, asks for a prediction and provides a complete executable experiment. It continues with an observation prompt, deliberate change, fresh transfer case, two hints, feedback, limitation and primary reference. No hidden prior notebook variables are needed. The `results` dictionary links labelled mathematical output to visible source.

The refresher sits immediately before the main explanation and is labelled optional. It reviews the particular prerequisite rather than adding an unrelated textbook chapter. Its open state saves per lesson and travels with draft exports. A field-notes prerequisite map links modules and common reminders. Main explanations still define the new concept instead of making essential instruction depend on finding an optional panel.

Integrated workshops intentionally combine objectives and take longer: open-box design, a vertical trajectory, an ideal RC threshold and an exact-versus-Monte-Carlo check. The final core lesson offers optimisation, ODE and integral starters and an exportable report. Learners must record their assumptions and interpretation, not only copy a final expression.

## UX review

Before implementation: preserve large type and the recoverable worker editor from existing labs; introduce a calm forest-green and ink palette, a symbolic demonstration and a visible prerequisite route. Keep mathematical notation adjacent to code and preserve a plain text representation. Optional panels should not interrupt learners who already know the prerequisite.

After implementation: desktop and 390px screenshots reviewed. The overview uses executed square-root simplifications to demonstrate assumptions. Headings are large Sora; prose is DM Sans at 20px desktop and 18px on phones; code and text output are at least 16px. The expanded refresher combines short prose, an equation and a small example in one readable region. Matrix and long-expression output scrolls within its card. Figures offer full-size viewing.

The editor and results follow one flow on ordinary laptop widths. Loading, completed, stale, error and stopped states explain what the visible output represents. Errors open text details; Reset restores authored code; Stop kills the worker and supports restarting. Exports preserve completed source separately from later edits. Contents use collapsible modules, with a keyboard-accessible phone toggle and Escape recovery. Local fonts, math assets and runtime avoid third-party page requests. A skip link, labels, visible focus and MathML output are retained.

## Executable evidence

`npm run check` combines:

- Native execution of all 52 sources, checking exact fractions, assumptions, original domain exclusions, solution domains, equation residuals, derivatives, rank, diagonalisation, least-squares conditions, ODE checks, density moments, cancellation stability, all three final starters and a Monte Carlo estimator against its exact reference.
- A build that executes exact published code to generate worked text, 217 labelled symbolic records and five figures. Every refresher and worked expression is rendered with KaTeX errors treated as build failures.
- Relative links, fragments and duplicate IDs across all 54 generated pages.
- Real browser/Wasm execution of all 52 sources with native text and LaTeX agreement. The browser suite checks all refresher panels, saved state, the three capstone paths, exact-source run/report export, full-size figures, error and Stop recovery, feedback, drafts and fresh-context progress import. It checks all lesson pages at 320px and 390px with refresher and worked maths open, 200% text reflow, both themes, and reading/refreshers/worked mathematics with JavaScript disabled.

Screenshots and exported run/report/progress fixtures are generated in `test-results/` and uploaded by CI. GitHub Actions records the final check and Pages deployment outcome. No execution output is hand authored.

## Evidence gaps

These are author review, mathematical reference checks and browser checks, not learning-effectiveness evidence. No learner study has evaluated whether the panels supply the right prerequisite support. A useful follow-up observes learners with rusty algebra on exact fractions, square-root assumptions, cancellation and a first derivative, then a new transfer task without hints. Record which panels they need, whether the examples resolve the gap and whether they can explain the resulting assumptions independently.

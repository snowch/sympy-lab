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


## 2026-11-13 — visual clutter review

Prompted by the user's tablet screenshots and concern that the UI is noisy. Reviewed the live overview plus first, middle and capstone lessons at 390px, 820px and 1440px. This is a design review; it makes no frontend or deployment change. Browser observations and screenshots are held in the workspace's `scratch/course-ui-review/` directory.

The shared lesson template exposes too much supporting structure at once. At 820px, this course's first explanatory paragraph starts at about 725px and its editor at 1642px. These coordinates are observations of the current initial state, not usability targets or learner-study results. Prior tests checked execution, readability and reflow; they did not establish low cognitive load.

High-priority recommendations:

1. Use one compact lesson navigation bar. Keep one small module/lesson context line, title and one-sentence learning intention. Remove the duplicate outcome card and permanent numbered jump-navigation row from ordinary short lessons.
2. Create an editorial reading flow with plain headings and whitespace. Reserve framing for the executable workspace and meaningful exceptional states. Present the change task and ordinary answer choices without separate coloured or bordered cards.
3. Replace the empty pre-run result panel and repeated ready/no-result/device messages with one compact status. Show the result area after execution; keep one clear provenance label then. Expose Stop during execution and export after a completed run. Keep error, stale-output and recovery information available when relevant.
4. Put runtime details, keyboard help, downloads and ancillary actions behind a secondary control. Make notes and hints optional disclosures. Keep source/provenance and scientific or mathematical limitations available without repeating boilerplate throughout every lesson.
5. Preserve the current large reading/code type, course depth, predictions, experiments, transfer questions and accessibility. The target is a calmer presentation of the same learning design, rather than adding another colour scheme or reducing text size.

Course-specific findings: The shared template additionally displays a prerequisite line and a prominent maths-refresher panel before the explanation. Keep the refresher requested by the user, with one quiet disclosure line and a readable expanded example. Actual and worked mathematics currently frame each labelled expression separately; use a shared results area with lightweight labels and equations. Preserve MathML, exact/plain-text alternatives and horizontal scrolling for long notation.

Proposed default sequence: compact course context; title and one goal; explanation; prediction and experiment; actual results when present; one practice question; next lesson. Optional help belongs beside the relevant activity. Scientific Method Lab is the appropriate reference for a later shared-template simplification, followed by Monte Carlo Lab and SymPy Lab.

Evidence gap: this is a screenshot/live-browser and author review, not an observed learner study. The user's screenshots provide real qualitative evidence that the existing visual hierarchy is distracting. A revised design should be checked at tablet widths as well as the existing phone and desktop widths, including before-run, running, error and completed-result states.


## 2026-11-13 — quiet interface implementation

Implemented the clutter review across the course overview and lesson layout.
The shared renderer is in `scripts/quiet.mjs`, with local copies in each course
so deployment remains independent. `src/quiet.css` is combined into the existing
content-fingerprinted stylesheet.

- One compact header, one context line and one visible learning goal. Removed
  the duplicate outcome card, numbered section-jump bar and secondary mobile bar.
- Prediction questions remain visible; recording a prediction and writing notes
  are optional. Saved text reopens its disclosure. Ordinary instructions, answer
  options, change tasks and reading marks use lightweight editorial styling.
- No empty pre-run output panel or repeated readiness/device boilerplate. Actual
  output and its provenance appear after a result. Stop appears during execution;
  export appears for a recorded run. Runtime information and downloads are under
  Tools. Escape restores focus from support menus.
- Native module disclosures replace the overview's card grid and marketing
  sections. Search opens matching modules, clearing search restores their prior
  state, and module hashes open their target. Example previews and portable-work
  controls remain available below the curriculum.
- SymPy's refreshers remain available as quiet disclosures; labelled equations
  share an unboxed results area. Code, mathematical examples, CSV interfaces,
  reports, exact-source exports and package versions are preserved.

Fresh 820px-wide before/after inspection of the first lesson: explanation starts
at approximately 725px → 323px; editor starts at 1642px → 920px;
initial page height is 4345px → 2615px. These are measured rendering
coordinates for this sample, not learning-outcome claims. Also inspected 390px
and 1440px screenshots. Main reading text remains 20px on desktop/tablet and
18px on phones, with 16px code.

Verification retains the full native and real-Wasm suites, plus initial-state
checks and targeted 820/1024px regressions for tablet navigation, optional tools,
search, module deep links and source access. Existing phone, 200% text, saved
draft, progress, mathematical output, CSV/report, error/Stop and static-reading
checks remain in place. This visual/functional review does not replace a learner
study; further density feedback from actual course use remains valuable.

Local verification completed: the full native and real-Wasm browser suites passed
for the quiet layout. After the final focus/save-error adjustments, rebuilt all
three sites, rechecked their local links and ran focused browser checks for
820/1024px navigation and deep links, Stop focus return, cancelled-run output,
optional hints/notes, saved text reopening and unavailable-storage alerts.
GitHub Actions runs the complete suite again before each Pages deployment.

## Mathematical notation and visual teaching revision — 13 November 2026

The user’s screenshots exposed the cost of the previous simplification: raw Python-like expressions in explanations, no concept illustration on the first lesson, detached text/reference disclosures and weak grouping around the results. The UX and learning-design skills were applied before implementation and after screenshot review.

The essential route now includes one mathematical reference illustration per lesson: 52 across the core route and workshops. Area partitions, number lines, unit circles, curves, holes, tangents, contours, vector maps, covariance geometry and an unfolded box explain the particular concept. Transformation and comparison diagrams cover ideas such as object binding, denominator construction and numerical input provenance. Alternatives are not joined by sequence arrows; grouped polynomial terms use addition. Illustrations have visible captions, mathematical scope and accessible descriptions, work without JavaScript, and use separate narrow/wide SVG compositions where needed. Their palette follows the explicit page theme. These are authored reference models, separate from the learner’s execution. The Monte Carlo reference histogram uses the actual seeded build execution.

Main prose, predictions, changes, feedback and refresher examples use explicit `$LaTeX$` for maths and backticks for literal Python. A shared escaping formatter preserves that distinction in the static build and browser feedback. The first lesson pairs $(x+1)^2$ with `(x+1)**2`; its Python syntax assessment deliberately preserves the literal `**` and `^` choices. API syntax is never silently translated into a different mathematical operation.

Code, actual symbolic results, text output and the executed reference share one experiment surface. There is no empty result panel before execution. Actual results remain labelled and exported separately from the build reference; stale source and errors retain their existing provenance. A bounded area model derives from the actual returned `Original` expression, updates after changing the offset, and travels with the exact-source run export. It disappears for unsupported expressions and for assumptions incompatible with the geometric interpretation. Its caption states the nonnegative-real scope and schematic dimensions.

Review covered first-lesson tablet/phone screenshots before and after running, plus narrow light/dark concept screenshots for cancellation, curve intersections, gradients, diagonalisation, covariance, box geometry and Monte Carlo. A label-bounds audit found and corrected graph axis headings and an unnecessarily long scientific-notation tick. Diagram labels are checked inside their SVG bounds. Eight long reference equations were split across lines on narrow screens; a 320px audit confirms every visible concept equation fits without horizontal scrolling. Curve keys name each rule and use line patterns as well as colour. The native suite also checks the live area representation against exact symbolic expansion and refuses incompatible domains. Existing Wasm, error/Stop, export, draft, theme, keyboard, no-JavaScript and reflow coverage is retained. Browser evidence is under `test-results/` and is uploaded by the existing Pages workflow.

These illustrations and author/browser checks have not been evaluated in a learner study. Static reference diagrams do not change when a learner edits a model; executed plots and the first lesson’s live area model are explicitly separate.

## 2026-11-14 — illustrated course introduction

Applied the repository learning-design and UX skills before and after the
homepage work. The new original SVG shows an algebra notebook and pencil, with
a square partitioned into x², x, x and 1. The two unit-width strips have equal
width/height, and the corner is a square. Its accessible description identifies
nonnegative area lengths. The user-provided Common Ground screenshot guided
the composition; the artwork and code are original.

A deep green hero pairs that scene with the course promise and existing
Start/Continue, before-start and prerequisite-map links. It stacks after the
text on phones and preserves course search, module links and saved progress.
Mathematical results, optional refreshers and lesson editor/output behaviour
remain in their established reading flow. The vector is embedded locally and
uses text/shapes with no remote image dependency or animation.

Verification: all eight native tests passed across 52 standalone sources. The
complete real-Wasm suite checked native text/LaTeX agreement, all refreshers,
live area models, reports, drafts, progress, error/Stop recovery, both themes,
320/390px, 200% text and JavaScript-free reading. Link checks passed for 54 pages
and 3,760 relative links/fragments. Rebuilt after final illustration/styling
refinements and repeated focused hero and quiet-layout checks. Captured the
three heroes at 320/390/820/1440px and checked text enlargement and artwork label
bounds. Inspected phone/tablet/desktop and dark-theme captures. Local evidence
is in test-results/hero-*.png; these checks do not establish learner outcomes.
## Exercise directions and successful-run recovery — 17 November 2026

Applied the local learning-design and UX skills. The cancellation exercise
uses one hole setting and finds the zeros of the original denominator before
interpreting the cancelled polynomial. The edited limit feeds both one-sided
calculations. The inverse exercise checks the determinant before inversion and
reports a singular matrix as a mathematical result. Each learner-facing edit
names a line or value and asks the learner to explain the resulting output.
[Simplification](https://docs.sympy.org/latest/tutorials/intro-tutorial/simplification.html) · [Calculus](https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html) · [Matrices](https://docs.sympy.org/latest/tutorials/intro-tutorial/matrices.html)

Tab reaches Run from the editor. Keyboard activation moves focus to Stop and
returns focus to Run when execution ends. Restore example keeps the most
recently replaced code for recovery, including after reload or progress
import. Execution errors have a separate message and optional traceback.
Successful text, typeset results, diagrams, plots and exports describe the
last successful execution.

Chromium walkthroughs followed the original and edited examples at phone and
desktop widths, checked reflow in both themes, and exercised draft recovery and
keyboard Run and Stop. After a deliberate capstone error, the typeset result
and JSON stayed identical and the Markdown still contained the exact successful
source and stdout, including source with internal Markdown fences. The
browser suite also verifies the three edits, prior result preservation,
portable progress and the reading path without JavaScript. These are functional
and author checks. Learning effectiveness remains unmeasured.


## Course-wide check of wording, edits and state

The [wording and interface audit](copy-audit.md) records the opening and closing
checks across all 54 routes, their literal editor changes, evidence and
limits. This review applied the learning-design and UX skills again to the
essential route with optional panels closed, each source-to-output comparison
and the state of earlier drafts and results after a rejected write or run.

## Python startup review

Applied the UX and learning-design skills to the existing lesson route. The
learner predicts, edits and selects Run Python as before. Preparation begins
after rendering on eligible visible lessons and only loads Python and pinned
packages. The overview and field notes do not start a Python worker. The
prepared worker joins the first explicit Run and receives the editor source at
that click. Only an actual run can produce a result.

Package transfers can overlap Python bootstrap. Wheel versions, build-time
hash checks and printed evidence are preserved. The worker and its embedded
helpers share the app build ID. The pinned engine has its own versioned path.
Existing per-run variables, figure cleanup and reusable imports remain in
place. Restart Python under the editor tools clears the worker, including
its virtual files, and keeps the edited source. Slow connections, Save Data,
small reported device memory and background tabs defer speculative startup.

The browser suite checks the prepared path with denied storage and no idle
callback, Run during initialization, repeated clicks, fresh user variables,
restart clearing a virtual file, explicit Run with Save Data, cancellation,
worker-load failure and manual recovery. The full course checks still compare
real executions with authored examples and inspect accessible reading and
recovery. This review covers the implementation and learner controls.


## Offline access review

Added only a header App status icon and the offline save/update/recovery flow. Learners choose Save offline copy before disconnecting; readiness follows verification of every promised byte, including optional Python. Opening status or checking versions does not run examples or download the whole course. Existing reading order, prerequisites, experiments, controls, navigation and storage keys remain. Modal feedback names actions and preserves earlier results. Busy work and failed storage prevent restart. See [offline design](offline-update-design.md) and regression test evidence. Learning effectiveness remains unmeasured.

Offline removal regression: a delayed pre-removal verification cannot restore a deleted copy’s ready status. The browser test holds a genuine worker STATUS reply across removal and checks the status after releasing it.

The header offline icon starts disabled and is enabled only after its dialog handlers are installed. A browser fixture delays that module and checks both states, preventing a visible but inactive first click on slow connections.

## Shared header icon controls

UX and learning-design review: compact Material 3 theme/offline actions replace header text controls; 48px targets, action labels, tooltips and focus outlines preserve discoverability and keyboard access. Existing native theme handlers, offline verification, saved work, runner controls and subject-specific links remain authoritative. The saved badge requires a verified current offline copy; an update dot identifies an offered update. Go keeps a status icon because it offers no complete offline copy. No lesson sequence, teaching claims or prerequisites change. Review phone/tablet/desktop, both themes, keyboard, storage denial and the real save/update state transitions. Functional evidence is recorded with the change; it does not establish learning effectiveness.


## Visible header labels (2026-11-26)

UX and learning-design review: retain the Material symbols and add visible
**Offline** and **Theme** labels so touch users can identify the actions without
a tooltip. The Code runner name and state, subject-specific tools, native theme
preferences and verified offline/update badges remain. Controls fit their text,
use at least 48px touch targets, and wrap on narrow screens rather than hiding
labels. No execution, lesson instructions, progress or saved-work contract changes.
The shared [course design guide](https://github.com/snowch/cuda-python-lab/blob/main/docs/course-design-guide.md#theme-and-offline-icons)
records this rule. Validation covers the built header at 320, 390, 820 and 1440px
in both themes, keyboard focus, modal opening/Escape, persistence and project-local
asset requests. Functional checks do not establish learning effectiveness.

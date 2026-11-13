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

Review covered first-lesson tablet/phone screenshots before and after running, plus narrow light/dark concept screenshots for cancellation, curve intersections, gradients, diagonalisation, covariance, box geometry and Monte Carlo. A label-bounds audit found and corrected graph axis headings and an unnecessarily long scientific-notation tick. Diagram labels are checked inside their SVG bounds. The native suite also checks the live area representation against exact symbolic expansion and refuses incompatible domains. Existing Wasm, error/Stop, export, draft, theme, keyboard, no-JavaScript and reflow coverage is retained. Browser evidence is under `test-results/` and is uploaded by the existing Pages workflow.

These illustrations and author/browser checks have not been evaluated in a learner study. Static reference diagrams do not change when a learner edits a model; executed plots and the first lesson’s live area model are explicitly separate.

# Learning design

Audience: people able to read basic Python but with uneven or rusty mathematics. The course teaches symbolic computation through mathematical tasks. It does not assume calculus or linear algebra at the start. Module prerequisites and a route map help returning learners enter later modules.

Outcomes: construct exact expressions; state assumptions and domains; choose a transformation; solve and verify equations; reason about functions, calculus and matrices; derive small models; turn symbolic work into checked numerical functions; export a reproducible investigation.

Structure: eight modules of six short investigations (48), plus four optional integrated workshops. Each lesson targets one observable outcome and includes three short explanatory paragraphs, a prediction, an independent executable Python example, actual output, an executed worked result, a deliberate change, a fresh transfer question, two progressive hints, explanatory feedback and a limitation. Integrated workshops take longer than an ordinary initial pass.

Maths refreshers: every lesson has a closed-by-default, clearly labelled optional panel immediately before the main explanation. Each panel reviews the specific prerequisite using plain language, one typeset equation and a small worked example. It connects the notation to the current task, not a separate general textbook chapter. Learners can open it when needed without interrupting the route for others. Definitions still appear in the essential lesson where the new SymPy concept requires them.

Progression and misconceptions: Python assignment is not mathematical equality; ** means power; exact numbers are different from early rounded floats; matching printed symbol names need not mean matching assumptions; sqrt(x**2) depends on the domain; cancellation can remove a hole from an expression's visible form; simplification is goal-dependent; solver outputs have domains and forms; numerical roots depend on starting points; antiderivatives include a family; a Taylor polynomial has a local error term; eigenvectors have nonunique scale; symbolic identities alone do not validate a real-world model.

Representation: show editable Python, labelled typeset symbolic results and plain text together. The visible `results` dictionary identifies expressions to typeset. Scripts run independently without hidden prior notebook state. LaTeX comes from actual SymPy evaluation; KaTeX renders it locally. All worked records are generated from exact source. Invented modelling inputs are labelled. References point to primary SymPy documentation.

Design review before implementation: retain the large-type reading surface and recoverable worker editor from the existing labs; give this course its own green/ink palette, mathematical visual introduction and clear prerequisite route. Keep the refresher optional, with a readable equation and a worked example. Preserve keyboard controls, local drafts, exact-source exports, stop/reset, mobile contents and Pages-relative assets. Review optional panels closed and open at 320/390px and 200% text size.

Evidence: author review and executable/browser checks are not learner validation. No study with learners has been conducted. Follow-up evaluation should observe a learner with rusty algebra using the first expression, assumptions, cancellation and first derivative lessons, including whether the panel answers the missing prerequisite and whether they can transfer the idea without hints.

## Quiet presentation

Keep the learning structure while reducing simultaneous scaffolding. Present one
plain learning goal followed by explanation, a visible prediction question, the
experiment and a transfer case. Recording the prediction and keeping field notes
are optional disclosures; saved text reopens them on return. Progressive hints,
worked examples and runtime tools stay available beside the relevant activity.
Results appear after execution, with clear provenance and recoverable error/Stop
states. Course modules are native disclosures; search opens matching modules and
module deep links reveal their contents. Mathematical refreshers remain optional,
readable disclosures where the course provides them.

## Mathematical representation and concept visuals

Keep mathematical notation and executable Python distinct. Typeset mathematical
expressions in explanations, questions and feedback; style literal Python with
inline code, including incorrect Python answer options where operator syntax is
being assessed. Never turn a Python XOR distractor into a mathematically correct
superscript. Retain the large reading scale and optional prerequisite refreshers.

Each lesson receives a mathematical illustration that explains its particular
idea: geometry, a graph, an interval, a transformation or a dependency diagram.
Illustrations are generated from explicit mathematical models during the build,
with stated domains, captions and accessible descriptions; they are reference
illustrations, separate from the learner's actual output. Use responsive variants
so figure labels remain readable on phones. The first lesson also visualises an
eligible returned square expression after execution, so changing its constant
changes the geometric interpretation. Preserve the exact result and provenance.

Group code and results into one coherent experiment area. Keep text output and
the published reference available with explicit labels and compact spacing.
Visual hierarchy should come from meaningful representations and restrained
section structure, without restoring duplicate goal panels or navigation bars.

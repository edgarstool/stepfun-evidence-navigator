# StepFun Agent Builder Program submission

## Demo title
Evidence Navigator — an evidence-aware project status agent

## Public demo
https://edgarstool.github.io/stepfun-evidence-navigator/

## Source and verification
https://github.com/edgarstool/stepfun-evidence-navigator

## What it does
Evidence Navigator turns unstructured project notes into:
1. a concise status summary;
2. facts supported by the supplied notes;
3. unknowns that should not be stated as facts;
4. one next action; and
5. a way to verify that action.

This helps prevent a merged pull request, a closed task, and an actually deployed feature from being treated as the same proof.

## StepFun integration
- Model: `step-3.7-flash`
- API channel: Step Plan OpenAI-compatible endpoint
  `https://api.stepfun.ai/step_plan/v1/chat/completions`
- Tested with a real Step Plan call.
- Recorded usage: 87 prompt tokens, 927 completion tokens, 1,014 total.
- The full request outcome and evidence are in [VERIFICATION.md](VERIFICATION.md).

## Suggested X post
Built **Evidence Navigator** with Step 3.7 Flash: an agent that turns project notes into supported facts, unknowns, and one verifiable next step.

Demo: https://edgarstool.github.io/stepfun-evidence-navigator/

Source + real API proof: https://github.com/edgarstool/stepfun-evidence-navigator

@StepFun_ai #BuildWithStepFun

## Form
Submit at https://forms.gle/5UAE1cJgUCrMMchP9

The form requires the StepFun platform UID.
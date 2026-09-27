# Evidence Navigator — StepFun Agent Builder Program demo

Evidence Navigator is a small, working agent that turns project notes into an evidence-aware status summary and one verifiable next action. It uses **Step 3.7 Flash** through StepFun's Step Plan API channel.

## What it does

- Extracts facts that the supplied notes actually support
- Lists important unknowns
- Proposes one next action and a concrete verification method
- Avoids declaring a service live merely because a ticket is closed or code merged

## Run locally

Python 3.10+ and an active Step Plan trial/subscription with a StepFun API key are required.

```powershell
$env:STEPFUN_API_KEY = 'your-key'
python .\server.py
```

Open `http://127.0.0.1:8766`, paste project notes, and select **請 Agent 分析**. The browser never receives the API key.

> The app uses `https://api.stepfun.ai/step_plan/v1/chat/completions`. Step Plan Credits and the separately billed standard API balance are separate.

## Verified live model call

A real `step-3.7-flash` call through the Step Plan channel returned a complete analysis on 2026-09-27. See [VERIFICATION.md](VERIFICATION.md) for the input, output, request ID, and token usage. The key and the model's hidden reasoning are not retained.

## Builder Program submission

- **Project:** Evidence Navigator — an evidence-aware project status agent
- **Description:** Evidence Navigator uses Step 3.7 Flash to review project notes, separate supported claims from unknowns, and propose one verifiable next action. It helps builders avoid claiming a feature is live solely because a task was closed.
- **Demo page:** https://edgarstool.github.io/stepfun-evidence-navigator/
- **X draft:** Built Evidence Navigator with Step 3.7 Flash: an agent that turns project notes into supported facts, unknowns, and one verifiable next step. Demo: https://edgarstool.github.io/stepfun-evidence-navigator/ @StepFun_ai #BuildWithStepFun
- **Builder Program:** https://platform.stepfun.ai/builder-program

## License

MIT.
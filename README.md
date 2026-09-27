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

The public GitHub Pages site is a recorded evidence page, not a hosted API backend. The interactive runner in `index.html` + `server.py` runs locally with the operator's own Step Plan key.

## Red-team evaluation

The original prompt passed 2/3 adversarial cases and failed an unsupported-PASS injection. After hardening note boundaries and adding strict response validation, a fresh live Step 3.7 Flash run passed 3/3 cases. See [REDTEAM.md](REDTEAM.md) and [redteam-results.json](redteam-results.json).

If you expose the Python backend publicly, add your own authentication/rate limiting before allowing untrusted callers to spend API credits.

## Builder Program submission

- **Project:** Evidence Navigator — an evidence-aware project status agent
- **Description:** Evidence Navigator uses Step 3.7 Flash to review project notes, separate supported claims from unknowns, and propose one verifiable next action. It helps builders avoid claiming a feature is live solely because a task was closed.
- **Demo page:** https://edgarstool.github.io/stepfun-evidence-navigator/
- **X draft:** Built Evidence Navigator with Step 3.7 Flash: an agent that turns project notes into supported facts, unknowns, and one verifiable next step. Demo: https://edgarstool.github.io/stepfun-evidence-navigator/ @StepFun_ai #BuildWithStepFun
- **Builder Program:** https://platform.stepfun.ai/builder-program

## License

MIT.
- [OpenAI GPT-3.5 Price Calculator](https://openai.deepakness.com/)- [keyfleet](https://github.com/WhaleFYu/keyfleet)

    A zero-dependency Python library (no service to run) that fails over across several OpenAI-compatible API keys, keeps a per-key daily spend ledger with a hard cap, and classifies failures (401 → quarantine, 429/402 → cooldown, 5xx → deprioritize, local gateway → stop) instead of blindly retrying. `keyfleet check` probes every key concurrently and prints a report you can paste into an issue.


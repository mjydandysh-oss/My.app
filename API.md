# My.app Agent API

This document describes the local agent HTTP API provided by the `myapp_agent` package.

Base URL (default when serve runs locally):
- `http://localhost:9000` (port configurable via CLI)

Authentication
--------------
All endpoints require an API key submitted in the header `X-API-KEY`.
Set `MYAPP_AGENT_KEYS` environment variable on the server (comma-separated list of allowed keys), or pass keys when running the server with `--keys`.

Endpoints
---------

### GET /v1/health
Check the service health.

Response (200):

```json
{ "status": "ok", "version": "0.1.0" }
```

---

### POST /v1/chat
Send a chat prompt to the local assistant.

Request JSON:

```json
{
  "prompt": "Write a unit test for the function X",
  "mode": "assistant"
}
```

Response JSON:

```json
{
  "reply": "[Agent v0.1] I received: ..."
}
```

Notes: The local assistant currently returns a deterministic reply. You can extend the implementation in `myapp_agent.server.chat` to call remote LLM providers (OpenAI, HF) or local models.

---

### POST /v1/execute
Execute a shell command (whitelisted commands only).

Request JSON:

```json
{
  "command": "ls -la",
  "timeout": 20,
  "workdir": "/workspace/My.app"
}
```

Response JSON:

```json
{
  "returncode": 0,
  "stdout": "...",
  "stderr": ""
}
```

Security: Execution is intentionally restricted by a whitelist in `myapp_agent.executor.ALLOWED_COMMANDS`. Commands not on the whitelist return HTTP 403.

---

Examples (curl)
----------------

Set your key (example uses the generated key from the release):

```bash
MYKEY="<your-key-from-releases>"
```

Chat example:

```bash
curl -s -X POST http://localhost:9000/v1/chat \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $MYKEY" \
  -d '{"prompt":"Summarize the repository"}'
```

Execute example:

```bash
curl -s -X POST http://localhost:9000/v1/execute \
  -H "Content-Type: application/json" \
  -H "X-API-KEY: $MYKEY" \
  -d '{"command":"ls -la","timeout":10}'
```

Extending the agent
-------------------
- To integrate an LLM provider, modify `myapp_agent.server.chat` to call your provider and return the model output.
- To add safe sandboxing, consider running commands inside short-lived containers and returning the results.

Logs
----
Agent runtime logs are written to `logs/agent.log` by default.



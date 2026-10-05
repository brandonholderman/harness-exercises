# Harness

Requires Python 3.10+ and a running model API. No extra Python packages.

From this directory:

```powershell
python .\harness.py --project ..\web-project "Read public/index.html and explain it."
```

`--project` selects the directory the tools can access. The starter only has
`read_file`, so include file names in your prompt. Omit the prompt to type it
when the program starts. Each run starts a new conversation.

## Code

`TOOLS` describes the available tool to the model. `execute_tool` parses its
arguments and calls the Python function. `main` sends the result back to the
model and repeats until it gets an answer without tool calls.

The default limit is eight API requests. Change it with `--max-steps`.

## Configuration

The defaults are `qwen3:8b` and `http://localhost:11434/v1`.
Override them with `--model` and `--base-url`, or environment variables:

```powershell
$env:LLM_MODEL = "qwen3:8b"
$env:LLM_BASE_URL = "http://localhost:11434/v1"
```

Local Ollama needs no API key. For a service that requires one, set `LLM_API_KEY`.
The harness appends `/chat/completions` to the base URL.

If the connection fails, check that Ollama is running. Use `ollama list` to check
the model name.

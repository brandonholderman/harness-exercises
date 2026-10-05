# Agent harness exercise

`harness/` runs the assistant. `web-project/` is the project it works on.
Both use Python 3.10+ with no extra packages.

## Setup

Install [Ollama](https://ollama.com/download/windows) and keep it running.
From this directory in PowerShell:

```powershell
ollama pull qwen3:8b
python .\web-project\server.py
```

Open http://127.0.0.1:8000. In another terminal:

```powershell
python .\harness\harness.py --project .\web-project "Read public/index.html and describe the page."
```

The terminal prints each tool call and its result.

## Exercise

Extend the harness so it can answer this request without listing the project
contents in the prompt:

```powershell
python .\harness\harness.py --project .\web-project "List the files and folders in the project root."
```

Only `read_file` is implemented. Add a way for the assistant to list the
project's top-level entries. Choose the tool name and arguments. Keep the
listing inside the directory passed to `--project`; do not recurse into folders.

Check the answer against the project directory. Then ask for the contents of
`public/index.html`; the assistant can now discover the file before reading it.

Later, add file writing as a separate exercise. Writing a new file is a simpler
next step than changing part of an existing file.

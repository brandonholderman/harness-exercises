# Web project

Requires Python 3.10+. From this directory:

```powershell
python .\server.py
```

Open http://127.0.0.1:8000. Stop with Ctrl+C. Use `--port 8001` if the port is busy.

The server serves files from `public/`. Refresh after editing HTML or JavaScript.
Restart the server after editing `server.py`.

To invoke the harness from this directory, including a VS Code terminal:

```powershell
python ..\harness\harness.py --project . "Read public/index.html and explain it."
```

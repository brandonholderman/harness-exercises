"""Serve public/ on localhost."""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    # Use this file's location rather than the terminal's current directory.
    public = Path(__file__).resolve().parent / "public"
    handler = partial(SimpleHTTPRequestHandler, directory=str(public))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Open http://127.0.0.1:{server.server_port} (Ctrl+C to stop)", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    main()

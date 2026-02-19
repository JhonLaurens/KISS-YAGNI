import http.server, socketserver, webbrowser, os, sys

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(ROOT, "src", "web")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

if __name__ == "__main__":
    if not os.path.exists(WEB_DIR):
        print(f"ERROR: No existe {WEB_DIR}")
        sys.exit(1)
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}/src/web/index.html"
            print(f"Servidor activo: {url}")
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError:
        print(f"Puerto {PORT} ocupado.")
    except KeyboardInterrupt:
        print("Detenido.")

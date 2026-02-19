import http.server, socketserver, webbrowser, os, sys, subprocess

HOST = "127.0.0.1"
PORT = 8000
PORT_RANGE = range(8000, 8101)
ROOT = os.path.dirname(os.path.abspath(__file__))
WEB_DIR = os.path.join(ROOT, "web-presentacion-kiss-yagni", "src")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)


def _start_server(port):
    try:
        with http.server.ThreadingHTTPServer((HOST, port), Handler) as httpd:
            httpd.daemon_threads = True
            url = (
                f"http://{HOST}:{port}/web-presentacion-kiss-yagni/src/index.html"
            )
            print("Servidor listo. Abriendo navegador...", flush=True)
            print(f"Servidor activo: {url}", flush=True)
            webbrowser.open(url)
            httpd.serve_forever()
        return True
    except OSError as exc:
        print(f"Error al iniciar servidor en {HOST}:{port}: {exc}")
        return False
    except KeyboardInterrupt:
        print("Detenido.")
        return True


def _free_port(port):
    if os.name != "nt":
        return False

    try:
        result = subprocess.check_output(
            ["netstat", "-ano"], text=True, stderr=subprocess.STDOUT
        )
        pids = set()
        for line in result.splitlines():
            if f":{port} " in line and "LISTENING" in line:
                parts = line.split()
                pid = parts[-1]
                if pid.isdigit():
                    pids.add(pid)

        if not pids:
            return False

        for pid in pids:
            subprocess.check_call(
                ["taskkill", "/F", "/PID", pid],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        return True
    except Exception:
        return False


def main():
    if not os.path.exists(WEB_DIR):
        print(f"ERROR: No existe {WEB_DIR}")
        return 1

    socketserver.TCPServer.allow_reuse_address = True
    if _start_server(PORT):
        return 0

    print(f"Puerto {PORT} ocupado o bloqueado. Intentando cerrar procesos...")
    if _free_port(PORT) and _start_server(PORT):
        return 0

    print("Buscando un puerto disponible...")
    for port in PORT_RANGE:
        if port == PORT:
            continue
        if _start_server(port):
            return 0

    print("No se pudo iniciar el servidor en el rango 8000-8100.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())

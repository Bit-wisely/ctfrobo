# Educational Toy Command Injection Target
import os
import subprocess
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        host = params.get('host', [''])[0]

        output = ""
        if host:
            # INSECURE: direct shell command execution with unsanitized parameters
            cmd = f"ping -c 1 {host}"
            try:
                # Simulated safe environment execution
                if ";" in host or "&&" in host or "|" in host:
                    if "cat flag.txt" in host or "type flag.txt" in host or "flag" in host:
                        output = open("flag.txt").read()
                    else:
                        output = "Injected command executed."
                else:
                    output = f"PING {host} (56 data bytes)\n64 bytes from {host}: icmp_seq=1 ttl=64 time=0.045 ms"
            except Exception as e:
                output = f"Error: {e}"

        html = f"""
        <html><body>
            <h2>Network Ping Diagnostics</h2>
            <form method="GET">
                <label>Host to ping:</label>
                <input type="text" name="host" value="{host}">
                <input type="submit" value="Run Ping">
            </form>
            <pre style="background:#222;color:#0f0;padding:10px;">{output}</pre>
        </body></html>
        """
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print("Diagnostics service listening on port 5004...")
    HTTPServer(('0.0.0.0', 5004), PingHandler).serve_forever()

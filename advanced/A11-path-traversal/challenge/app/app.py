import os
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

class FileServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/download':
            filename = params.get('file', [''])[0]
            # VULNERABLE: Direct path joining without canonical path validation or safe basename
            target_path = os.path.normpath(os.path.join("public", filename))

            try:
                with open(target_path, "rb") as f:
                    content = f.read()
                self.send_response(200)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(content)
            except Exception as e:
                self.send_response(404)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(f"File Not Found: {e}".encode('utf-8'))
        else:
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(b"""
            <html><body>
                <h2>Public Document Viewer</h2>
                <a href="/download?file=sample.txt">Download sample.txt</a>
            </body></html>
            """)

if __name__ == '__main__':
    print("File server running on port 5005...")
    HTTPServer(('0.0.0.0', 5005), FileServerHandler).serve_forever()

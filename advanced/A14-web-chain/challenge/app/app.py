import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

class WebChainHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open("templates/index.html") as f:
                self.wfile.write(f.read().encode('utf-8'))
        elif self.path == '/secret_api_gateway_v1/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('X-Debug-Key', 'debug_admin_984')
            self.end_headers()
            self.wfile.write(json.dumps({
                "message": "Gateway ready. Send POST requests to /api/execute with action=get_flag"
            }).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/api/execute':
            debug_key = self.headers.get('X-Debug-Key', '')
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length).decode('utf-8')
            
            if debug_key == 'debug_admin_984':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "flag": "full web exploit chain"
                }).encode('utf-8'))
            else:
                self.send_response(403)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "Invalid or missing X-Debug-Key header"
                }).encode('utf-8'))

if __name__ == '__main__':
    print("Web chain service active on port 5008...")
    HTTPServer(('0.0.0.0', 5008), WebChainHandler).serve_forever()

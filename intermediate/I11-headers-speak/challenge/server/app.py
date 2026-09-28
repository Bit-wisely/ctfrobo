from http.server import HTTPServer, BaseHTTPRequestHandler

class HeaderHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.send_header('Server', 'Apache/2.4.41 (Ubuntu)')
        self.send_header('X-CTF-Message', 'headers contain secrets')
        self.send_header('X-Powered-By', 'PHP/7.4.3')
        self.end_headers()
        self.wfile.write(b"Hello! Look closely at the response metadata.\n")

if __name__ == '__main__':
    print("Serving on port 8080...")
    HTTPServer(('0.0.0.0', 8080), HeaderHandler).serve_forever()

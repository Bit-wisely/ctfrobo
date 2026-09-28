from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

PORT = 5000

class CookieHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie_header = self.headers.get('Cookie', '')
        cookies = {}
        if cookie_header:
            for item in cookie_header.split(';'):
                if '=' in item:
                    k, v = item.strip().split('=', 1)
                    cookies[k] = v

        role = cookies.get('role', 'user')

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        if 'role' not in cookies:
            self.send_header('Set-Cookie', 'role=user; Path=/')
        self.end_headers()

        if role == 'admin':
            body = f"""
            <html><body>
                <h1>Welcome, Administrator!</h1>
                <p>Secret Flag: <b>flag{{cookie admin access}}</b></p>
            </body></html>
            """
        else:
            body = f"""
            <html><body>
                <h1>Welcome, Standard User!</h1>
                <p>Your current role is: <b>{role}</b></p>
                <p>Access Denied: Administrator role required for flags.</p>
            </body></html>
            """
        self.wfile.write(body.encode('utf-8'))

if __name__ == '__main__':
    print(f"Starting server on port {PORT}...")
    server = HTTPServer(('0.0.0.0', PORT), CookieHandler)
    server.serve_forever()

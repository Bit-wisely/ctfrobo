import base64
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

class ForgeryAppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie_header = self.headers.get('Cookie', '')
        session_data = None

        if 'session=' in cookie_header:
            try:
                raw_cookie = [c.strip() for c in cookie_header.split(';') if c.strip().startswith('session=')][0]
                token = raw_cookie.split('=', 1)[1]
                decoded_json = base64.b64decode(token).decode('utf-8')
                session_data = json.loads(decoded_json)
            except Exception:
                session_data = None

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        if not session_data:
            default_session = base64.b64encode(b'{"user": "guest", "role": "user"}').decode('utf-8')
            self.send_header('Set-Cookie', f'session={default_session}; Path=/')
            session_data = {"user": "guest", "role": "user"}
        self.end_headers()

        if session_data.get('role') == 'admin':
            html = f"""
            <html><body>
                <h1>Admin Control Panel</h1>
                <p>Welcome, Administrator!</p>
                <p>Secret Flag: <b>tampered session token</b></p>
            </body></html>
            """
        else:
            html = f"""
            <html><body>
                <h1>Guest Dashboard</h1>
                <p>Current user: {session_data.get('user', 'unknown')} (Role: {session_data.get('role', 'user')})</p>
                <p>Administrative privileges are required to view the flag.</p>
            </body></html>
            """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print("Session Server listening on port 5001...")
    HTTPServer(('0.0.0.0', 5001), ForgeryAppHandler).serve_forever()

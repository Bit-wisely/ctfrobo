import base64
import json
import hmac
import hashlib
from http.server import HTTPServer, BaseHTTPRequestHandler

SECRET_KEY = b"super_secret_jwt_key_2026"

def b64url_encode(data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    return base64.urlsafe_b64encode(data).decode('utf-8').rstrip('=')

def b64url_decode(data):
    rem = len(data) % 4
    if rem > 0:
        data += '=' * (4 - rem)
    return base64.urlsafe_b64decode(data.encode('utf-8'))

class JWTHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        auth_header = self.headers.get('Authorization', '')
        user_role = 'guest'

        if auth_header.startswith('Bearer '):
            token = auth_header[7:].strip()
            parts = token.split('.')
            if len(parts) >= 2:
                try:
                    header = json.loads(b64url_decode(parts[0]))
                    payload = json.loads(b64url_decode(parts[1]))

                    # VULNERABLE: Accepting alg="none" without signature verification
                    if header.get('alg', '').lower() == 'none':
                        user_role = payload.get('role', 'guest')
                    elif header.get('alg') == 'HS256' and len(parts) == 3:
                        sig = b64url_decode(parts[2])
                        expected_sig = hmac.new(SECRET_KEY, f"{parts[0]}.{parts[1]}".encode('utf-8'), hashlib.sha256).digest()
                        if hmac.compare_digest(sig, expected_sig):
                            user_role = payload.get('role', 'guest')
                except Exception:
                    user_role = 'invalid'

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        if user_role == 'admin':
            html = f"""
            <html><body>
                <h1>JWT Admin Console</h1>
                <p>Welcome, Admin!</p>
                <p>Secret Flag: <b>flag{{jwt_token_forged}}</b></p>
            </body></html>
            """
        else:
            sample_header = b64url_encode(json.dumps({"alg": "HS256", "typ": "JWT"}))
            sample_payload = b64url_encode(json.dumps({"user": "guest", "role": "user"}))
            sample_sig = b64url_encode(hmac.new(SECRET_KEY, f"{sample_header}.{sample_payload}".encode('utf-8'), hashlib.sha256).digest())
            guest_token = f"{sample_header}.{sample_payload}.{sample_sig}"
            html = f"""
            <html><body>
                <h1>JWT Portal</h1>
                <p>Role: {user_role}</p>
                <p>Your guest token: <code>{guest_token}</code></p>
            </body></html>
            """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print("JWT challenge running on port 5006...")
    HTTPServer(('0.0.0.0', 5006), JWTHandler).serve_forever()

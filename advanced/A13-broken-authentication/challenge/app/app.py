import hashlib
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

SALT = "_secret_recovery_salt_2026"

def get_reset_token(username):
    return hashlib.md5(f"{username}{SALT}".encode('utf-8')).hexdigest()

class AuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/reset':
            token = params.get('token', [''])[0]
            admin_expected = get_reset_token('admin')

            if token == admin_expected:
                html = f"""
                <html><body>
                    <h2>Password Reset Successful for Administrator!</h2>
                    <p>Administrative Flag: <b>predictable reset token</b></p>
                </body></html>
                """
            else:
                html = f"""
                <html><body>
                    <h2>Invalid or Expired Reset Token</h2>
                    <p>Provided token: {token}</p>
                </body></html>
                """
        else:
            sample_token = get_reset_token('guest')
            html = f"""
            <html><body>
                <h2>Account Recovery Portal</h2>
                <p>Example: Guest recovery link is: <code>/reset?token={sample_token}</code></p>
                <p>Tokens are calculated as MD5(username + "_secret_recovery_salt_2026")</p>
            </body></html>
            """

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print("Authentication challenge server running on port 5007...")
    HTTPServer(('0.0.0.0', 5007), AuthHandler).serve_forever()

import sqlite3
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

def init_db():
    conn = sqlite3.connect(":memory:")
    with open("database.sql") as f:
        conn.executescript(f.read())
    return conn

db_conn = init_db()

class SQLiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open("templates/login.html") as f:
            self.wfile.write(f.read().encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')
        params = urllib.parse.parse_qs(post_data)

        username = params.get('username', [''])[0]
        password = params.get('password', [''])[0]

        query = f"SELECT username, secret_flag FROM users WHERE username = '{username}' AND password = '{password}'"

        cur = db_conn.cursor()
        try:
            cur.execute(query)
            row = cur.fetchone()
        except Exception as e:
            row = None
            error_msg = str(e)
        else:
            error_msg = None

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

        if row:
            html = f"""
            <html><body>
                <h2>Authentication Successful!</h2>
                <p>Welcome, <b>{row[0]}</b>.</p>
                <p>Secret Flag: <b>{row[1]}</b></p>
            </body></html>
            """
        else:
            html = f"""
            <html><body>
                <h2>Login Failed</h2>
                <p>Invalid credentials.</p>
                {"<p style='color:red'>Database Error: " + error_msg + "</p>" if error_msg else ""}
                <a href='/'>Try again</a>
            </body></html>
            """
        self.wfile.write(html.encode('utf-8'))

if __name__ == '__main__':
    print("SQLi Challenge running on port 5002...")
    HTTPServer(('0.0.0.0', 5002), SQLiHandler).serve_forever()

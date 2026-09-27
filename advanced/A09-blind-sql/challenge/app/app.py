import sqlite3
import json
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

def init_db():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    with open("database.sql") as f:
        conn.executescript(f.read())
    return conn

db_conn = init_db()

class BlindSQLHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)
        username = params.get('username', [''])[0]

        exists = False
        if username:
            query = f"SELECT id FROM users WHERE username = '{username}'"
            try:
                cur = db_conn.cursor()
                cur.execute(query)
                row = cur.fetchone()
                if row:
                    exists = True
            except Exception:
                exists = False

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"exists": exists}).encode('utf-8'))

if __name__ == '__main__':
    print("Blind SQLi challenge running on port 5003...")
    HTTPServer(('0.0.0.0', 5003), BlindSQLHandler).serve_forever()

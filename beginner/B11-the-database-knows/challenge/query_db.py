import sqlite3

def run_query():
    # In-memory SQLite database initialized with the challenge SQL
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    
    with open("database.sql", "r") as f:
        cur.executescript(f.read())
        
    print("Database loaded successfully!")
    print("Executing query for administrator records...")
    
    cur.execute("""
        SELECT users.username, classified_vault.secret_note 
        FROM users 
        JOIN classified_vault ON users.id = classified_vault.user_id 
        WHERE users.role = 'administrator';
    """)
    
    for row in cur.fetchall():
        print(f"User: {row[0]} | Note: {row[1]}")

if __name__ == "__main__":
    run_query()

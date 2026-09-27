import sqlite3

def solve():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()
    
    with open("database.sql") as f:
        cur.executescript(f.read())

    query = """
    SELECT d.name, e.name, e.role, s.secret_value
    FROM departments d
    JOIN employees e ON d.dept_id = e.dept_id
    JOIN secure_vault s ON e.emp_id = s.emp_id
    WHERE d.name = 'Cyber Security' AND e.role = 'Department Head';
    """
    cur.execute(query)
    row = cur.fetchone()
    if row:
        print(f"Department: {row[0]}")
        print(f"Employee: {row[1]} ({row[2]})")
        print(f"Secret: {row[3]}")

if __name__ == "__main__":
    solve()

# Bug reports for exercise4.py

Line: 4
Problem: The admin password is written in the code, so everyone who reads the code knows it. It must be read from the environment.
Example: the password "admin123" is visible in the source code, expected: it is read from the environment (os.environ).
Fix: ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "")

Line: 14
Problem: The function uses string formatting with user input directly in a SQL query, which is vulnerable to SQL injection attacks.
Example: find_user(db, "admin' OR '1'='1") returns all users, expected no user.
Fix: return db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

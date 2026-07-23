import sqlite3

db = sqlite3.connect("data.db")
cursor = db.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    full_name TEXT
)
""")

db.commit()

def add_user(user_id, full_name):
    cursor.execute(
        "INSERT OR IGNORE INTO users (user_id, full_name) VALUES (?, ?)",
        (user_id, full_name)
    )
    db.commit()

def get_users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]

def get_all_users():
    cursor.execute("SELECT user_id FROM users")
    return cursor.fetchall()
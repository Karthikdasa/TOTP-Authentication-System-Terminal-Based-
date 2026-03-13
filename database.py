import sqlite3

DB_NAME = "users.db"


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE,
        password TEXT,
        totp_secret TEXT
    )
    """)

    conn.commit()
    conn.close()


def add_user(email, password, secret):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users(email,password,totp_secret) VALUES(?,?,?)",
        (email, password, secret)
    )

    conn.commit()
    conn.close()


def get_user(email):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE email=?", (email,))
    user = cursor.fetchone()

    conn.close()

    return user
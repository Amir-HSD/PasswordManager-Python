import sqlite3

def connect():
    conn = sqlite3.connect('users.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS "users" (
        "id"	INTEGER,
        "title"	TEXT,
        "username"	TEXT,
        "password"	TEXT,
        "note"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    )
    ''')
    conn.commit()

def insert_user(conn, title, username, password, note):
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO users (title, username, password, note) VALUES (?, ?, ?, ?)
    ''', (title, username, password, note))
    conn.commit()

def update_user(conn, id, title, username, password, note):
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE users SET title = ?, username = ?, password = ?, note = ? WHERE id = ? 
    ''' , (title, username, password, note, id))
    conn.commit()

def delete_user(conn, id):
    cursor = conn.cursor()
    cursor.execute('''
    delete from users where id = ?
    ''',(id,))
    conn.commit()

def get_all_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

def get_user(conn, id):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?',(id,))
    return cursor.fetchone()

def close_connection(conn):
    conn.close()

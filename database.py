import sqlite3


def connect_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    conn = sqlite3.connect('password.db')
    cursor = conn.cursor()
    return conn, cursor


def disconnect_db(conn) -> None:
    conn.commit()
    conn.close()


def create_database() -> None:
    conn, cursor = connect_db()

    cursor.execute('''
        CREATE TABLE "users" (
        "id" INTEGER NOT NULL PRIMARY KEY,
        "username" TEXT NOT NULL,
        "master_password" BLOB NOT NULL,
        "key" BLOB NOT NULL
        );
    ''')

    cursor.execute('''
        CREATE TABLE "services" (
        "service_name" TEXT NOT NULL,
        "username" TEXT NOT NULL,
        "password" BLOB NOT NULL,
        "user_id" INTEGER NOT NULL,
        CONSTRAINT foreignkey_users
        FOREIGN KEY ("user_id")
        REFERENCES users(id)
        );
    ''')

    disconnect_db(conn)


def add_user(username, hashed_master, key) -> None:
    conn, cursor = connect_db()
    cursor.execute(f'''
        INSERT INTO users ("username", "master_password", "key")
        VALUES ("{username}", "{hashed_master}", "{key}")
    ''')

    disconnect_db(conn)


def get_password(username) -> str:
    conn, cursor = connect_db()
    cursor.execute(f'''
        SELECT master_password FROM users WHERE username = "{username}"
    ''')

    password = cursor.fetchone()
    disconnect_db(conn)
    return password


def get_userid(username) -> int:
    conn, cursor = connect_db()
    cursor.execute(f'''
        SELECT id FROM USERS WHERE username= "{username}"
    ''')

    user_id = cursor.fetchone()
    disconnect_db(conn)
    return user_id


def delete_user(user_id) -> None:
    conn, cursor = connect_db()

    cursor.execute(f'''
        DELETE FROM users WHERE id = {user_id}
    ''')

    cursor.execute(f'''
        DELETE FROM services WHERE user_id = {user_id}
    ''')

    disconnect_db(conn)


def get_users() -> list:
    conn, cursor = connect_db()

    cursor.execute(f'''
        SELECT username FROM users
    ''')

    users = cursor.fetchall()
    disconnect_db(conn)
    return users







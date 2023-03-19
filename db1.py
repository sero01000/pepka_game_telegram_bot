from sqlite3 import connect
db_path="db1.db"

def add_user_to_game(chat_id,user_id,user_name,dick_len,last_time_play):
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO '{chat_id}' VALUES ({user_id}, '{user_name}', {dick_len}, {last_time_play})")
    conn.commit()
    conn.close()
def get_row(chat_id,user_id):
    conn = connect(db_path)
    cursor = conn.cursor()
    row=cursor.execute(f"SELECT * FROM '{chat_id}' WHERE user_id = {user_id}").fetchall()
    conn.close()
    return row
def update_by_user(chat_id,user_id,dick_len,last_time_play):
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE '{chat_id}' SET dick_len = {dick_len},last_time_play={last_time_play} WHERE user_id = {user_id}")
    conn.commit()
    conn.close()
def check_table(chat_id):
    conn = connect(db_path)
    cursor = conn.cursor()
    table=cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{chat_id}'").fetchall()
    conn.close()
    return table
def create_table(chat_id):
    conn = connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE '{chat_id}' ('user_id'   INTEGER NOT NULL UNIQUE,'user_name' TEXT NOT NULL,'dick_len'  INTEGER,'last_time_play'   INTEGER NOT NULL)")
    conn.commit()
    conn.close()
def get_table(chat_id):
    conn = connect(db_path)
    cursor = conn.cursor()
    rows = cursor.execute(f"SELECT * FROM '{chat_id}'").fetchall()
    conn.close()
    return rows
def get_leaders_by(chat_id):
    conn = connect(db_path)
    cursor = conn.cursor()
    leaders=cursor.execute(f"SELECT * from '{chat_id}' ORDER BY dick_len DESC").fetchall()
    conn.close()
    return leaders
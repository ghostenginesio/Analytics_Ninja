import sqlite3

conn = sqlite3.connect("ig_data.sqlite")

cursor = conn.cursor()

sql_query = """ CREATE TABLE app_user(
    id integer PRIMARY KEY,
    client_id text,
    client_secret text,
    code text,
    access_token text,
    user_id text,
    instagram_account_id text
)

"""

cursor.execute(sql_query)

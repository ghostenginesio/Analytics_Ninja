import sqlite3

conn = sqlite3.connect("ig_data.sqlite")

cursor = conn.cursor()

sql_query = """ CREATE TABLE app_user(
    id integer PRIMARY KEY,
    client_id text NOT NULL,
    client_secret text NOT NULL,
    code text,
    access_token text,
    user_id text,
    instagram_account_id text NOT NULL UNIQUE
)

"""

cursor.execute(sql_query)

import sqlite3


def create_db(cur):
    cur.execute('''
        CREATE TABLE game (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  -- 반드시 있어야 함
            game_name TEXT NOT NULL,
            original_price REAL NOT NULL,
            discount_price REAL NOT NULL,
            discount_startdate TEXT,
            discount_enddate TEXT,
            genre TEXT,
            release_date TEXT,
            maker TEXT,
            player_number TEXT,
            product_type TEXT,
            game_language TEXT,
            game_image_url TEXT,
            game_url TEXT,
            collect_date TEXT,
            UNIQUE(game_name, product_type)
        )
    ''')


conn = sqlite3.connect("mainDB.db")
cur = conn.cursor()

create_db(cur)

conn.commit()
conn.close()
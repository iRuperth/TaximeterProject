import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "data", "journey_database.db")
DB_TIMEOUT = 10

def init_db():
    timeout_ms = DB_TIMEOUT * 1000
    conn = sqlite3.connect(DATABASE, timeout=DB_TIMEOUT)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA busy_timeout = {timeout_ms}') 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS journeys (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            passenger_name TEXT NOT NULL,
            total_duration REAL NOT NULL,
            total_price REAL NOT NULL,
            start_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    
def log_journey(user_id, passenger_name, total_duration, total_price):
    timeout_ms = DB_TIMEOUT * 1000
    conn = sqlite3.connect(DATABASE, timeout=DB_TIMEOUT)
    cursor = conn.cursor()
    cursor.execute(f'PRAGMA busy_timeout = {timeout_ms}')
    duration_rounded = round(total_duration, 2)
    price_rounded = round(total_price, 2)
    cursor.execute('''
        INSERT INTO journeys (user_id, passenger_name, total_duration, total_price)
        VALUES (?, ?, ?, ?)
    ''', (user_id, passenger_name, duration_rounded, price_rounded))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database '{DATABASE}' initialized successfully.")

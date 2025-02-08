import sqlite3

def create_database():
    conn = sqlite3.connect('fitness.db')
    cursor = conn.cursor()

    # Create Users table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Create Exercises table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS exercises (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        category TEXT
    )
    ''')

    # Create Workout_logs table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS workout_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        exercise_id INTEGER,
        sets INTEGER,
        reps INTEGER,
        weight FLOAT,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users (id),
        FOREIGN KEY (exercise_id) REFERENCES exercises (id)
    )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database() 
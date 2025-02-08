import sqlite3
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_name='fitness.db'):
        self.db_name = db_name

    def get_connection(self):
        return sqlite3.connect(self.db_name)

    def get_exercise_id(self, exercise_name):
        """Get or create exercise ID from name"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Try to find existing exercise
            cursor.execute("SELECT id FROM exercises WHERE name = ?", (exercise_name,))
            result = cursor.fetchone()
            
            if result:
                return result[0]
            
            # If not found, create new exercise
            cursor.execute(
                "INSERT INTO exercises (name) VALUES (?)",
                (exercise_name,)
            )
            conn.commit()
            return cursor.lastrowid
            
        finally:
            conn.close()

    def save_workout(self, user_id, exercise_name, sets, reps, weight, notes=None):
        """Save a workout to the database"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            # Get or create exercise ID
            exercise_id = self.get_exercise_id(exercise_name)
            
            # Insert workout log
            cursor.execute("""
                INSERT INTO workout_logs 
                (user_id, exercise_id, sets, reps, weight, notes) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user_id, exercise_id, sets, reps, weight, notes))
            
            conn.commit()
            return cursor.lastrowid
            
        finally:
            conn.close()

    def get_recent_workouts(self, user_id, limit=10):
        """Get recent workouts for a user"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        try:
            cursor.execute("""
                SELECT w.date, e.name, w.sets, w.reps, w.weight, w.notes
                FROM workout_logs w
                JOIN exercises e ON w.exercise_id = e.id
                WHERE w.user_id = ?
                ORDER BY w.date DESC
                LIMIT ?
            """, (user_id, limit))
            
            return cursor.fetchall()
            
        finally:
            conn.close() 
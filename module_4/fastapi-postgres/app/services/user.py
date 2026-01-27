from psycopg2.extensions import connection
from app.schemas.user import UserCreate
from typing import List, Optional

class UserService:    
    @staticmethod
    def create_user(db: connection, user: UserCreate) -> dict:
        cursor = db.cursor()
        print(user)
        try:
            cursor.execute(
                """
                INSERT INTO users (email, username, full_name)
                VALUES (%s, %s, %s)
                RETURNING id, email, username, full_name, is_active, created_at
                """,
                (user.email, user.username, user.full_name)
            )
            new_user = cursor.fetchone()
            return new_user
        finally:
            cursor.close()
    
    @staticmethod
    def get_all_users(db: connection) -> List[dict]:
        cursor = db.cursor()
        try:
            cursor.execute(
                "SELECT id, email, username, full_name, is_active, created_at FROM users"
            )
            users = cursor.fetchall()
            return users
        finally:
            cursor.close()

    
    @staticmethod
    def get_user_by_id(db: connection, user_id: int) -> Optional[dict]:
        cursor = db.cursor()
        try:
            cursor.execute(
                """
                SELECT id, email, username, full_name, is_active, created_at 
                FROM users WHERE id = %s
                """,
                (user_id,)
            )
            user = cursor.fetchone()
            return user
        finally:
            cursor.close()


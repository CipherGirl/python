from psycopg2.extensions import connection
from app.schemas.user import UserCreate, UserUpdate
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

    @staticmethod
    def update_user(
        db: connection, 
        user_id: int, 
        user_update: UserUpdate
    ) -> Optional[dict]:
        
        cursor = db.cursor()
        try:
            update_fields = []
            values = []
            
            if user_update.email is not None:
                update_fields.append("email = %s")
                values.append(user_update.email)
            if user_update.username is not None:
                update_fields.append("username = %s")
                values.append(user_update.username)
            if user_update.full_name is not None:
                update_fields.append("full_name = %s")
                values.append(user_update.full_name)
            if user_update.is_active is not None:
                update_fields.append("is_active = %s")
                values.append(user_update.is_active)
            
            if not update_fields:
                raise ValueError("No fields to update")
            
            values.append(user_id)
            query = f"""
                UPDATE users 
                SET {', '.join(update_fields)}
                WHERE id = %s
                RETURNING id, email, username, full_name, is_active, created_at
            """
            
            cursor.execute(query, values)
            updated_user = cursor.fetchone()
            return updated_user
        finally:
            cursor.close()
    
    @staticmethod
    def delete_user(db: connection, user_id: int) -> bool:
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM users WHERE id = %s RETURNING id", (user_id,))
            deleted = cursor.fetchone()
            return deleted is not None
        finally:
            cursor.close()
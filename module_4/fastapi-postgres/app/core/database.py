import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from typing import Generator
from app.core.config import settings

def get_db_connection():
    conn = psycopg2.connect(settings.database_url, cursor_factory=RealDictCursor)
    return conn

@contextmanager
def db_ctx():
    conn = get_db_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def db_generator() -> Generator:
    conn = psycopg2.connect(settings.database_url, cursor_factory=RealDictCursor)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    with db_ctx() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                username VARCHAR(100) NOT NULL,
                full_name VARCHAR(255),
                is_active BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        cursor.close()



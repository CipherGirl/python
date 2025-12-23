import logging
import sqlite3
from contextlib import contextmanager

conn = sqlite3.connect('application.db')

c = conn.cursor()

# # ========= CREATING TABLE =========
# c.execute("""
#     CREATE TABLE IF NOT EXISTS blogs (
#         title TEXT,
#         author TEXT,
#         views INTEGER
#     )
# """)

# # ========= INSERT FUNCTION =========
# # "with conn" ensures commit or rollback automatically
# def insert_blog(title: str, author: str, views: int) -> None:
#     with conn:
#         c.execute(
#             "INSERT INTO blogs (title, author, views) VALUES (?, ?, ?)",
#             (title, author, views),
#         )

# # Usage
# insert_blog("Hello Python", "Hena", 500)


# Exmample with try catch
def try_catch_manual_cm():
    logging.basicConfig(level=logging.INFO)
    connection = sqlite3.connect("application.db")
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())
    finally:
        connection.close()

# Example with with and cm object from sqlite3.connect as conn
def with_sqlite_cm():
    with sqlite3.connect("application.db") as conn:
        conn.execute("CREATE TABLE test (id INTEGER)")
        conn.execute("INSERT INTO test VALUES (1)")

# Example for custom class based context manager
class SQLite:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def __enter__(self):
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, error: Exception, value: object, traceback: object):
        logging.info("Calling __exit__")
        self.connection.commit()
        self.connection.close()


def with_custom_class_cm():
    logging.basicConfig(level=logging.INFO)
    with SQLite(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


# Example of decorator based custom context manager from contextlib contextmanager
@contextmanager
def open_db(file_name: str):
    conn = sqlite3.connect(file_name)
    try:
        logging.info("Creating connection")
        yield conn.cursor()
    finally:
        logging.info("Closing connection")
        conn.commit()
        conn.close()


def with_custom_decorator_cm():
    logging.basicConfig(level=logging.INFO)
    with open_db(file_name="application.db") as cursor:
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


with_custom_class_cm()
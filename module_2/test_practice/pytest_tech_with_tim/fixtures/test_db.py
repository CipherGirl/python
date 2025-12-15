import pytest
from db import DataBase

"""SETUP and TEARDOWN EXAMPLE USING FIXTURES IN PYTEST"""
@pytest.fixture
def db():
    """Set up a fresh database before each test and tear it down after."""
    # SETUP - Prepare the database before each test
    database = DataBase()
    yield database
    # TEAR DOWN - Clean up after each test
    database.data.clear()

def test_insert_user(db):
    db.add_user(1, "alice")
    assert db.get_user(1) == "alice"

def test_insert_existing_user(db):
    db.add_user(1, "alice")
    with pytest.raises(ValueError, match="User ID already exists."):
        db.add_user(1, "bob")

def test_delete_user(db):
    db.add_user(2, "bob")
    db.delete_user(2)
    assert db.get_user(2) is None


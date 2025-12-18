"""
conftest.py
===========

This file is automatically discovered by pytest and is used to define
shared test fixtures, hooks, and configuration for tests in this
directory and all subdirectories.

Key points:
- Fixtures defined here do NOT need to be imported in test files.
- pytest injects fixtures by name.
- This file should contain test utilities, not application logic.
"""

import pytest
import tempfile
import os


# -------------------------------------------------------------------
# BASIC FIXTURE
# -------------------------------------------------------------------
@pytest.fixture
def sample_numbers():
    """
    Provides a reusable list of numbers for tests.

    Scope: function (default)
    This fixture runs once per test that uses it.
    """
    return [1, 2, 3, 4, 5]


# -------------------------------------------------------------------
# FIXTURE WITH SETUP + TEARDOWN (yield style)
# -------------------------------------------------------------------
@pytest.fixture
def temp_file():
    """
    Creates a temporary file for testing file I/O.

    Setup:
    - Creates a temp file
    - Writes known content

    Yield:
    - Provides the file path to the test

    Teardown:
    - Deletes the file after the test finishes
    """
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(b"Hello, pytest!")
    temp.close()

    yield temp.name

    os.unlink(temp.name)


# -------------------------------------------------------------------
# PARAMETRIZED FIXTURE
# -------------------------------------------------------------------
@pytest.fixture(params=[1, 2, 3])
def number(request):
    """
    Parametrized fixture.

    Any test using this fixture will run multiple times,
    once for each parameter value.
    """
    return request.param


# -------------------------------------------------------------------
# AUTOUSE FIXTURE (runs automatically)
# -------------------------------------------------------------------
@pytest.fixture(autouse=True)
def set_test_env(monkeypatch):
    """
    Automatically sets environment variables for all tests.

    This fixture runs for every test without being explicitly requested.
    """
    monkeypatch.setenv("ENV", "test")


# -------------------------------------------------------------------
# SESSION-SCOPED FIXTURE
# -------------------------------------------------------------------
@pytest.fixture(scope="session")
def session_resource():
    """
    Runs once per pytest session.

    Useful for:
    - Database connections
    - Expensive setup
    - External services
    """
    print("\n[setup] session resource")
    yield "SESSION_RESOURCE"
    print("\n[teardown] session resource")


# -------------------------------------------------------------------
# CUSTOM PYTEST HOOK
# -------------------------------------------------------------------
def pytest_configure(config):
    """
    Pytest hook that runs once at startup.

    Used to:
    - Register custom markers
    - Configure global test behavior
    """
    config.addinivalue_line(
        "markers",
        "slow: marks tests as slow-running"
    )

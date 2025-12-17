import pytest
import tempfile
import os

@pytest.fixture
def temp_file():
    temp = tempfile.NamedTemporaryFile(delete=False)
    temp.write(b"hello")
    temp.close()

    yield temp.name

    os.unlink(temp.name)


def test_file_content(temp_file):
    with open(temp_file, "r") as f:
        content = f.read()
    assert content == "hello"
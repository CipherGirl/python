```py
# ===============================
# FILE & IO
# ===============================
with open("example.txt", "w") as f:
    f.write("hello")

# # ===============================
# # FILESYSTEM
# # ===============================
import os

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")

# ===============================
# DATABASE
# ===============================
import sqlite3

with sqlite3.connect(":memory:") as conn:
    conn.execute("CREATE TABLE test (id INTEGER)")
    conn.execute("INSERT INTO test VALUES (1)")

# ===============================
# THREADING / CONCURRENCY
# ===============================
from threading import Lock

lock = Lock()
counter = 0

with lock:
    counter += 1

# ===============================
# TEMPORARY FILES & DIRECTORIES
# ===============================
import tempfile

with tempfile.NamedTemporaryFile() as f:
    f.write(b"temp data")

with tempfile.TemporaryDirectory() as tmpdir:
    print("Temp dir:", tmpdir)

# ===============================
# TESTING (pytest)
# ===============================
import pytest

with pytest.raises(ValueError):
    int("abc")

# ===============================
# MOCKING
# ===============================
from unittest.mock import patch

with patch("math.sqrt") as mock_sqrt:
    mock_sqrt.return_value = 10
    import math
    assert math.sqrt(4) == 10

# ===============================
# EXCEPTION SUPPRESSION
# ===============================
from contextlib import suppress
import os

with suppress(FileNotFoundError):
    os.remove("non_existent_file.txt")

# ===============================
# REDIRECT STDOUT
# ===============================
from contextlib import redirect_stdout
import io

buffer = io.StringIO()
with redirect_stdout(buffer):
    print("captured output")

# ===============================
# DECIMAL CONTEXT (FINANCE)
# ===============================
from decimal import Decimal, localcontext

with localcontext() as ctx:
    ctx.prec = 2
    result = Decimal("1.234") * Decimal("3.456")

# ===============================
# NETWORK / HTTP
# ===============================
from urllib.request import urlopen

with urlopen("https://google.com") as response:
    html = response.read()


# ===============================
# RESOURCE CLEANUP
# ===============================
from contextlib import closing
import socket

with closing(socket.socket()) as sock:
    sock.connect(("example.com", 80))

# ===============================
# CUSTOM CONTEXT MANAGER (CLASS)
# ===============================
class Timer:
    def __enter__(self):
        import time
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        print("Elapsed:", time.time() - self.start)

with Timer():
    sum(range(100000))

# ===============================
# GENERATOR-BASED CONTEXT MANAGER
# ===============================
from contextlib import contextmanager

@contextmanager
def simple_context():
    print("enter")
    yield
    print("exit")

with simple_context():
    print("inside")

# ===============================
# ASYNC CONTEXT MANAGER (EXAMPLE)
# ===============================
import asyncio

async def async_example():
    lock = asyncio.Lock()
    async with lock:
        pass

# asyncio.run(async_example())
```

## contextlib 

### 
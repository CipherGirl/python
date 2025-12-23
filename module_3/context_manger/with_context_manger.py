"""
this with statement, open() returns an io.TextIOBase object. 
This object supports the context manager protocol, 
so the with statement calls .__enter__() and 
assigns its return value to file. 

Then, you can manipulate the file inside the with code block. 
When the block ends, Python automatically calls .__exit__(), 
which closes the file even if an exception occurs in the with code block.
"""
with open("hello.txt", mode="w", encoding="utf-8") as file:
    file.write("Hello, World!")

import logging
import pathlib

file_path = pathlib.Path("/hello.txt")
try:
     with file_path.open(mode="w") as file:
        file.write("Hello, World!")
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)

"""
Traversing Directories

A with statement with os.scandir() as the context manager supplier. 
Then, you iterate over the entries in the working directory represented by "." and 
print their names and sizes on the screen. 
In this case, .__exit__() calls scandir.close() to 
close the iterator and release the acquired resources.
"""
import os

with os.scandir(".") as entries:
     for entry in entries:
         print(entry.name, "->", entry.stat().st_size, "bytes")






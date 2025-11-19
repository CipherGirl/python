import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir, "example.txt")

if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        f.write("This is a new file.\n")

with open(file_path, "r") as f:
    print(f.read())



with open(file_path, "w") as f:
    f.write("Hello, Python!\n")
    f.write("File handling is fun.")


# with open(file_path, "r") as f:
#     print(f.read())

with open(file_path, "r") as f:
    for line in f:
        print("Line:", line.strip())

with open(file_path, "r") as f:
    print("First 10 characters:", f.read(10))
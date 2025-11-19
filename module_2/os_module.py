# Corey Schafer - Python Tutorial: OS Module - Use Underlying Operating System Functionality

import os

# print(os.getcwd())
# print(os.listdir()) 

# print(os.makedirs('test/sub'))
# print(os.removedirs('test/sub'))

# os.rename('example.txt', 'demo.txt')

# print(os.stat('demo.txt').st_size) # file details - Size, last modification time

# for dirpath, dirname, filenames in os.walk("/Users/welldev/Code/Personal/python/module_2"):
#     print("Curent Path: " , dirpath)
#     print("Directories: ", dirname)
#     print("Files: ", filenames)
#     print()


# print(os.environ.get('HOME'))

# module_1 = os.path.join((os.environ.get('HOME')) , 'Code/Personal/python/module_1')

# print(module_1)

# for dirpath, dirname, filenames in os.walk(module_1):
#     print("Curent Path: " , dirpath)
#     print("Directories: ", dirname)
#     print("Files: ", filenames)
#     print()

# print(os.path.basename(module_1))
# print(os.environ.get('HOME'))
# print(os.path.split(os.environ.get('HOME')))
# print(os.path.exists(module_1))
# print(os.path.isdir(module_1))
# print(os.path.isfile(module_1))


# JimShapedCoding - Python OS Module | The best functions

# Chat GPT Advanced Functions
with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.stat().st_size)

fd = os.open("demo.txt", os.O_RDONLY)
stat = os.fstat(fd)

print(os.uname())
print(os.cpu_count())
print(os.getpid(),os.getppid())
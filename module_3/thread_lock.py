import threading
import time

FILE_NAME = "/Users/welldev/Code/self-development/python/content.txt"

def read_file():
    with open(FILE_NAME, 'r') as file:
        content = file.read()
        print(f'{threading.current_thread().name} Read: {content}')

def modify_file():
    with open(FILE_NAME, 'w') as file:
        file.write("Modifier Content")
        print(f'{threading.current_thread().name} modified the file')

lock = threading.Lock()

def read_file_locked():
    with lock:
        with open(FILE_NAME, 'r') as file:
            content = file.read()
            print(f'{threading.current_thread().name} Read: {content}')

def modify_file_locked():
    with lock:
        with open(FILE_NAME, 'w') as file:
            file.write("Locked Modify Content")
            print(f'{threading.current_thread().name} modified the file')


threads = []

for _ in range(5):
    read_thread = threading.Thread(target=read_file_locked)
    modify_thread = threading.Thread(target=modify_file_locked)

    threads.append(read_thread)
    threads.append(modify_thread)

    read_thread.start()
    modify_thread.start()

for thread in threads:
    thread.join()



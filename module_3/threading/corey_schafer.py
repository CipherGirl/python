"""
This is blocking example
"""
# import time

# start = time.perf_counter()

# def do_something():
#     print("Sleeping 1 Second")
#     time.sleep(1)
#     print("Done Sleeping")

# do_something()
# do_something()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds')

"""
This is threading
"""
import time, threading, os

start = time.perf_counter()

def do_something(seconds, arg):
    pid = os.getpid()
    thread_count = threading.current_thread()

    print(f"[PID {pid}] Threads: {thread_count} → Sleeping {seconds}s, {arg}")
    time.sleep(seconds)
    print(f"[PID {pid}] Done")
    

# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# t1.start()
# t2.start()

# t1.join()
# t2.join()
threads = []

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1, _])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')



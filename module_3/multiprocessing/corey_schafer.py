# import time
# import multiprocessing
# import os

# def do_something(second):
#     pid = os.getpid()
#     print(f"[PID {pid}] Sleeping {second} Second")
#     time.sleep(1)
#     print(f"[PID {pid}] Done Sleeping")

# if __name__ == "__main__":
#     start = time.perf_counter()

#     # p1 = multiprocessing.Process(target=do_something)
#     # p2 = multiprocessing.Process(target=do_something)

#     # p1.start()
#     # p2.start()

#     # p1.join()
#     # p2.join()


#     processes = []

#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[1.5])
#         p.start()
#         processes.append(p)

#     for process in processes:
#         process.join()

#     finish = time.perf_counter()

#     print(f'Finished in {round(finish-start, 2)} seconds')



#     finish = time.perf_counter()
#     print(f"Finished in {round(finish - start, 2)} seconds")

import os
import time
import threading
import multiprocessing
import psutil

def do_something(seconds):
    pid = os.getpid()
    thread_name = threading.current_thread().name

    # Set CPU affinity
    # proc = psutil.Process(pid)
    # proc.cpu_affinity([0, 1])
    # print(f"[PID {pid}] CPU affinity: {proc.cpu_affinity()}")

    print(f"[PID {pid}] Thread: {thread_name} → Sleeping {seconds}s")
    time.sleep(seconds)
    print(f"[PID {pid}] Done")

if __name__ == "__main__":
    processes = []

    for _ in range(1000000):  # reduced to 10 to avoid CPU overload
        p = multiprocessing.Process(target=do_something, args=(5,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()


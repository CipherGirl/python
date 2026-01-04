import time, concurrent.futures, os, threading

start = time.perf_counter()

def do_something(seconds, arg=None):
    pid = os.getpid()
    thread_count = threading.current_thread()

    print(f"[PID {pid}] Threads: {thread_count.name} → Sleeping {seconds}s, {arg}")
    time.sleep(seconds)
    return f"[PID {pid}] Done Executing {seconds}s"
    # return "Done Executing"
    
with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_something, seconds=1)
    f2 = executor.submit(do_something, seconds=1)

    seconds = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in seconds]
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    results = executor.map(do_something, seconds)

    for result in results:
        print(result)


#
# threads = []
#
# for _ in range(10):
#     t = threading.Thread(target=do_something, args=[1, _])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds')



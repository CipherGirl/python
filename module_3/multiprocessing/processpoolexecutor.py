import time
import concurrent.futures
import os
import multiprocessing

start = time.perf_counter()

def do_something(seconds):
    pid = os.getpid()
    process_name = multiprocessing.current_process().name
    
    print(f"[PID {pid}] Process: {process_name} → Sleeping {seconds}s")
    time.sleep(seconds)
    return f"[PID {pid}] Done Executing {seconds}s"

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        seconds = [5, 4, 3, 2, 1]
        
        # Using map - processes items in order
        results = executor.map(do_something, seconds)
        
        for result in results:
            print(result)
    
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} seconds')
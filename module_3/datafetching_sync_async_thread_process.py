import time
import asyncio
import aiohttp
import requests
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List

# Dummy URLs to fetch (using httpbin for testing)
URLS = [
    "https://httpbin.org/anything",
    "https://httpbin.org/anything",
    "https://httpbin.org/anything",
    "https://httpbin.org/anything",
    "https://httpbin.org/anything",
]


# ============================================
# 1. SYNCHRONOUS APPROACH
# ============================================
def fetch_url_sync(url: str) -> dict:
    """Fetch a single URL synchronously"""
    response = requests.get(url)
    return {"url": url, "status": response.status_code, "length": len(response.text)}


def synchronous_fetching(urls: List[str]):
    """Fetch all URLs one by one"""
    print("\n=== SYNCHRONOUS FETCHING ===")
    start = time.time()
    
    results = []
    for url in urls:
        result = fetch_url_sync(url)
        results.append(result)
        print(f"Fetched: {result['url']} - Status: {result['status']}")
    
    elapsed = time.time() - start
    print(f"Total time: {elapsed:.2f} seconds")
    return results


# ============================================
# 2. ASYNCHRONOUS WITH ASYNCIO
"""
Timeline visualization:
Thread 1: [Start Task1] → [await...] [Start Task2] → [await...] [Continue Task1] → [Done]
          └────────────────────────────────────────┬────────────────────────────────────┘
                                        Single thread switching
"""
# ============================================
async def fetch_url_async(session: aiohttp.ClientSession, url: str) -> dict:
    """Fetch a single URL asynchronously"""
    async with session.get(url) as response:
        text = await response.text()
        return {"url": url, "status": response.status, "length": len(text)}


async def async_fetching(urls: List[str]):
    """Fetch all URLs concurrently using asyncio"""
    print("\n=== ASYNCHRONOUS FETCHING (asyncio) ===")
    start = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url_async(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    
    for result in results:
        print(f"Fetched: {result['url']} - Status: {result['status']}")
    
    elapsed = time.time() - start
    print(f"Total time: {elapsed:.2f} seconds")
    return results


# ============================================
# 3. THREADPOOL EXECUTOR
# ============================================
"""
Timeline visualization:
Thread 1: [████ I/O wait ████] [process]
Thread 2:   [████ I/O wait ████] [process]
Thread 3:     [████ I/O wait ████] [process]
          └── All waiting simultaneously ──┘
"""
def threadpool_fetching(urls: List[str], max_workers: int = 5):
    """Fetch URLs using a thread pool"""
    print("\n=== THREADPOOL FETCHING ===")
    start = time.time()
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(fetch_url_sync, urls))
    
    for result in results:
        print(f"Fetched: {result['url']} - Status: {result['status']}")
    
    elapsed = time.time() - start
    print(f"Total time: {elapsed:.2f} seconds")
    return results


# ============================================
# 4. PROCESSPOOL EXECUTOR
"""
Timeline visualization:
Process 1: [████████] CPU Core 1
Process 2: [████████] CPU Core 2
Process 3: [████████] CPU Core 3
          └─ Running simultaneously ─┘
"""
# ============================================
def fetch_url_for_process(url: str) -> dict:
    """Fetch URL (must be picklable for ProcessPool)"""
    import requests  # Import inside function for multiprocessing
    response = requests.get(url)
    return {"url": url, "status": response.status_code, "length": len(response.text)}


def processpool_fetching(urls: List[str], max_workers: int = 5):
    """Fetch URLs using a process pool"""
    print("\n=== PROCESSPOOL FETCHING ===")
    start = time.time()
    
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(fetch_url_for_process, urls))
    
    for result in results:
        print(f"Fetched: {result['url']} - Status: {result['status']}")
    
    elapsed = time.time() - start
    print(f"Total time: {elapsed:.2f} seconds")
    return results


# ============================================
# MAIN EXECUTION
# ============================================
if __name__ == "__main__":
    print("Comparing different data fetching approaches...")
    print(f"Fetching {len(URLS)} URLs (each with 1 second delay)\n")
    
    # 1. Synchronous
    synchronous_fetching(URLS)
    
    # 2. Asynchronous with asyncio
    asyncio.run(async_fetching(URLS))
    
    # 3. ThreadPool
    threadpool_fetching(URLS, max_workers=5)
    
    # 4. ProcessPool
    processpool_fetching(URLS, max_workers=5)
    
    print("\n=== SUMMARY ===")
    print("Synchronous: Sequential execution, slowest for I/O")
    print("Asyncio: Best for I/O-bound tasks, single-threaded concurrency")
    print("ThreadPool: Good for I/O-bound, easier than asyncio for legacy code")
    print("ProcessPool: Best for CPU-bound tasks, overhead for I/O operations")
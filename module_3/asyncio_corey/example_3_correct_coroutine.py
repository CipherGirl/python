import asyncio, time

async def fetch_data(param):
    print(f'Do something with {param}')
    await asyncio.sleep(param)
    print(f'Done with {param}')
    return f'Result of {param}'


async def main():
    # Order of the execution in the event loop depends
    # on the order we are queuing the coroutines here
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    # If I await task2 here the background will run task1 first
    # But as we awaited task2 it will save the task1 result to memory
    # And return the result for task2 first, with task1 already completed and stored away
    result1 = await task1
    print("Fetching result1 completed")

    result2 = await task2
    print("Fetching result2 completed")

    return [result1, result2]

t1 = time.perf_counter()
results = asyncio.run(main())
t2 = time.perf_counter()

print(f"Total time: {t2-t1:.2f}")
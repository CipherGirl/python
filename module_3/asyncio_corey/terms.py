import asyncio
import time

def sync_function(test_param):
    print("This is synchronous function")

    time.sleep(1)

    return f"Sync Result: {test_param}"

async def async_function(test_param):
    print("This is asynchronous function")
    time.sleep(1)
    return f"Async Result: {test_param}"

async def main():
    # sync_result = sync_function("Synchronous")
    # print(sync_result)
    """"
    Future
    Low-level object representing a result that will be available later.
    States:
    pending → result not ready
    finished → result available
    cancelled → task cancelled
    Similar to JavaScript Promises.
    Usually used indirectly via coroutines and tasks.
    """
    # loop = asyncio.get_running_loop()
    # future = loop.create_future()
    #
    # print(f"Empty Future: {future}")
    #
    # future.set_result("Future Result: Test")
    #
    # future_result = await future
    # print(future_result)

    """
    Coroutine:
    Defined using async def.
    A function whose execution can be paused and resumed.
    Calling a coroutine function returns a coroutine object (an awaitable).
    Use await to run a coroutine object and get its result.
    """
    # coroutine_obj = async_function("Coroutine")
    # print(coroutine_obj)
    #
    # # Scheduled to event loop and run to completion at the same time
    # coroutine_result = await coroutine_obj
    #
    # print(coroutine_result)

    """
    Task:
    A wrapper around a coroutine that schedules it on the event loop.
    Enables concurrent execution of multiple coroutines.
    Keeps track of completion, exceptions, or cancellation.    
    Tasks are futures under the hood, but with scheduling logic.
    """
    task = asyncio.create_task(async_function("Task"))
    print(task)

    task_result = await task

    print(task_result)
if __name__ == "__main__":
    asyncio.run(main())
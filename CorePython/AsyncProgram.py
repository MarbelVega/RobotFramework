import asyncio
import time
from timeit import default_timer


async def load(delay):
    print(f"Starting {delay} second timer ")
    await asyncio.sleep(delay)


# async is heads-up something in here is long running
async def main():
    start_time = default_timer()
    two_task = asyncio.create_task(load(2))
    three_task = asyncio.create_task(load(3))

    await asyncio.sleep(0.5)
    print("Running other tasks")

    # await tells we're ready to get that value and now we're blocked
    await two_task
    await three_task
    execution_time = default_timer() - start_time
    print(f"{execution_time} is less than 5 seconds")


asyncio.run(main())

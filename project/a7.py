from aioprofile import profile

@profile
async def slow_function():
    await asyncio.sleep(2)
    return "Done!"

async def main():
    result = await slow_function()
    print(result)

asyncio.run(main())


import asyncio
from aioprofile.profiler import AsyncProfiler

async def task_a():
    await asyncio.sleep(1)
    print("Task A finished")

async def task_b():
    await asyncio.sleep(2)
    print("Task B finished")

async def main():
    async with AsyncProfiler(real_time=True):
        await asyncio.gather(task_a(), task_b())

asyncio.run(main())

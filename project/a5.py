# import aiohttp
# import asyncio

# async def fetch_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.text()

# async def main():
#     data = await fetch_data("https://jsonplaceholder.typicode.com/posts")
#     print(data[:100])  # Wyświetl pierwsze 100 znaków

# asyncio.run(main())


# import trio

# async def say_hello():
#     print("Hello!")
#     await trio.sleep(1)
#     print("Goodbye!")

# trio.run(say_hello)


import asyncio

async def deadlock():
    await asyncio.gather(
        asyncio.Lock().acquire(),
        asyncio.Lock().acquire()
    )

asyncio.run(deadlock())


semaphore = asyncio.Semaphore(10)
async def limited_task():
    async with semaphore:
        await some_async_function()
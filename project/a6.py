import asyncio
import aiohttp

async def producer(queue, urls):
    for url in urls:
        await queue.put(url)
    await queue.put(None)  # Znak zakończenia

async def consumer(queue):
    async with aiohttp.ClientSession() as session:
        while True:
            url = await queue.get()
            if url is None:
                break
            async with session.get(url) as response:
                print(await response.text())

async def main():
    queue = asyncio.Queue()
    urls = ["https://jsonplaceholder.typicode.com/posts/1",
            "https://jsonplaceholder.typicode.com/posts/2"]

    await asyncio.gather(producer(queue, urls), consumer(queue))

asyncio.run(main())

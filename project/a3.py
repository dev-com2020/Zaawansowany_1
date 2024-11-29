import asyncio

async def producer(queue):
    for i in range(10):
        await asyncio.sleep(1)
        await queue.put(i)
        print(f'Produced {i}')
    
async def consumer(queue):
    while True:
        item = await queue.get()
        print(f'Consumed {item}')
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    await asyncio.gather(producer(queue), consumer(queue))


asyncio.run(main())
import aiofiles

async def read():
    async with aiofiles.open('file.txt', mode='r') as f:
        return await f.read()
    
async def write(data):
    async with aiofiles.open('file.txt', mode='w') as f:
        await f.write(data)
    
async def main():
    await write('Hello, world!')
    print(await read())

if __name__ == '__main__':  
    import asyncio
    asyncio.run(main())

import asyncio

async def work(name: str, delay: int):
    print(f"{name} 开始")
    await asyncio.sleep(delay)
    print(f"{name} 结束")


async def main():
    # await work("A", 2)
    # await work("B", 2)
    await asyncio.gather(work("A", 2),work("B", 2))


asyncio.run(main())

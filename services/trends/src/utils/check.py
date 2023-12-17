import asyncio

from prisma import Prisma


async def main() -> None:
    db = Prisma(auto_register=True)
    await db.connect()

    data = await db.trendingdata.find_many()
    print(data)

    await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())

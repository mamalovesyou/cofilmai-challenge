import os

from prisma import Prisma

prisma = Prisma(
    datasource={
        "url": os.environ.get("DATABASE_URL"),
    }
)

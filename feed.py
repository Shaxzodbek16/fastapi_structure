# It is for feed the data to the model for training and testing purpose
import asyncio

from faker import Faker
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.databases.postgres import get_general_session


class Feed:
    def __init__(self, session: AsyncSession = Depends(get_general_session)) -> None:
        self.__session = session
        self.__faker = Faker()

    async def feed_user_model(self, count: int) -> list[int]:
        pass

    async def run(self):
        users_id = await self.feed_user_model(100)
        print("Successfully fed the data to the models")


feed = Feed()
if __name__ == "__main__":
    feed = Feed()
    asyncio.run(feed.run())

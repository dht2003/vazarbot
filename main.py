import asyncio
import os
from loguru import logger
from dotenv import load_dotenv
from bot import bot


async def main():
    load_dotenv()
    token = os.getenv("DISCORD_TOKEN")
    await bot.load_extension("cogs.notifications")
    await bot.load_extension("cogs.popup")
    await bot.load_extension("cogs.settings")
    logger.debug(f"Cogs Loaded")
    await bot.start(token)


if __name__ == "__main__":
    asyncio.run(main())
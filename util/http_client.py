import aiohttp
from bot import bot_config

async def bot_api_post(path: str, payload: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"{bot_config.api_url}{path}",
            json=payload,
            timeout=aiohttp.ClientTimeout(total=5)
        ) as resp:
            text = await resp.text()
            if resp.status != 200:
                raise RuntimeError(text)
            return text
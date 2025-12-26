from dataclasses import dataclass
import discord
import loguru

DEFAULT_API_URL = "http://127.0.0.1:5000"

@dataclass
class BotConfig:
    prefix: str = "!"
    api_url: str = DEFAULT_API_URL


bot_config = BotConfig()

INTENTS = discord.Intents.default()
INTENTS.message_content = True

def get_prefix(_, __):
    return bot_config.prefix


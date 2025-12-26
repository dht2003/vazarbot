from loguru import logger
from discord.ext import commands
from .bot_config import get_prefix, INTENTS



bot = commands.Bot(command_prefix=get_prefix,
                   intents=INTENTS)

@bot.event
async def on_ready():
    logger.debug("Bot ready")
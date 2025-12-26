from loguru import logger
from discord.ext import commands
from util import bot_api_post


class Popup(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="popup")
    async def popup(self, ctx, msg):
        logger.debug(f"{self.bot.user} sending popup msg: {msg}")

        payload = {
            "msg": msg
        }

        try:
            await bot_api_post("/popup_notification", payload)
            await ctx.send(
                f"sent popup msg: {msg}"
            )
        except Exception as e:
            await ctx.send(f"❌ {e}")

async def setup(bot):
    await bot.add_cog(Popup(bot))
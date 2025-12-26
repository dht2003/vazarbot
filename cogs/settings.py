from discord.ext import commands
from bot import bot_config

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="prefix")
    @commands.has_permissions(administrator=True)
    async def set_prefix(self, ctx, new_prefix: str):
        old = bot_config.prefix
        bot_config.prefix = new_prefix
        await ctx.send(f"✅ Prefix changed `{old}` → `{new_prefix}`")

    @commands.command(name="config")
    async def show(self, ctx):
        await ctx.send(
            f"⚙️ **Bot Config**\n"
            f"Prefix: `{bot_config.prefix}`\n"
            f"API: `{bot_config.api_url}`"
        )

async def setup(bot):
    await bot.add_cog(Settings(bot))

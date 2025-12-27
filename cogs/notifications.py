from loguru import logger
from discord.ext import commands
from util import bot_api_post, parse_start_time


class Notification(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def _add_notification(self, ctx, when: str, time: str, title: str):
        try:
            start_time = parse_start_time([when, time])
        except ValueError as e:
            await ctx.send(f"❌ {e}")
            return

        payload = {
            "time": start_time.isoformat(),
            "title": title
        }

        try:
            await bot_api_post("/add_notification", payload)
            logger.debug(f"sending notification to endpoint with {self.bot.user}")
            await ctx.send(
                f"📅 **{title}**\n"
                f"At: `{start_time.strftime('%Y-%m-%d %H:%M')}`"
            )
        except Exception as e:
            await ctx.send(f"❌ {e}")

    @commands.command(name="notification",
                      description=(
                              "Schedule a meeting\n\n"
                              "Examples:\n"
                              "• /notification in 10m Standup\n"
                              "• /notification at 14:30 title:Daily Sync\n"
                      ))
    async def notification(self, ctx
                           , when: str = commands.parameter(description="in/at")
                           , time: str = commands.parameter(description="The time for the notification")
                           , title: str = commands.parameter(description="The title for the notification")):
        await self._add_notification(ctx, when, time, title)

    @commands.command(name="paramedic")
    async def paramedic(self, ctx, patient: str = commands.parameter(description="The patient for the appointment"),
                        when: str = commands.parameter(description="in/at"),
                        time: str = commands.parameter(description="The time for the notification")):
        await self._add_notification(ctx, when, time, f"{patient} has an appointment with the paramedic")

    @commands.command(name="doctor")
    async def doctor(self, ctx, patient: str = commands.parameter(description="The patient for the appointment"),
                        when: str = commands.parameter(description="in/at"),
                        time: str = commands.parameter(description="The time for the notification")):
        await self._add_notification(ctx, when, time, f"{patient} has an appointment with the doctor")


async def setup(bot):
    await bot.add_cog(Notification(bot))

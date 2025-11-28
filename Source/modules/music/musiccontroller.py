from discord.ext import commands
from .musicservice import MusicService

class MusicController(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.service = MusicService()

    @commands.command(name="play")
    async def play(self, ctx, *, url: str):
        """Toca uma música pelo link."""
        await self.service.play_music(ctx, url)

    @commands.command(name="pause")
    async def pause(self, ctx):
        await self.service.pause(ctx)

    @commands.command(name="resume")
    async def resume(self, ctx):
        await self.service.resume(ctx)

    @commands.command(name="stop")
    async def stop(self, ctx):
        await self.service.stop(ctx)


async def setup(bot):
    await bot.add_cog(MusicController(bot))

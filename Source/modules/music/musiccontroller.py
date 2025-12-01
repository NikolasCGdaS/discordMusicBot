from discord.ext import commands
from .musicservice import MusicService

class MusicController(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.service = MusicService()

    @commands.command(name="play")
    async def play(self, ctx, *, query: str):
        await self.service.play_music(ctx, query)
    
    @commands.command(name="pause")
    async def pause(self, ctx):
        await self.service.pause(ctx)

    @commands.command(name="resume")
    async def resume(self, ctx):
        await self.service.resume(ctx)

    @commands.command(name="stop")
    async def stop(self, ctx):
        await self.service.stop(ctx)
    
    @commands.command(name="queue")
    async def queue(self, ctx):
        await self.service.queue(ctx)

    @commands.command(name="skip")
    async def skip(self, ctx):
        await self.service.skip(ctx)



async def setup(bot):
    await bot.add_cog(MusicController(bot))

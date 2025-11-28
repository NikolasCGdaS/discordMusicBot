import discord
import yt_dlp

class MusicService:

    def __init__(self):
        # Dicionário para armazenar fila por servidor
        self.queues = {}

    async def join_voice(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Você não está em um canal de voz.")
            return None

        channel = ctx.author.voice.channel

        if ctx.voice_client is None:
            return await channel.connect()
        else:
            return ctx.voice_client
        
    #tocar musica

    async def play_music(self, ctx, url):
        vc = await self.join_voice(ctx)
        if vc is None:
            return

        ydl_opts = {
            'format': 'bestaudio',
            'noplaylist': True
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            audio_url = info['url']

        source = await discord.FFmpegOpusAudio.from_probe(
            audio_url,
            executable="ffmpeg"
        )

        vc.play(source)
        await ctx.send(f"Tocando agora: {info.get('title')}")

    #pausar/despausar musica

    async def pause(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_playing():
            ctx.voice_client.pause()
            await ctx.send("Música pausada.")

    async def resume(self, ctx):
        if ctx.voice_client and ctx.voice_client.is_paused():
            ctx.voice_client.resume()
            await ctx.send("Música retomada.")
            
    #parar musica

    async def stop(self, ctx):
        if ctx.voice_client:
            ctx.voice_client.stop()
            await ctx.send("Música parada.")

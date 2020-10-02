import discord
from discord.ext import commands
from discord.utils import get
import config
import os
# from yandex_music.client import Client
# New coment

# client = Client.from_credentials('maxwwhd@yandex.com', 'Afhnjdsq123')
# client.tracks(['3173236:26637689'])
bot = commands.Bot(command_prefix=config.BOT_PREFIX)


@bot.event
async def on_ready():
    print("Logged in as: " + bot.user.name + "\n")


@bot.command(pass_context=True, aliases=['j', 'joi'])
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f"The bot has connected to {channel}\n")

    await ctx.send(f"Joined {channel}")


bot.run(config.TOKEN)

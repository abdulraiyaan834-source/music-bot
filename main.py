import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

# Yahan prefix '!' se badalkar '>' kar diya gaya hai
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    # Yahan par apna Voice Channel ID dalein jahan bot 24/7 rhega
    channel_id = 123456789012345678
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.connect()

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        await ctx.author.voice.channel.connect()
    else:
        await ctx.send("Aap kisi voice channel mein nahi hain!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()

# Render se token load karne ke liye
bot.run(os.environ['BOT_TOKEN'])

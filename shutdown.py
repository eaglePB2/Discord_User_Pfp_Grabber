import discord
from discord.ext import commands

TOKEN = 'REDACTED'

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready and connected to {bot.user.name}')
    ctx = await bot.get_context(None)
    await ctx.send("Shutting down...")
    await bot.logout()

bot.run(TOKEN)

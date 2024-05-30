import discord
from discord.ext import commands
import json
import requests
import re

intents = discord.Intents.default()
intents.members = True

TOKEN = 'REDACTED'
GUILD_ID = '<Insert Your Guild ID Here>'
JSON_FILE_PATH = 'playerlist.json'

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready and connected to {bot.user.name}')
    await check_pfp_availability()
    print("Account check completed! shutting down...")
    await bot.close()

@bot.command()
async def get_profile_pic(ctx, user_id):
    guild = bot.get_guild(GUILD_ID)
    member = guild.get_member(int(user_id))

    if member is not None:
        profile_pic_url = member.avatar_url_as(size=1024)
        await ctx.send(f"Profile picture of {member.name}: {profile_pic_url}")
        update_pfp_in_json(user_id, str(profile_pic_url))
    else:
        await ctx.send("User not found in the server")

def update_pfp_in_json(user_id, new_pfp_url):
    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for profile in data:
            if profile['id'] == user_id:
                profile['pfp'] = new_pfp_url

    with open(JSON_FILE_PATH, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

async def check_pfp_availability():
    await bot.wait_until_ready()

    with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    for profile in data:
        user_id = profile['id']
        pfp_url = profile['pfp']
        response = requests.head(pfp_url)
        if response.status_code != 200:
            filtered_id = re.search(r'/(\d+)/', pfp_url).group(1)
            User = await bot.fetch_user(filtered_id)
            if User.avatar != None:
                update_pfp_in_json(user_id, str(User.avatar))
            else:
                print("Looks like this user had left the server, or deleted his account :(")
            print(f"user {user_id} avatar has been updated!")
        else:
            print(f"Profile picture for user {user_id} is available.")

bot.run(TOKEN)

import discord
import os
from discord import app_commands
from discord.ext import commands

TOKEN = "YOUR TOKEN HERE"

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix="v!", intents=intents, case_insensitive=True)

@client.event
async def on_ready():
  print("Bot is online!")
  try:
    synced = await client.tree.sync()
    print(f"synced {len(synced)} commands")
  except Exception as e:
    print(e)

client.run(TOKEN)

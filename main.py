import discord
import os
from pytz import timezone
from datetime import datetime
from datetime import date
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

@client.tree.command(name="ping", description="Displays the latency of the bot (in ms)")
async def ping(interaction: discord.Interaction):
  pingEmbed = discord.Embed(color=0x26931b, timestamp=datetime.now())
  pingEmbed.add_field(name="**Pong!**",value=f"Latency: {round(client.latency * 1000)}ms",inline=False)
  pingEmbed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar)
  await interaction.response.send_message(embed=pingEmbed)

client.run(TOKEN)

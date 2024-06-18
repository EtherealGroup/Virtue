import discord
from dotenv import load_dotenv
import os
from pytz import timezone
from datetime import datetime
from datetime import date
from discord import app_commands
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  

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

class InfoMenu(discord.ui.View):
  def __init__(self):
    super().__init__()
    self.value = None
    self.add_item(discord.ui.Button(label="Source Code", url = "https://github.com/EtherealGroup/Virtue", emoji="<githubwhite:1252766253777420349>"))
  

@client.tree.command(name="ping", description="Displays the latency of the bot (in ms)")
async def ping(interaction: discord.Interaction):
  pingEmbed = discord.Embed(color=0x26931b, timestamp=datetime.now())
  pingEmbed.add_field(name="**Pong!**",value=f"Latency: {round(client.latency * 1000)}ms",inline=False)
  pingEmbed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar)
  await interaction.response.send_message(embed=pingEmbed)

@client.tree.command(name = "info", description = "Information about the bot, and the source code")
async def info(interaction: discord.Interaction):
  view = InfoMenu()
  soEmbed = discord.Embed(title="Information", color=0x26931b)
  soEmbed.add_field(name="Ethereal Group", value = "We are Ethereal Group, the developers of this discord bot. We're focused on making open-source and high quality discord bots", inline = False)
  soEmbed.set_thumbnail(url = "https://avatars.githubusercontent.com/u/173092938?s=200&v=4")
  soEmbed.set_footer(text=f"Requested by {interaction.user.name}", icon_url=interaction.user.display_avatar)
  await interaction.response.send_message(embed=soEmbed, view=view)

client.run(TOKEN)

import discord
from discord.ext import commands
from flask import Flask
import threading
import os

# Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True  # Wichtig!
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = os.getenv("DISCORD_TOKEN")


@bot.event
async def on_ready():
    print(f"✅ Eingeloggt als {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

# Flask Server für UptimeRobot
app = Flask("")

@app.route("/")
def home():
    return "Ich bin wach!"

def run():
    app.run(host="0.0.0.0", port=8080)

# Webserver starten
threading.Thread(target=run).start()

# Bot starten
bot.run(TOKEN)
import os
import requests
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def weather(ctx, *, city: str):
    """Fetches weather information for a given city."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']

        message = (
            f"🌤 **Weather in {city.title()}**\n"
            f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)\n"
            f"💨 Humidity: {humidity}%\n"
            f"🌍 Condition: {weather_desc}"
        )
    else:
        message = "City not found. Please enter a valid city name."

    await ctx.send(message)

bot.run(TOKEN)

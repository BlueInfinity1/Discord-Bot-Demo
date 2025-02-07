# Discord Weather Bot

A simple Discord bot that fetches real-time weather updates using the **OpenWeatherMap API**.

## Features
- Get weather updates with `!weather <city>`
- Displays temperature, humidity, and conditions
- Uses `.env` for secure API key storage

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/BlueInfinity1/Discord-Bot-Demo.git
cd Discord-Bot-Demo
```

### 2. Install Dependencies
Make sure you have Python 3.8+ installed, then run:

`
pip install discord.py python-dotenv requests`

### 3. Create a `.env` File
Inside the project directory, create a `.env` file and add:

```env
DISCORD_BOT_TOKEN=your_discord_bot_token
WEATHER_API_KEY=your_openweathermap_api_key
```

### 4. Running the Bot
Start the bot by running:

`
python src/bot.py
`

### 5. Usage
Once the bot is running, you can use the following command in any Discord server where your bot is active:

`
!weather London
`

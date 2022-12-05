# Path: bot.py
# Write a discord bot that can do the following:
# 1. When a user types something in a channel, the bot will log it to console
# Use slash commands to make the bot do the following:
# 1. When a user types /help, the bot will send a message to the channel with the help message
# 2. When a user types /ping, the bot will send a message to the channel with the ping
# 3. When a user types /echo, the bot will send a message to the channel with the message that the user typed

# All the imports required in single line
import discord


# Bot code
async def on_message(message):
    print(message.content)




class Bot(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

import os
import discord
import requests
import json

# Provide a bot Token
TOKEN = os.environ.get('BOT_TOKEN') # get the bot token from the environment variable
BOT_PREFIX = 'bot ' # the prefix for the bot commands


intents = discord.Intents.default()
intents.message_content = True


bot = discord.Client(intents=intents)


name = None
did_ask_for_name = False


@bot.event
async def on_message(msg):
    global name, did_ask_for_name
    if msg.author == bot.user:
        return
    if not msg.content.startswith(BOT_PREFIX):
        return
    if "meme" in msg.content:
        response = requests.get(url="https://meme-api.com/gimme")
        json_data = json.loads(response.text)
        await msg.channel.send(json_data.get('url'))
        return
    print('[New message]', msg.content)
    if did_ask_for_name:
        name = msg.content
    if not name:
        did_ask_for_name = True
        await msg.channel.send('Hallo! Wie heißt du?')
    else:
        await msg.channel.send('Hallo ' + name)
            
        
if __name__ == '__main__':
    bot.run(TOKEN)
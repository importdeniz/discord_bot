import os
import discord
import requests
import json


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_message(msg):
    global name, did_ask_for_name
    if msg.author == bot.user:
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

bot.run(os.environ['BOT_TOKEN'])

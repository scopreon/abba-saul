# bot.py
# import os
#
# import discord
# from dotenv import load_dotenv
# load_dotenv()
# TOKEN = 'NzIxNjQ5NjUxODc4NDYxNDUz.XuXqUg.gCakSDsbfb5J7YYsD-alEVYQ-lo'
# client = discord.Client()
#
# @client.event
# async def on_ready():
#     print(f'{client.user} has connected to Discord!')
#
# client.run(TOKEN)

# bot.py
import os

import discord
import random
from dotenv import load_dotenv
import requests
import ast


def returnMishnah(book,perek,mishnah):
    response = requests.get(f"https://www.sefaria.org/api/texts/Mishnah_{book.title()}.{perek}?commentary=0&context=1&pad=0&wrapLinks=1&multiple=0")
    once = True
    data = response.json()
    res = ast.literal_eval(str(data))
    texts = str(res['text']).split('\', \'')
    texts[0] = texts[0][2:]
    texts[len(texts)-1] = texts[len(texts)-1][:len(texts[len(texts)-1])-2]
    english = texts[mishnah-1]

    hebrew = str(res['he']).split('\', \'')
    hebrew[0] = hebrew[0][2:]
    hebrew[len(hebrew)-1] = hebrew[len(hebrew)-1][:len(hebrew[len(hebrew)-1])-2]
    hebrew = hebrew[mishnah-1][:len(hebrew[mishnah-1])-3]

    returnSt = [english,hebrew]
    return english,hebrew





load_dotenv()
TOKEN = 'NzIxNjQ5NjUxODc4NDYxNDUz.XuXqUg.gCakSDsbfb5J7YYsD-alEVYQ-lo'




client = discord.Client()

@client.event
async def on_ready():
    print('Ready')


@client.event
async def on_message(message):
    print('message recieved')
    if message.author == client.user:
        return
    try:
        if 'abba saul' in message.content:
            response = message.content.split(' ')
            response = returnMishnah(response[2],int(response[3]),int(response[4]))
            await message.channel.send(response[1])
            await message.channel.send(response[0])
    except(Exception):
        pass


# client = CustomClient()
client.run(TOKEN)

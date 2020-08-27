# importing dependencies
import discord
from dotenv import load_dotenv
import requests
import ast

# message parsed to function and processed, chooses which route to take with data
def processMessage(message):
    # splits by spaces into array
    response = message.split(' ')
    # fetching mishnah, Hebrew/Englush
    if response[2] == 'fetch':
        dict = {'book': '', 'perek': '', 'mishnah': '','word':''}
        engOrHebrew = 0
        increment = 0
        # getting all tags and options included in path, allows for them to be any order and still be processed
        for r in response:
            if r == '-b':
                dict['book'] = response[increment + 1]
            if r == '-p':
                dict['perek'] = int(response[increment + 1])
            if r == '-m':
                dict['mishnah'] = int(response[increment + 1])
            if r == '-o':
                engOrHebrew = int(response[increment + 1])
            increment += 1
        # call returnMishnah() function with dictionary of all parameters to print required mishnah
        # store returned values in response new response
        response = returnMishnah(dict)
        # inline if, handles if they only want the Hebrew or only the English
        # Returns normal response if endOrHebrew is 0 (both) returns only 1 data entry if otherwise
        return response if not engOrHebrew else response[engOrHebrew-1]
    # translate option
    if response[2]=='translate':
        print(response)
        response = translate(response[4])
        return response
    # help option
    if response[2] == 'help':
        response=('''Welcome to abba saul, the best mishnah bot on the market!!!
        How to use:
        
        Mode options:
        fetch: this will fetch a mishnah from sefaria, both English and Hebrew
        +Tags:
        ++ -b: specifies the book
        ++ -p: specifies the perek
        ++ -m: specifies the mishnah
        ++ -o: specifies if you would like only the Hebrew (1) or English (2). {Default=Both}
        translate: will translate a specific word
        +Tags:
        ++ -w: word to translate
        
        ''')
        return 'Help'+response


# this function makes a GET request to the Sefaria API  
def returnMishnah(dict):
    # read book and perek into response
    # this function has just lots of data monipulation to get it into the right format
    response = requests.get(f"https://www.sefaria.org/api/texts/Mishnah_{dict['book'].title()}.{dict['perek']}?commentary=0&context=1&pad=0&wrapLinks=1&multiple=0")
    data = response.json()
    res = ast.literal_eval(str(data))
    texts = str(res['text']).split('\', \'')
    texts[0] = texts[0][2:]
    texts[len(texts)-1] = texts[len(texts)-1][:len(texts[len(texts)-1])-2]
    english = texts[dict['mishnah']-1]

    hebrew = str(res['he']).split('\', \'')
    hebrew[0] = hebrew[0][2:]
    hebrew[len(hebrew)-1] = hebrew[len(hebrew)-1][:len(hebrew[len(hebrew)-1])-2]
    hebrew = hebrew[dict['mishnah']-1][:len(hebrew[dict['mishnah']-1])-3]
    # add language at beginning of data to tell which language it is in
    return 'Hebrew#'+hebrew,'English#'+english

# translates an indivual word
def translate(val):
    print('translatin')
    response = requests.get(f"https://www.sefaria.org/api/words/{val.title()}")
    data = response.json()
    res = ast.literal_eval(str(data))
    translation=res[0]['content']['senses'][0]['definition']
    return 'Translation'+translation


load_dotenv()
# API token
TOKEN = 'NzIxNjQ5NjUxODc4NDYxNDUz.XuXqUg.gCakSDsbfb5J7YYsD-alEVYQ-lo'
client = discord.Client()

@client.event
async def on_ready():
    print('Ready')

# main message handler
@client.event
async def on_message(message):
    print('message recieved')
    if message.author == client.user:
        return
    # only process message if starts are 'abba saul'
    if 'abba saul' in message.content:
        response = processMessage(message.content)
        embed = discord.Embed(title="Mishna Bot")
        embed.set_author(name="abba saul")
        try:
            if response[:11] == 'Translation':
                embed.add_field(name='Hebrew', value=message.content.split(' ')[4], inline=False)
                embed.add_field(name='Translation', value=response[11:], inline=False)
                await message.channel.send(embed=embed)
        except(Exception):
            pass
        try:
            if response[:4] == 'Help':
                embed.add_field(name='Help', value=response[4:], inline=False)
                await message.channel.send(embed=embed)
        except(Exception):
            pass
        try:
            for r in (response if not type(response) is str else [response]):
                r = r.split('#')
                embed.add_field(name=r[0], value=r[1], inline=False)
            await message.channel.send(embed=embed)
        except(Exception):
            pass
    try:
        pass
    except(Exception):
        await message.channel.send('Oy vei it seems something went wrong... don\'t do anything silly')




# client = CustomClient()
client.run(TOKEN)

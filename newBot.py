import discord
import asyncio
import botMessages
import botSecret
import requests
import re
import os
from os import environ
import urllib.request
from bs4 import BeautifulSoup

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
#!test -A test command for the bot
    if message.content.startswith('!test'):
        await client.send_message(message.channel, botMessages.Test)

#!cat -send a random image of a cat
    if message.content.startswith('!cat'):
        response = requests.get('http://thecatapi.com/api/images/get', stream=True)
        with open ('cat.png', 'wb') as f:
            f.write(response.raw.read())
        with open('cat.png', 'rb') as f:
            await client.send_file(message.channel, f, filename='cat.png', content='Please, enjoy this cat.')
            
    if message.content.startswith('!help'):
        await client.send_message(message.channel, content='__**Michael Bot Help**__\n\n Command-Format: !meal-diningcenter \n All lower case\n Replace meal with food for whole day menu')

    if message.content.startswith('!food-udcc'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/udm", "all", "none", "none", "none"))
    if message.content.startswith('!breakfast-udcc'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/udm", "first", "Lunch", "none", "Breakfast")) 
    if message.content.startswith('!lunch-udcc'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/udm", "middle", "Dinner", "Breakfast", "Lunch"))
    if message.content.startswith('!dinner-udcc'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/udm", "middle", "none", "Lunch", "Dinner"))

    if message.content.startswith('!food-windows'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/windows", "all", "none", "none", "none")) 
    if message.content.startswith('!lunch-windows'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/windows", "first", "Continuous Service", "none", "Breakfast")) 
    if message.content.startswith('!continuousservice-windows'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/windows", "middle", "Dinner", "Breakfast", "Continuous Service"))
    if message.content.startswith('!dinner-windows'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/windows", "middle", "Late Night", "Continuous Service", "Dinner"))
    if message.content.startswith('!latenight-windows'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/windows", "middle", "none", "Dinner", "Late Night"))

    if message.content.startswith('!food-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "all", "none", "none", "none")) 
    if message.content.startswith('!breakfast-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "first", "Lunch", "none", "Breakfast")) 
    if message.content.startswith('!lunch-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "middle", "Continuous Service", "Breakfast", "Lunch"))
    if message.content.startswith('!continuousservice-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "middle", "Dinner", "Lunch", "Continuous Service"))
    if message.content.startswith('!dinner-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "middle", "none", "Continuous Service", "Dinner"))
    if message.content.startswith('!food-conversations'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/conversations", "all", "none", "none", "none")) 

    if message.content.startswith('!food-seasons'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/seasons", "all", "none", "none", "none")) 
    if message.content.startswith('!breakfast-seasons'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/seasons", "first", "Lunch", "none", "Breakfast")) 
    if message.content.startswith('!lunch-seasons'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/seasons", "middle", "Dinner", "Breakfast", "Lunch"))
    if message.content.startswith('!dinner-seasons'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/seasons", "middle", "Late Night", "Lunch", "Dinner"))
    if message.content.startswith('!latenight-seasons'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/seasons", "middle", "none", "Dinner", "Late Night"))

    if message.content.startswith('!food-storms'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/storms", "all", "none", "none", "none")) 
    if message.content.startswith('!breakfast-storms'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/storms", "first", "Lunch", "none", "Breakfast")) 
    if message.content.startswith('!lunch-storms'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/storms", "middle", "Dinner", "Breakfast", "Lunch"))
    if message.content.startswith('!dinner-storms'):
        await client.send_message(message.channel,food("http://www.dining.iastate.edu/menus/storms", "middle", "none", "Lunch", "Dinner"))


def food(link, time, next, previous, curent):
    if time == "all":
        webPage = link
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        final = ""
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']})
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if dinnerStuffWord == "Breakfast" or dinnerStuffWord == "Lunch" or dinnerStuffWord == "Dinner" or dinnerStuffWord == "Continuous Service" or dinnerStuffWord == "Late Night":
                final += "\n**" + dinnerStuffWord + "**\n\n"
            else:
                final += dinnerStuffWord + "\n"
        return final
    if time == "first":
        webPage = link
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        final = ""
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header', 'station-header']})
        for y in range (0, len(dinnerStuff)):
                stringElement = str(dinnerStuff[y])
                if 'station-header' in stringElement:
                    final += "\n**" + dinnerStuff[y].text + "**\n"
                else:
                    dinnerStuffWord = dinnerStuff[y].text
                    if next ==  dinnerStuffWord:
                        break
                    if dinnerStuffWord == "Breakfast" or dinnerStuffWord == "Lunch":
                        final += "\n__**" + dinnerStuffWord + "**__\n"
                    else:
                        final += dinnerStuffWord + "\n"
        return final
    if time == "middle":
        print = 0
        webPage = link
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        final = ""
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header', 'station-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if curent ==  dinnerStuffWord or print == 1:
                print = 0
                if next != dinnerStuffWord:
                    print = 1
                    stringElement = str(dinnerStuff[y])
                    if 'station-header' in stringElement:
                        final += "\n**" + dinnerStuff[y].text + "**\n"
                    else:
                        if  dinnerStuffWord == "Lunch" or dinnerStuffWord == "Dinner" or dinnerStuffWord == "Continuous Service":
                            final += "\n__**" + dinnerStuffWord + "**__\n"
                        else:
                            final += dinnerStuffWord + "\n" 
        return final
    if time == "last":
        print = 0
        webPage = link
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        final = ""
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header', 'station-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if curent ==  dinnerStuffWord or print == 1:
                stringElement = str(dinnerStuff[y])
                if 'station-header' in stringElement:
                    final += "\n**" + dinnerStuff[y].text + "**\n"
                else:
                    if dinnerStuffWord == "Lunch" or dinnerStuffWord == "Dinner" or dinnerStuffWord == "Late Night":
                        final += "\n__**" + dinnerStuffWord + "**__\n"
                    else:
                        final += dinnerStuffWord + "\n" 
                print = 1
        return final


    

#Run locally
#client.run(botSecret.Token)

#Run on Heroku. Defined under Settings->Config Vars
Sclient.run(os.environ.get['BOT_TOKEN'])

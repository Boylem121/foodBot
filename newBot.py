import discord
import asyncio
import botMessages
import botSecret
import requests
import re
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

    if message.content.startswith('!food-udcc'):
        webPage = 'http://www.dining.iastate.edu/menus/udm'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!breakfast-udcc'):
        webPage = 'http://www.dining.iastate.edu/menus/udm'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord:
                break
            await client.send_message(message.channel,dinnerStuffWord)  

    if message.content.startswith('!lunch-udcc'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/udm'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Dinner" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!dinner-udcc'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/udm'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Dinner" ==  dinnerStuffWord or print == 1:
                await client.send_message(message.channel,dinnerStuffWord)
                print = 1
                      
        
    if message.content.startswith('!food-windows'):
        webPage = 'http://www.dining.iastate.edu/menus/windows'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinner = []
        dinner = soup.findAll("div", attrs={"class": "menu-item"}, limit=43)
        for x in range (0, len(dinner)):
            dinnerFood = dinner[x].text
            await client.send_message(message.channel, dinnerFood)

    if message.content.startswith('!lunch-windows'):
        webPage = 'http://www.dining.iastate.edu/menus/windows'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Continuous Service" ==  dinnerStuffWord:
                break
            await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!continuousservice-windows'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/windows'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Continuous Service" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Dinner" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!dinner-windows'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/windows'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Dinner" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Late Night" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!latenight-windows'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/windows'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Late Night" ==  dinnerStuffWord or print == 1:
                await client.send_message(message.channel,dinnerStuffWord)
                print = 1

    if message.content.startswith('!food-seasons'):
        webPage = 'http://www.dining.iastate.edu/menus/seasons'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinner = []
        dinner = soup.findAll("div", attrs={"class": "menu-item"}, limit=43)
        for x in range (0, len(dinner)):
            dinnerFood = dinner[x].text
            await client.send_message(message.channel, dinnerFood)

    if message.content.startswith('!breakfast-seasons'):
        webPage = 'http://www.dining.iastate.edu/menus/seasons'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord:
                break
            await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!continuousservice-seasons'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/seasons'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Continuous Service" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Dinner" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!dinner-seasons'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/seasons'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Dinner" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Late Night" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!latenight-seasons'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/seasons'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Late Night" ==  dinnerStuffWord or print == 1:
                await client.send_message(message.channel,dinnerStuffWord)
                print = 1

    if message.content.startswith('!food-conversations'):
        webPage = 'http://www.dining.iastate.edu/menus/conversations'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinner = []
        dinner = soup.findAll("div", attrs={"class": "menu-item"}, limit=43)
        for x in range (0, len(dinner)):
            dinnerFood = dinner[x].text
            await client.send_message(message.channel, dinnerFood)

    if message.content.startswith('!breakfast-conversations'):
        webPage = 'http://www.dining.iastate.edu/menus/conversations'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord:
                break
            await client.send_message(message.channel,dinnerStuffWord) 

    if message.content.startswith('!lunch-conversations'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/conversations'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Continuous Service" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!continuousservice-conversations'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/conversations'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Continuous Service" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Dinner" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!dinner-storms'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/conversations'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Dinner" ==  dinnerStuffWord or print == 1:
                await client.send_message(message.channel,dinnerStuffWord)
                print = 1

    if message.content.startswith('!food-storms'):
        webPage = 'http://www.dining.iastate.edu/menus/storms'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinner = []
        dinner = soup.findAll("div", attrs={"class": "menu-item"}, limit=43)
        for x in range (0, len(dinner)):
            dinnerFood = dinner[x].text
            await client.send_message(message.channel, dinnerFood)

    if message.content.startswith('!breakfast-storms'):
        webPage = 'http://www.dining.iastate.edu/menus/storms'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord:
                break
            await client.send_message(message.channel,dinnerStuffWord) 

    if message.content.startswith('!lunch-storms'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/storms'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Lunch" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Continuous Service" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!continuousservice-storms'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/storms'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Continuous Service" ==  dinnerStuffWord or print == 1:
                print = 0
                if "Dinner" != dinnerStuffWord:
                    print = 1 
                    await client.send_message(message.channel,dinnerStuffWord)

    if message.content.startswith('!dinner-storms'):
        print = 0
        webPage = 'http://www.dining.iastate.edu/menus/storms'
        page = urllib.request.urlopen(webPage)
        soup = BeautifulSoup(page, 'html.parser')
        dinnerStuff = []
        dinnerStuff = soup.findAll(True, {'class':['menu-item', 'event-header']}) #43
        for y in range (0, len(dinnerStuff)):
            dinnerStuffWord = dinnerStuff[y].text
            if "Dinner" ==  dinnerStuffWord or print == 1:
                await client.send_message(message.channel,dinnerStuffWord)
                print = 1

    

#Run locally
client.run(botSecret.Token)

#Run on Heroku. Defined under Settings->Config Vars
#client.run(environ.get('BOT_TOKEN'))
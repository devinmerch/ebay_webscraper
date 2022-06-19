from datetime import datetime
from http import client
import time
import discord
import random
from ebay_scraper import *

token = 'OTgxMzQ1MDIwOTI3OTM0NTE0.GMk668.tD0GJva3-Tqwl9qqHMvbfMjGda7TMTBUhgQII4'

client = discord.Client()

@client.event
async def on_ready():
    print('Discord bot online. Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.channel.name == 'xbox360alerts':
        if message.content.startswith('!start'):
            await message.channel.send('Working...')
            while True:
                refreshpage()                                       #Sets global variables for functions to pull from
                title1 = get_title() 
                title1 = title1.lower()                             #Formats title to lowercase string and removes $ in price
                title1 = str(title1)

                if ("skyrim" in title1) and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 70) and (price <= 300):
                        await message.channel.send('<@147857923832414209> ' + str(title1.upper()))
                        await message.channel.send('Price is: $' + str(price))
                        await message.channel.send(get_link())
                        #Shows timestamp
                        now = datetime.now()
                        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
                        await message.channel.send("Timestamp = " + str(dt_string))
                        duplicatetitle = title1
                        continue
                    continue

                if ("minecraft") in title1 and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 65) and (price <= 115):
                        await message.channel.send('<@147857923832414209> ' + str(title1.upper()))
                        await message.channel.send('Price is: $' + str(price))
                        await message.channel.send(get_link())
                        #Shows timestamp
                        now = datetime.now()
                        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
                        await message.channel.send("Timestamp = " + str(dt_string))
                        duplicatetitle = title1
                        continue
                    continue

                if ("modern warfare 2" in title1) and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 70) and (price <= 215):
                        await message.channel.send('<@147857923832414209> ' + str(title1.upper()))
                        await message.channel.send('Price is: $' + str(price))
                        await message.channel.send(get_link())
                        #Shows timestamp
                        now = datetime.now()
                        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
                        await message.channel.send("Timestamp = " + str(dt_string))
                        duplicatetitle = title1
                        continue
                    continue

                time.sleep(20)

client.run(token)
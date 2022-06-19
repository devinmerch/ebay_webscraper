from datetime import datetime
from http import client
import time
import discord
import random
from gamecube_bot_files.gamecube_url import *


token = 'OTgyMTMwNzY3Nzk2NzY4NzY4.G09Ov4.-F3w_IwqHWPaSXmlHCTy6SMt0noGMJDxaTXFsQ'

client = discord.Client()

@client.event
async def on_ready():
    print('Discord bot online. Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    duplicatetitle = "test"

    if message.author == client.user:
        return

    if message.channel.name == 'gamecubealerts':
        if message.content.startswith('!start'):
            await message.channel.send('Working...')
            while True:
                title1 = get_title()
                #Formats title to lowercase string and removes $ in price
                title1 = title1.lower()
                title1 = str(title1)

                if ("animal crossings" in title1) and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 300) and (price <= 1000):
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

                if ("wind waker") in title1 and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 300) and (price <= 500):
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

                if ("pokemon colosseum" in title1) and (title1 != duplicatetitle):
                    price = get_price()
                    price = price.replace(price[:1], '')
                    price = float(price)
                    if (price >= 205) and (price <= 500):
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

                time.sleep(60)
                refreshpage()

client.run(token)
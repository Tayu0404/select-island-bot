import discord
import random
import os

client = discord.Client()

# island edit
#"island name" : Seating capacity
islands = {
        "軍艦島" : 6,
        "屋久島" : 6,
        "小豆島" : 6,
        "種子島" : 6,
        "佐渡島" : 6
        }
#Dictionary for bot
botIslands = islands

def selectIsland() :
     selectIsland = random.choice(list(botIslands.keys()))
     botIslands[selectIsland] -= 1
     return selectIsland

def capacityCheck(selectIsland) :
    if botIslands[selectIsland] is 0:
        del botIslands[selectIsland]

@client.event
async def on_message(message):
    if message.content == '!select':
        select = selectIsland()
        await message.channel.send(select)
        capacityCheck(select)
    if message.content == '!island reset':
        botIslands = islands
client.run(os.environ['discord-token'])

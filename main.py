import discord
from discord.ext import commands
import keep_alive
from secret_key import key
import os

intents = discord.Intents.all()
shinp = commands.Bot(command_prefix="%", intents=intents)


#On ready function
@shinp.event
async def on_ready():
  channel = shinp.get_channel(824783050856071201)
  
  print('\nShinp is alive\n')
  await shinp.change_presence(activity=discord.Game(name="Shinp 2.5 on development"))

  
#On message nested if's
@shinp.event
async def on_message(message, ctx=None):
  
  if message.author == shinp.user:
    return
  if message.content.startswith("hi shinp") or message.content.startswith(
      "Hi shinp") or message.content.startswith(
        "Hello shinp") or message.content.startswith("hello shinp"):
    await message.channel.send(f"Hi {message.author.mention}!!")
    await message.channel.send("<:face:890688147640426546>")

  elif message.content.startswith("&shinp"):
    await message.channel.send("<:shinp:1011071326200549447>")

  elif message.content.startswith("Im ") or message.content.startswith("im "):
    ctx = str(message.content)
    ctx = ctx[3:]
    await message.channel.send(f"Hi {ctx}!!")
    await message.channel.send("<:shinpSNIFF:990124674539200522>")

  elif message.content.startswith("I'm ") or message.content.startswith("i'm "):
    ctx = str(message.content)
    ctx = ctx[4:]
    await message.channel.send(f"Hi {ctx}!!")
    await message.channel.send("<:shinpSNIFF:990124674539200522>")
 
  
  elif "shinp dont look" in message.content or "shinp don't look" in message.content:

    await message.reply("<:shinpback:916519047741464596>")

  elif message.content.startswith("paa") :

    await message.reply("paaaaaaaaaaaaaaaaaaaaaaaaaa")
    await message.channel.send("<a:shrimpaaaaa:844584444991242240> ")
  
  elif "love shinp" in message.content:
    await message.add_reaction('<:shinpheart:1003207547924250644>')

  elif "VV" in message.content or "vv" in message.content or "Vv" in message.content or "vV" in message.content:
    await message.channel.send("<:milostare:868376201494954044>")

  elif message.content.startswith("shinp died") or message.content.startswith(
      "shinp die"):
    await message.channel.send("<:dhinp:963178241668046878>")

  elif message.content.startswith("<:oreo:963972256416026705>"):
    await message.channel.send(
      "<:shonp:954424922992685056> <:oreo:963972256416026705>")

  elif message.content.startswith("dm shinp"):
    await message.author.send("Hi")

  elif "Dragon" in message.content or "dragon" in message.content:
    await message.add_reaction('🐉')

  elif "Shrimp" in message.content or "shrimp" in message.content:
    await message.add_reaction('<:shreal:942537112950013972>')

  elif ":3" in message.content:
    await message.add_reaction('<:face:890688147640426546>')
  
  elif "nudl" in message.content:
    await message.add_reaction('<:gau:969090982677184532>')

  elif "thistle" in message.content:
    await message.add_reaction('<:thistledrool:1011056496341159976>') 


  elif message.content.startswith("&dance") or message.content.startswith("&Dance"):
    await message.channel.send("<a:shinpnaenaeDANCE:1049493953390596107>")
    
  elif message.content.startswith("&info"):
    await message.channel.send(
      "ShinpBot under development by a Winged snek :feather: :snake:\nI accept all feedback to improve shinp"
    )

  elif message.content.startswith("&help"):
    await message.channel.send("Try to use\n&shinp\n&info")


#When a new member Joins
@shinp.event
async def on_member_join(member):
  await shinp.get_channel(824783050856071201).send(
    f"Welcome to the server {member.mention}!!! Ready to be Shinpfied?\n<:shreal:942537112950013972>"
  )


keep_alive.keep_alive()  #Keep shinp alive
try:
  shinp.run(key)
except:
  os.system("kill 1")
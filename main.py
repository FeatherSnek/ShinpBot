import discord
from discord.ext import commands
import keep_alive
from secret_key import key
import os
from Food_list import popular_foods
from pokepi import pokes
from dicti import xd,reacts
from GPT import ai

intents = discord.Intents.all()
shinp = commands.Bot(command_prefix="&",intents=intents,help_command=None)

@shinp.event
async def on_ready():
  print('\nShinp is alive\n')
  await shinp.change_presence(activity=discord.Game(name="AI Shinp available on DM"))
  """for guild in shinp.guilds:
        for channel in guild.text_channels: 
            if channel.permissions_for(guild.me).send_messages: 
                await channel.send("I'm alive!")
                return"""
              



@shinp.command()
async def help(ctx):

  embed=discord.Embed(
    title="SHINPBOT 2.5",
        description="Discord.py Bot with funny interactions and some commands about a little creature called Shinp",
        color=discord.Color.blue())
        
  
    #embed.set_author(name=ctx.author.display_name, url="https://twitter.com/RealDrewData", icon_url=ctx.author.avatar_url)
  embed.add_field(name="**help**", value="Get information about the commands", inline=False)
  embed.add_field(name="**&shinps**", value="Shinp appears on chat", inline=False)
  embed.add_field(name="**&poke (name or number of the pokemon)**", value="Shinp searchs on the pokedex and send info about the pokemon", inline=False)
  embed.add_field(name="**&hype (text)**", value="Shinp get hyped", inline=False)
  embed.add_field(name="-------------------DM ONLY:-----------------------\n||&AI (text)||", value="||Shinp answer your questions ~~(Sometimes shinp send no context answers)~~||", inline=False)
  
  embed.set_footer(text="Shinp (la criatura) belongs to nudl (https://twitter.com/long_and_soft)\nBot coded by a Feather snek 🐍")
  await ctx.send(embed=embed)
  return


@shinp.command()
@commands.dm_only()
async def AI(ctx,qstion):
  qstion = ctx.message.content[3:]
  try:
    await ctx.message.reply(ai(qstion))
    return

  except:
    await ctx.message.reply("<:shinptired:1011066241689071756>")
    return


@shinp.command()
async def shinps(message):
  
  await message.channel.send("<:shinp:1011071326200549447>")
  return

@shinp.command()
async def poke(ctx,aux):
  try:
    aux = ctx.message.content[6:]

    lst = pokes(aux)

    name = lst[0] 
    id = lst[1]
    sprite = lst[2]
    types = lst[3]
    try:
      type1,type2 = types
      typed = type1+" "+type2
    except:
      typed= types[0]

  
  
  


    embed=discord.Embed(
      title=name.upper(),
        url="https://www.pokemon.com/us/pokedex/"+name,
        description=" ",
        color=discord.Color.blue())
    embed.set_author(name="Pokedex", icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/1200px-Pok%C3%A9_Ball_icon.svg.png")

    embed.set_thumbnail(url=sprite)
    embed.add_field(name="**ID:**", value=id, inline=False)
    embed.add_field(name="**Types:**", value=typed  , inline=False)
  
    embed.set_footer(text="Data from: https://pokeapi.co/")
    await ctx.send(embed=embed)
    return 

  except:
    await ctx.reply(f"{aux} is not in my books!!")
    await ctx.send("<:shint:977320928734236692>")
    return

@shinp.command()
async def hype(ctx):

 aux = str(ctx.message.content[5:])
 await ctx.send(f"<:shinppers:977671695487877120> {aux} <:shinpoint:977671607965319220>") 
 return 


""" Esta chingadera no sirve :c
@shinp.command()
async def add(ctx):

  
  aux = str(ctx.message.content[4:])
  
  f = open("Food_list.txt","r")
    
  for words in f:
    
    if words in aux:
      await ctx.message.reply(f"{words} its already on the food list")
      return
  with open("Food_list.txt", "w") as filed:
     filed.write(aux)
     filed.close()
     await ctx.message.reply(f"{aux} added to the food list")
     return
"""

@shinp.event
async def on_command_error(ctx, exception):
    if isinstance(exception, commands.PrivateMessageOnly):
        await ctx.reply("AI shinp is available only on DM")


@shinp.event
async def on_message(message,ctx=None):
  ctx = str(message.content)
  await shinp.process_commands(message)
  
  if message.author == shinp.user:
    return

  if ctx.startswith("hi shinp") or ctx.startswith("hello shinp"):
      await message.channel.send(f"Hi {message.author.mention}!!")
      await message.channel.send("<:face:890688147640426546>")
      return

    
    

  elif ctx.startswith("i'm ") or ctx.startswith("im ") or ctx.startswith("I'm") or ctx.startswith("im") :
    ctx = ctx[3:]
    await message.channel.send(f"Hi {ctx}!!")
    await message.channel.send("<:shinpSNIFF:990124674539200522>")
    return 
  
  for keyg,msd in xd.items():
    if keyg in ctx:
      await message.channel.send(msd)
      return 
  for keyd,mgd in reacts.items():
    if keyd in ctx:
      await message.add_reaction(mgd)
      return

  for food_word in popular_foods:
    if food_word in message.content.lower():
      await message.channel.send(f"<:shonp:954424922992685056> {food_word} <:rimpr:1019722150342557728>") 
      return 


#When a new member Joins
@shinp.event
async def on_member_join(member):
  for guild in shinp.guilds:
      for channel in guild.text_channels: 
          if channel.permissions_for(guild.me).send_messages: 
              await channel.send(f"Welcome to the server {member.mention}!!! Ready to be Shinpfied?\n<:shreal:942537112950013972>") 
          return 
                 

      
      
      
keep_alive.keep_alive()  #Keep shinp alive
try:
  shinp.run(key)
except:
  os.system("kill 1")







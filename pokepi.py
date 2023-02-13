import json
import requests

def pokes(ctx):
  url = "https://pokeapi.co/api/v2/pokemon/"+ctx
  rqst = requests.get(url)
  answr = json.loads(rqst.content)

  poke = str((answr["name"]))
  id = str((answr ["id"]))
  sprite = (answr["sprites"] ["front_default"])
  type = [typ["type"]["name"] for typ in answr["types"]]
  
  poke_list = [poke,id,sprite,type]
  
  return (poke_list)

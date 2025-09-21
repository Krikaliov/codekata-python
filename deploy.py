import discord
from utils import event_handler, MsgEvent, last_channel, sep_line
from dotenv import load_dotenv
from game import GameMain
import os

if __name__ == "__main__":
  print(sep_line())
  print("Launching bot...")
  instance_intents = discord.Intents.default()
  instance_intents.members = True
  instance_intents.message_content = True

  client = discord.Client(intents=instance_intents)

  @client.event
  async def on_ready():
    data = discord.Game("Tic-Tac-Toe! Just say 'Play with me'!")
    await client.change_presence(activity = data)
    print(sep_line())
    print("Bot has started!")
    
  @client.event
  async def on_message(message):
    last_channel.setChannel(message.channel)
    await event_handler.post(MsgEvent(message.author.id, f"{message.author}", message.content))

  game:GameMain = GameMain()
  
  load_dotenv()
  loaded_key:str|None = os.getenv("CLIENT_KEY")
  if loaded_key != None:
    loaded_key_strict:str = loaded_key
    client.run(loaded_key_strict)
  else:
    print(sep_line())
    print("No secret key was found in .env")

  print(sep_line())
  print("Stopping bot...")

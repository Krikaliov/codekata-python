import discord
from utils import event_handler, MsgEvent, last_channel
from dotenv import load_dotenv
from game import GameMain
import os

if __name__ == "__main__":
  global event_handler

  print("==========================================================")
  print("Launching bot...")
  instance_intents = discord.Intents.default()
  instance_intents.members = True
  instance_intents.message_content = True

  client = discord.Client(intents=instance_intents)

  @client.event
  async def on_ready():
    data = discord.Game("Tic-Tac-Toe! Just say 'Play with me'!")
    await client.change_presence(activity = data)
    print("==========================================================")
    print("Bot has started!")
    
  @client.event
  async def on_message(message):
    last_channel.setChannel(message.channel)
    await event_handler.post(MsgEvent(message.author.id, f"{message.author}", message.content))

  game:GameMain = GameMain()
  
  load_dotenv()
  client.run(os.getenv("CLIENT_KEY"))

  print("==========================================================")
  print("Stopping bot...")

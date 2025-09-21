from datetime import datetime

def sep_line(length:int = 32) -> str:
  return length * '='

class Event:
  def __init__(self):
    self.date:str = datetime.now().isoformat()

class MsgEvent(Event):
  def __init__(self, author_id:int, author_name:str, msg:str):
    super().__init__()
    self.author_id:int = author_id
    self.author_name:str = author_name
    self.msg:str = msg
  def __str__(self) -> str:
    return self.msg

class EventHandler:
  def __init__(self):
    self.queue:list[Event] = []
    self.length:int = 0
    self.on_msg_event = self.__on_msg_event_default
    self.on_unknown_event = self.__on_unknown_event_default
  async def post(self, event:Event) -> None:
    if isinstance(event, MsgEvent):
      await self.on_msg_event(event)
    else:
      await self.on_unknown_event(event)
  async def __on_msg_event_default(self, event:MsgEvent) -> None:
    print(f"[{event.date}]",event.author_name,":",event.msg)
  async def __on_unknown_event_default(self, event:Event) -> None:
    print(f"[{event.date}]","<WARN> RECEIVED UNKNOWN EVENT")

event_handler:EventHandler = EventHandler()

class LastChannelHandler:
  def __init__(self):
    self.channel = None
  def hasChannel(self) -> bool:
    return not(self.channel is None)
  def setChannel(self, channel):
    self.channel = channel
  def getChannel(self):
    return self.channel

last_channel:LastChannelHandler = LastChannelHandler()

async def send_message(msg:str) -> None:
  global last_channel
  if last_channel.channel is None:
    return
  await last_channel.channel.send(msg)

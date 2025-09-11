from datetime import datetime

class Event:
  def __init__(self):
    self.date:str = datetime.now().isoformat()

class MsgEvent(Event):
  def __init__(self, author_id:int, author_name:str, msg:str):
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
  def post(self, event:Event) -> None:
    if event is MsgEvent:
      self.on_msg_event(event)
    else:
      self.on_unknown_event(event)
  def __on_msg_event_default(self, event:MsgEvent) -> None:
    print(f"[{event.date}]",event.author_name,":",event.message)
  def __on_unknown_event_default(self, event:Event) -> None:
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

def send_message(msg:str):
  global last_channel
  await last_channel.send(msg)

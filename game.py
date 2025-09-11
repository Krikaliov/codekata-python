from utils import event_handler, MsgEvent, Event, send_message
from grid import GameGrid

class GameMain:
  def __init__(self):
    global event_handler
    event_handler.on_msg_event = self.on_msg_event

    self.player_id:int = None
    self.grid:GameGrid = GameGrid()
    
  def on_msg_event(self, event:MsgEvent) -> None:
    # 1st state: the player id is None so the game is not playing
    if self.player_id is None:
      if event.msg.lower() == 'play with me':
        player_id = event.author_id
        await send_message(f'Hello {event.author_name}! You are the X and I am the O. You start:\n{self.grid}\nSay "B2" to put your first X on the center case of the game grid.')

    # 2nd state the player id is set so the game is playing
    if event.author_id == player_id:
      if event.msg.lower() == 'stop':
        player_id = None
        await send_message(f'Game aborted. Good bye!')
        return
      try:
        coords:tuple[int] = self.grid.coords(event.msg)
        if self.grid.player_put('X', coords):
          await send_message(f'{event.author_name} put an X at {event.msg}.')
        else:
          await send_message(f'Cannot fill this busy case! Try again.')
      except ValueError as err:
        await send_message(f'Bad statement: {err.args[0]}')
    
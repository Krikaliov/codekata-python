from utils import event_handler, MsgEvent, send_message
from grid import GameGrid

class GameMain:
  def __init__(self):
    global event_handler
    event_handler.on_msg_event = self.on_msg_event

    self.player_id:int|None = None
    self.grid:GameGrid = GameGrid()
  
  def reset(self):
    self.player_id = None
    self.grid.reset()

  def start(self, player_id:int):
    self.player_id = player_id
  
  def is_playing(self) -> bool:
    return self.player_id != None
  
  # -1 -> unsupported purpose
  # 0 -> player and computer successfully played and the game continues
  # 1 -> player tried to play on an already occupied case
  # 2 -> player played and won! the game is no longer continuing
  # 3 -> player played but computer failed to play, so the game is aborted
  # 4 -> player played but computer won. the game is aborted
  # 5 -> player played but there is no free case left, so the game is aborted about tie
  def play(self, index_grid:int) -> int:
    if self.grid.put('X', index_grid):
      if self.grid.winner() == 'X':
        self.reset()
        return 2
      elif len(self.grid.free_cases()) < 1:
        self.reset()
        return 5
      else:
        index_grid_bot:int = self.__play(index_grid)
        if not(self.grid.put('O', index_grid_bot)):
          self.reset()
          return 3
        elif self.grid.winner() == 'O':
          self.reset()
          return 4
        else:
          return 0
    else:
      return 1
    
  async def on_msg_event(self, event:MsgEvent) -> None:
    # 1st state: the player id is None so the game is not playing
    if self.player_id is None:
      if event.msg.lower() == 'play with me':
        self.player_id = event.author_id
        await send_message(f'Hello {event.author_name}! You are the X and I am the O. You start:\n{self.grid}\nSay "B2" to put your first X on the center case of the game grid.')
    # 2nd state: the player id is set so the game is playing
    elif event.author_id == self.player_id:
      if event.msg.lower() == 'stop':
        self.reset()
        await send_message(f'Game aborted. Good bye!')
      elif event.msg.lower() == 'show':
        await send_message(f'You currently turn on this:\n{self.grid}')
      else:
        try:
          index_grid:int = self.grid.coords(event.msg)
          status:int = self.play(index_grid)
          if status == 0:
            await send_message(f'I played too. Here is the grid:{self.grid}')
          elif status == 1:
            await send_message(f'Cannot fill this busy case! Try again.')
          elif status == 2:
            await send_message(f'You win! The game ends:{self.grid}')
          elif status == 3:
            await send_message('Something went wrong with me, I cannot play this game, I give up...')
          elif status == 4:
            await send_message(f'I played too. Here is the grid:{self.grid}You lose... The game ends.')
          elif status == 5:
            await send_message(f'Tie! The game ends:{self.grid}')
          else:
            self.reset()
            await send_message('Something went wrong, the game is aborted.')
        except ValueError as err:
          await send_message(f'Bad statement: {err.args[0]}\nTry again.') 
    # 3rd state: another one attempts to launch a game while someone is already playing with me
    else:
      if event.msg.lower() == 'play with me':
        await send_message(f'I am already currently playing with player id {self.player_id}')
      elif event.msg.lower() == 'show':
        await send_message(f'Player currently turns on this:\n{self.grid}')
  
  def __play(self, last_player_move:int) -> int:
    free_cases:list[int] = self.grid.free_cases()
    return free_cases[1] if len(free_cases) > 1 else free_cases[0]

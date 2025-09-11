from utils import event_handler, MsgEvent, Event, send_message
from grid import GameGrid

class GameMain:
  def __init__(self):
    global event_handler
    event_handler.on_msg_event = self.on_msg_event

    self.player_id:int = None
    self.grid:GameGrid = GameGrid()
  
  def reset(self):
    self.player_id:int = None
    self.grid.reset()
    
  async def on_msg_event(self, event:MsgEvent) -> None:
    # 1st state: the player id is None so the game is not playing
    if self.player_id is None:
      if event.msg.lower() == 'play with me':
        self.player_id = event.author_id
        await send_message(f'Hello {event.author_name}! You are the X and I am the O. You start:\n{self.grid}\nSay "B2" to put your first X on the center case of the game grid.')

    # 2nd state the player id is set so the game is playing
    elif event.author_id == self.player_id:
      if event.msg.lower() == 'stop':
        self.reset()
        await send_message(f'Game aborted. Good bye!')
      elif event.msg.lower() == 'show':
        await send_message(f'You currently turn on this:\n{self.grid}')
      else:
        try:
          coords:tuple[int] = self.grid.coords(event.msg)
          if self.grid.player_put('X', coords):
            await send_message(f'{event.author_name} put an X at {event.msg}.')
            if self.grid.winner() == 'X':
              self.reset()
              await send_message('You win! The game ends.')
            elif len(self.grid.free_cases()) < 1:
              self.reset()
              await send_message('Tie! The game ends.')
            else:
              bot_coords:tuple[int] = self.__play(coords)
              if not(self.grid.player_put('O', bot_coords)):
                raise ValueError("Bot failed to play correctly!")
              await send_message(f'I put an O at {self.grid.coords_text(bot_coords)}. Here is the grid:{self.grid}')
              if self.grid.winner() == 'O':
                self.reset()
                await send_message('You lose... The game ends.')
              else:
                await send_message('You turn!')
          else:
            await send_message(f'Cannot fill this busy case! Try again.')
        except ValueError as err:
          self.reset()
          await send_message(f'Bad statement: {err.args[0]}\nThe game is aborted.')
          raise
        
    # 3rd state another one attempts to launch a game while someone is already playing with me
    else:
      if event.msg.lower() == 'play with me':
        await send_message(f'I am already currently playing with player id {self.player_id}')
      elif event.msg.lower() == 'show':
        await send_message(f'Player currently turns on this:\n{self.grid}')
  
  def __play(self, last_player_move:tuple[int]) -> None:
    free_cases:list[tuple[int]] = self.grid.free_cases()
    return free_cases[0]

from game import GameMain
from utils import sep_line

class GameInstance:
  def __init__(self, start:int, a:int, b:int, c:int):
    self.start:int = start
    self.a:int = a
    self.b:int = b
    self.c:int = c
    self.turn:int = 0
    self.status:int = -1 # when -1, nothing just started yet

  def compute_next_move(self, rel_move:int, free_moves:list[int]) -> int:
    moved:int = 0
    cur:int = self.start
    while rel_move > 0 and moved < 18:
      cur, rel_move, moved = (cur + 1) % 9, rel_move - 1, moved + 1
      while not(cur in free_moves):
        cur, moved = (cur + 1) % 9, moved + 1
    return 9 if moved > 17 else cur
  
  def play_a_turn(self, free_moves:list[int]) -> int:
    self.turn += 1
    if self.turn == 1:
      return self.compute_next_move(self.a, free_moves)
    elif self.turn == 2:
      return self.compute_next_move(self.b, free_moves)
    elif self.turn == 3:
      return self.compute_next_move(self.c, free_moves)
    else:
      return free_moves[0]
  
  def play(self, game_main:GameMain):
    game_main.start(1234)
    try:
      self.status = game_main.play(self.start)
      while self.status < 1:
        self.status = game_main.play(self.play_a_turn(game_main.grid.free_cases()))
    except IndexError as err:
      print(f"Something went wrong while testing: {err}\nThis was certainly caused by wrong mocked player move.")
      game_main.reset()

class Test:
  def __init__(self):
    self.victory_count:int = 0
    self.defeat_count:int = 0
    self.fail_count:int = 0
    self.tie_count:int = 0
    self.unhandled_events:int = 0
  
  def update(self, status:int):
    if status == 2:
      self.defeat_count += 1
    elif status == 3:
      self.fail_count += 1
    elif status == 4:
      self.victory_count += 1
    elif status == 5:
      self.tie_count += 1
    else:
      self.unhandled_events += 1
  
  def __str__(self) -> str:
    information:str = f" - Victory count: {self.victory_count}\n"
    information += f" - Defeat count: {self.defeat_count}\n"
    information += f" - Tie count: {self.tie_count}\n"
    information += f" - Fail count: {self.fail_count}\n"
    information += f" - Unhandled events that require debugging: {self.unhandled_events}\n"
    return information

if __name__ == "__main__":
  test_instance:Test = Test()
  game_main:GameMain = GameMain()
  all_games:list[GameInstance] = [GameInstance(s,a,b,c) for s in range(9) for a in range(1,8) for b in range(1,6) for c in range(1,4)]
  number_games:int = len(all_games)
  print(sep_line(64))
  print(f"{len(all_games)} different games are going to be played to test your game!")
  print(sep_line(64))
  for i in range(number_games):
    all_games[i].play(game_main)
    test_instance.update(all_games[i].status)
    print(f'\r{i}/{number_games} game played...', end='')
  print(f'\rAll games were played! Results of your bot:\n{test_instance}', end='')

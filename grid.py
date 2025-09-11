class GameGrid:
  def __init__(self):
    self.grid:list[str] = 9 * [' ']
  
  def reset(self) -> None:
    self.grid = 9 * [' ']
  
  def player_put(self, player_display:str, coords:tuple[int]) -> bool:
    index:int = 3 * coords[0] + coords[1]
    if self.grid[index] != ' ' or player_display == ' ':
      return False
    self.grid[index] = player_display
    return True

  def coords(self, coords_text:str) -> tuple[int]:
    if len(coords_text) == 2:
      y:int = 0
      if coords_text[0] == 'B':
        y = 1
      elif coords_text[0] == 'C':
        y = 2
      else:
        raise ValueError("Wrong column letter")
      x:int = 0
      if coords_text[1] == '2':
        y = 1
      elif coords_text[1] == '3':
        y = 2
      else:
        raise ValueError("Wrong row number")
    else:
      raise ValueError("Wrong argument")
  
  def __str__(self) -> str:
    display:str = ' |A|B|C|\n'
    display += '-|-|-|-|\n'
    for i in range(3):
      row:list = self.grid[i*3 : i*3+3]
      display += f'{i+1}|{"|".join(row)}|\n'
      display += '-|-|-|-|\n'
    return display
  
  def winner(self) -> str:
    if self.grid[0] == self.grid[1] and self.grid[1] == self.grid[2]:
      if self.grid[0] != ' ':
        return self.grid[0] # Upper row winner
    if self.grid[3] == self.grid[4] and self.grid[4] == self.grid[5]:
      if self.grid[3] != ' ':
        return self.grid[3] # MIddle row winner
    if self.grid[6] == self.grid[7] and self.grid[7] == self.grid[8]:
      if self.grid[6] != ' ':
        return self.grid[6] # Low row winner
    if self.grid[0] == self.grid[3] and self.grid[3] == self.grid[6]:
      if self.grid[0] != ' ':
        return self.grid[0] # Left column winner
    if self.grid[1] == self.grid[4] and self.grid[4] == self.grid[7]:
      if self.grid[1] != ' ':
        return self.grid[1] # Middle column winner
    if self.grid[2] == self.grid[5] and self.grid[5] == self.grid[8]:
      if self.grid[2] != ' ':
        return self.grid[2] # Right column winner
    if self.grid[0] == self.grid[4] and self.grid[4] == self.grid[8]:
      if self.grid[0] != ' ':
        return self.grid[0] # Anti-slash winner
    if self.grid[2] == self.grid[4] and self.grid[4] == self.grid[6]:
      if self.grid[2] != ' ':
        return self.grid[2] # Slash winner

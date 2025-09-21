class GameGrid:
  def __init__(self):
    self.grid:list[str] = 9 * [' ']
  
  def reset(self) -> None:
    self.grid = 9 * [' ']
  
  def put(self, player_display:str, index_grid:int) -> bool:
    if self.grid[index_grid] != ' ' or player_display == ' ':
      return False
    self.grid[index_grid] = player_display
    return True

  def coords(self, coords_text:str) -> int:
    if len(coords_text) == 2:
      y:int = 0
      if coords_text[0] == 'B':
        y = 1
      elif coords_text[0] == 'C':
        y = 2
      elif coords_text[0] != 'A':
        raise ValueError("Wrong column letter")
      x:int = 0
      if coords_text[1] == '2':
        x = 1
      elif coords_text[1] == '3':
        x = 2
      elif coords_text[1] != '1':
        raise ValueError("Wrong row number")
      return 3*x+y
    else:
      raise ValueError("Wrong argument")
  
  def coords_text(self, i:int) -> str:
    c:tuple[int, int] = (i // 3, i % 3)
    return f'{"A" if c[1]==0 else "B" if c[1]==1 else "C"}{"1" if c[0]==0 else "2" if c[0]==1 else "3"}'
  
  def __str__(self) -> str:
    display:str = '```\n'
    display += ' |A|B|C|\n'
    display += '-|-|-|-|\n'
    for i in range(3):
      row:list = self.grid[i*3 : i*3+3]
      display += f'{i+1}|{"|".join(row)}|\n'
      display += '-|-|-|-|\n'
    display += '```\n'
    return display
  
  def winner(self) -> str:
    if self.grid[0] == self.grid[1] and self.grid[1] == self.grid[2]:
      if self.grid[0] != ' ':
        return self.grid[0] # Upper row winner
    if self.grid[3] == self.grid[4] and self.grid[4] == self.grid[5]:
      if self.grid[3] != ' ':
        return self.grid[3] # Middle row winner
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
    return ' '
    
  def free_cases(self) -> list[int]:
    return [i for i in range(len(self.grid)) if self.grid[i]==' ']

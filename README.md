# Tic-tac-toe on Discord

## Codekata Lore

|       | A | B | C |
| ----- | - | - | - |
| **1** | X |   |   |
| **2** | O | O | O |
| **3** |   | X |   |

Here is a tic-tac-toe game coded in Python and deployable on Discord via a discord bot (by given your bot's private client key in `.env`, see more details below in the section ***Deploy***). The program permits any member to launch a game of tic-tac-toe against the machine. The player begins and draws `X` on the grid, while the computer is playing by drawing `O` on the grid. However, the programer is so bad in this game that he did not succeed to code a good strategy for the bot. The current strategy for the bot playing is choosing the second free box of the grid when reading the grid from top-left to bottom-right, which is the mean worst strategy ever found.

## What to do ?

### Goal

The goal of this project is to code a good strategy for the bot playing. The module `game.py` contains a class named `GameMain` with a private method entitled `__play` which takes the last player move (coordinate where the player put its `X`) and compute its next move against the player before returning it (as an integer representing the index of the game grid, see below).

### Editable methods

You can modify the following methods:

 - `GameMain.__play`: as discussed higher, this is the method **you shall update** to make the bot stronger and win a maximum of games from the `tests.py` executable module. This method takes the index of the game grid as argument played by the opposite player, a number between 0 and 8 that represents a box of the grid, and returns the next bot move as integer, also a number between 0 and 8 that represents a box of the grid:

|   |   |   |
| - | - | - |
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

**DO NOT MODIFY `GameMain.play` BUT ONLY `GameMain.__play` !!**

You can also add extra attributes or private methods to `GameMain` class but do not modify or delete any other method or attribute from `GameMain`.

Among sources, you can only update `game.py`, any other module must remain the same!

### Testing

When you think your job is done, launch `tests.py` with your instance of Python 3.12+.

### Deploying

When you are ready to deploy your code to Discord, launch `deploy.py` with your instance of Python 3.12+. Be sure you added the file `.env` with your secret client key as following:

```yaml
CLIENT_KEY=0
```

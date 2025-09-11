# Tic-tac-toe on Discord

## Codekata Lore

Here is a tic-tac-toe game coded in Python and deployable on Discord via a discord bot (by given your bot's private client key in `deploy.py`). The program permits any member to launch a game of tic-tac-toe against the machine. The player begins and draws `X` on the grid, while the computer is playing by drawing `O` on the grid. However, the programer is so bad in this game that he did not succeed to code a good strategy for the bot. The current strategy for the bot playing is choosing the first free case when reading the grid from top-left to bottom-right, which is the mean worst strategy ever found in the history of humanity.

## What to do ?

### Goal

The goal of this project is to code a good strategy for the bot playing. The module `game.py` contains a class named `GameMain` with a private method entitled `__play` which takes the last player move (coordinates where the player put its `X`) and compute its next move against the player before returning it (as a tuple of integers `(x,y)`). The `x` coordinate represents the line (index 0 to 2) and the `y` coordinate represents the column (index 0 to 2).

### Editable methods

You can modify the following methods:
 - `GameMain.on_msg_event`: takes an event message with author name, author id and name and react to this event. If the message is `play with me` whereas no game is running (`GameMain.player_id is None`), then launches the game. If a game is running (with a `GameMain.player_id` not being None) and the message is coordinates of the grid (e.g `B2` or `C1`), then takes account of the player move and check whether or not they win, or makes the bot playing, etc. You will find more useful interactions in this method.
 - `GameMain.__play`: as discussed higher, this is the method **you shall update** to make the bot stronger and pass all tests from `tests.py` executable module.

You can also add extra attributes or private methods to `GameMain` class but do not modify the initialization routine or the `reset` function and do not delete any other method or attribute from `GameMain`.

Among sources, you can only update `game.py`, any other module must remain the same!

### Testing

When you think your job is done, launch `tests.py` with your instance of Python 3.12.

### Deploying

When you are ready to deploy your code to the Discord bot, launch `deploy.py` with your instance of Python 3.12.

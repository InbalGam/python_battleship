# Python Battleship
Battleship game written in Python

Signs-

Empty cell: ' '

Positioned ship: 'o'

Bombed cell: 'x'

Bombed cell but there wasn't any ships: '-'


First the program asks if the player wants to load a saved game or start a new one,
if the player chooses a new game it asks for the player to choose one of two options of the game.

The program asks each player, individually, to position his ships, representing them with 'o' in each cell.
It also shows the player the new board with the positioned ship before entering a new ship.
The entering of the cells is like this- A0 A4.
Before another player is about to position his ships, the program has a 3 seconds delay and it also clears the screen.

When the two players set their board games, the program shows the first player his own board and a clean board representing the other player's board. Then player one chooses where he wants to hit, if he succeded that cell fills with 'x' if not with '-' and the second player will see the damage to his ships in his turn.
This is continued untill there is a winner or the players choose  to save the game (the game is saved in json format) and exit (they can load it again and continue playing from the same point).


# Quiet Dominator
## Overview
Welcome to Project Quiet Dominator which will be referred to as QD (pronounced 'cutie') henceforth for the sake of conciseness.

QD is an implementation of machine learning in a tic-tac-toe game. The core of this program is a classification algorithm that utilizes a decision tree to determine the computer's next move. It has the capacity to be trained by explicitly feeding it data via a txt file or simply by simply playing the game.
## Documentation
### How it Works
#### A game
Internally, the program represents a game with two arrays containing the moves of each player. Each square of the tic-tac-toe board is assigned a number of 1 through 9, starting from the top left square and ending at the bottom right. The arrays representing the game hold the numbers corresponding to which squares the players have occupied, in the order that the players have played them.
#### The Decision Tree
QD employs a decision tree classification algorithm. When the computer has to make a decision, it sends to the tree two arrays denoting who has occupied which squares. These arrays contain all the information needed to determine the next move. There are three splits (attributes) in the tree structure. The first attribute is which player (com or user) went first. The second attribute is which spaces the computer has occupied. The third attribute is which spaces the player has occupied. After these three traversals down the tree, a decision node is reached which contains the computer's next move.
#### Training
The initial tree is built using supervised machine learning. The program takes a txt file within which each line is a different instance of a game where the moves of each player separated by a vertical bar, |. For example, a game that looks like this:
<pre>
X | O | 
O | X | 
X | O | X
</pre>
Player X has won on the diagonal and this game would be represented, on a single line, by: 1,7,9,6|2,4,8. The string of numbers before the vertical bar represents player X's moves and the string of numbers after represents player O's moves.
The training module takes an instance of a game and steps through it one move at a time, adding attribute nodes to the tree.

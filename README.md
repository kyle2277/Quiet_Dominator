# Quiet Dominator
## Overview
Welcome to Project Quiet Dominator which will be referred to as QD (pronounced 'cutie') henceforth for the sake of conciseness.

QD is an implementation of machine learning in a tic-tac-toe game. The core of this program is a classification algorithm that utilizes a decision tree to determine the computer's next move. It has the capacity to be trained by explicitly feeding it data via a txt file or simply by playing the game.
## Documentation
### How it Works
#### The Decision Tree
QD employs a decision tree classification algorithm. When the computer has to make a decision, it sends to the tree two arrays denoting who has occupied which squares. These arrays contain all the information needed to determine the next move. There are three splits (attributes) in the tree structure. The first attribute is which player (com or user) went first. The second attribute is which spaces the computer has occupied. The third attribute is which spaces the player has occupied. After these three traversals down the tree, a decision node is reached which contains the computer's next move.
#### A game
Internally, the program represents a game with two arrays containing the moves of each player. Each square of the tic-tac-toe board is assigned a number of 1 through 9:
_____________
|   |   |   |
| 1 | 2 | 3 |
|___|___|___|
|   |   |   |
| 4 | 5 | 6 |
|___|___|___|
|   |   |   |
| 7 | 8 | 9 |
|___|___|___|
 
#### Training
The initial tree is built using supervised machine learning. The program takes a txt file within which each line represents a game and the moves of each player are given, separated by a vertical bar, |. For example, a game would be represented by, on a single line, "1

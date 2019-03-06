# Quiet Dominator
## Overview
Welcome to Project Quiet Dominator which will be referred to as QD (pronounced 'cutie') henceforth for the sake of conciseness.

QD is an implementation of machine learning in a tic-tac-toe game. The core of this program is a classification algorithm that utilizes a decision tree to determine the computer's next move. It has the capacity to be trained by explicitly feeding it data via a txt file or simply by playing the game.
## Documentation
### How it Works
#### The Decision Tree
QD employs a decision tree classification algorithm. When the computer has to make a decision, it sends to the tree two arrays denoting who has occupied which squares. These arrays contain all the information needed to determine the next move. There are three splits (attributes) in the tree structure. The first attribute is which player (com or user) went first. The second attribute is which spaces the computer has occupied. The third attribute is which spaces the player has occupied. After these three traversals down the tree, a decision node is reached which contains the computer's next move.
#### Training
The tree is designed to support 

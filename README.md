<img src=https://github.com/kyle2277/Quiet_Dominator/blob/master/QD_logo.png width="300" height="200"></img>
___
# Quiet Dominator
## Overview
Welcome to Project Quiet Dominator which will be referred to as QD (pronounced 'cutie') henceforth for the sake of conciseness.

QD is an implementation of machine learning in a tic-tac-toe game. The core of this program is a classification algorithm that utilizes a decision tree to determine the computer's next move. It has the capacity to be trained by explicitly feeding it data via a txt file or simply by simply playing the game.
## Documentation
### Dependencies
* Python 3.5
### How it Works
#### A game
Internally, the program represents a game with two arrays containing the moves of each player. Each square of the tic-tac-toe board is assigned a number of 1 through 9, starting from the top left square and ending at the bottom right. The arrays representing the game hold the numbers corresponding to which squares the players have occupied, in the order that the players have played them.
#### The Decision Tree
QD employs a decision tree classification algorithm. When the computer has to make a decision, it sends to the tree two arrays denoting who has occupied which squares. These arrays contain all the information needed to determine the next move. There are three splits (attributes) in the tree structure. The first attribute is which player (com or user) went first. The second attribute is which spaces the computer has occupied. The third attribute is which spaces the player has occupied. After these three traversals down the tree, a decision node is reached which contains the computer's next move.
#### Training
The initial tree is built using supervised machine learning. The program takes a txt file within which each line is a different instance of a game where the moves of each player separated by a vertical bar, |. For example, for a game that traditionally looks like this:
<pre>
X | O | 
O | X | 
X | O | X
</pre>
Player X (com) has won on the diagonal and this game would be represented, on a single line, by: 1,7,9,6|2,4,8. The string of numbers before the vertical bar represents the computer's moves and the string of numbers after represents the player's moves. The training module takes an instance of a game and steps through it one move at a time, adding attribute nodes to the tree. Adding the game above to an empty tree would look like the following:
<pre>
Did com go first or second?                [root]
                                      ________|____________________
                                      |                           |
                                   [first]                     [second]
                      ________________|________________
                      |          |         |          |
Com moves?         [None]       [1]      [1,7]     [1,7,9]
                      |          |         |          |
User moves?        [None]       [2]      [2,4]     [2,4,8]
                      |          |         |          |
Decision node        [1]        [7]       [9]        [6]
</pre>
QD trains itself on the fly as well. Whenever a game with a human player is finished the result is added to the tree.
### Aside
The QD decision tree algorithm is fundamentally flawed. While this program is technically an implementation of machine learning, it is no more learning than memorization of data. The way the tree is currently set up, the attributes at which branches are split are discrete and highly specific when they should be categorical. This means that the only time that QD will perform optimally is with a perfectly fit tree that contains all possible permutations of moves. This is somewhat antithetical to machine learning theory, of which a main goal is to prevent overfitting, not make machines that only work with overfit models. Furthermore, the occupied squares are represented by numbers, meaning the tree can only see the board in one orientation.\
An improved algorithm would look not at the numbered squares occupied by each player, but at the squares occupied in realation to the game board as a whole. This way, the issue of fixed orientation would be eliminated and the tree could use patterns to choose the next move instead of a discrete attribute such as squares occupied. The decision tree would then be split at the points of highest information gain between patterns, resulting in an algorithm that categorizes data instead of matching it to pre-defined values.

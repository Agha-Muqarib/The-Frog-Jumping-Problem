# The-Frog-Jumping-Problem

Frog Jumping Problem is a python program that prints complete state space grap of the 'Frog Problem'. Also, it counts the number of states while generating them 

## Representation:

* Each state of the game will be represented in the form of a 7-char string, say 1110222 where:  1 represents green frog 2 represents brown frog 0 represents empty block. 
* The root node of the tree will be 111022.
* The goal node is 2220111

## Output:
 
 The output looks like this:
 
 ![Output](https://github.com/Agha-Muqarib/The-Frog-Jumping-Problem/blob/main/Images/Output.png)
 
 ## Changes:
 
 If you want to change the number of frogs to 2 or 4, make the following changes to driver code:
 
 * When number of frogs = 2 (of each kind)
   - ```starting_position = '11022'```
   - ```move_sequence = '1 2 2 1 1  2 2 1'```
 
 * When number of frogs = 4 (of each kind)
   - ```starting_position = '1110222'```
   - ```move_sequence = '1 2 2 1 1 1 2 2 2 1 1 1 2 2 1'```

 
 

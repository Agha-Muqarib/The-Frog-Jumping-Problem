# The-Frog-Jumping-Problem:

The Frog Jumping Problem is a python program that prints complete state space graph of the 'Frog Problem'. Also, it counts the number of states while generating them.

## Representation:

* Each state of the game will be represented in the form of a 7-char string, say 1110222 where:  1 represents green frog 2 represents brown frog 0 represents empty block. 
* The root node of the tree will be 111022.
* The goal node is 2220111.

## Output:
 
 The output looks like this:
 
 ![Output](https://github.com/Agha-Muqarib/The-Frog-Jumping-Problem/blob/main/Images/Output.png)
 
 ## Changes:
 
 If you want to change the number of frogs to 2, 3 or 4, make the following changes to driver code:
 
 * When number of frogs = 2 (of each kind)
   - ```starting_position = '11022'```
   - ```move_sequence = '1 2 2 1 1  2 2 1'```
   
             {is equal to the code 12-2-21}
   
 * When number of frogs = 3 (of each kind)
   - ```starting_position = '1110222'```
   - ```move_sequence = '1 2 2 1 1 1 2 2 2 1 1 1 2 2'```
        
             {is equal to the code 123-3-321}
   
 
 * When number of frogs = 4 (of each kind)
   - ```starting_position = '1110222'```
   - ```move_sequence = '1 2 2 1 1 1 2 2 2 2 1 1 1 1 2 2 2 2 1 1 1 2 2 1'```

             {is equal to the code 1234-4-4321}

## Relevant References:

For a better understanding, follow these resources:

* Reference to Case Study:
        [http://tantalus.questu.ca/~rhoshino/files/frogjumping.pdf](http://tantalus.questu.ca/~rhoshino/files/frogjumping.pdf) 
  
* Reference to Notebook/Code: 
        [http://www.bit.ly/CallystoFrog](http://www.bit.ly/CallystoFrog)
  
* Reference to Video: 
        [https://www.youtube.com/watch?v=R8wkhae4Pvg](https://www.youtube.com/watch?v=R8wkhae4Pvg)
 
 

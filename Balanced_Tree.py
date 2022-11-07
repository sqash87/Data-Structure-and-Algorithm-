#Starategies:

#define a recursive height function which will calculate the height of the each passed node.
#define another recursive function which will keep calling the height function with the root.left and root.right
#as long as the max(left_height,left_height)+1 is less than 1. 

#defining a class to create a node 
from tkinter.messagebox import RETRY
from tkinter.tix import Tree


class Node:
    def __init__(root, key):
        root.val= key
        root.right= None
        root.left= None


# defining a function is_balanced(root) which will call the calc_height function as 
# long as (max(left_height, right_heght))+1 is less than 1.
# While calc_height() will calculate the height of the passing root node. 

def is_balanced(root):
    if root is None:
        return True
    else:
        if abs(calc_height(root))<=1 and is_balanced(root.left) and is_balanced(root.right):
            return True
        else:
            return False 


# defining a function that will calculate height of the node passed into it by the is_balanced()
def calc_height(root):
    if root is None:
        return 0
    left_height = calc_height(root.left)
    right_heght = calc_height(root.right)

    return (max(left_height, right_heght))+1


# program starts interpreting from here. 
root = Node(10) 
root.left = Node(12)
root.right = Node(13)
root.left.left = Node(15)
root.left.right = Node(16)
root.left.left.right= Node(33)
root.right.right = Node(17)
root.right.right.left = Node(21)
root.right.right.right = Node(25)
root.right.right.left.left = Node(50)
root.right.right.left.right = Node(51)

if is_balanced(root):
    print("Tree is balanced")
else:
    print("Tree is not balanced")
		

#Approach: # Traverse down either the left or right of the tree 
           # Calculate the left_height and right_height by returning -1 when the parent node doesn't have any children.
           # and then eventually return the max(left_height, right_height)+1 to the relative parent node.


#Creating an node

class Tree():
    def __init__(root, key):
        root.left= None
        root.right= None
        root.val=key
	

#calculatig the left and right height of the node.    

def Calc_Height(root):
    if root is None:
        return -1
    
    left_height=Calc_Height(root.left)
        
    right_height=Calc_Height(root.right)

    return max(left_height, right_height)+1
    

tree = Tree(10)
tree.left= Tree(12)
tree.right= Tree(13)
tree.left.left= Tree(15)
tree.left.left.right= Tree(33)
tree.left.right= Tree(16)
tree.right.right= Tree(17)
tree.right.right.left= Tree(21)
tree.right.right.right= Tree(25)
tree.right.right.left.left= Tree(50)
tree.right.right.left.right= Tree(51)


print("The height of the tree is:", Calc_Height(tree))

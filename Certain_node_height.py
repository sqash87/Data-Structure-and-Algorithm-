
#Find a certain node and then calculate its height
class Tree():
    #constructor 
    def __init__(self, key):
       self.left= None
       self.right= None
       self.val= key

       
#Finds the right node
def Find_Node(self, val1):  
    if self:
        if self.val== val1:
            return self
    else:
        return 
    left = Find_Node(self.left,val1)
    
    if left:
        return left
    right= Find_Node(self.right,val1)
    return right


#calculate the height of that certian node.
def Calc_Height(root):
    
    if root is None:
        return -1
    
    left_height=Calc_Height(root.left)
        
    right_height=Calc_Height(root.right)

    return max(left_height, right_height)+1

     
# Find the height of a certain node:
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

#This function gives me the address of node 10.
root= Find_Node(tree,33)

#This function calculates the height of that certain node.
print("The height of the tree is:", Calc_Height(root))
    
    
    



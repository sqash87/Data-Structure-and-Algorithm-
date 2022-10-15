
# Implementing a doubly linked list with Adding and Deleting certain nodes and 
# travsersing forward and backward

#defining a class that will create a node.
from ast import Break
from email import header
from email.quoprimime import header_check


class Node():
    def __init__(self, val):
        #Node pointers
        self.Next= None 
        self.Prev= None 
        self.data= val
    

class Create_List:

    #function that defines pointers
    def __init__(self):
        self.Headpointer= None
        self.Tailpointer= None
    #function that add nodes one after another
    def Add_Nodes(self, val):
        
        #For the very first Node.
        if self.Headpointer==None:
            newnode= Node(val)
            self.Headpointer= newnode
        
        else:
            head_iterator= self.Headpointer
            while head_iterator.Next!=None:
                head_iterator= head_iterator.Next
            if head_iterator.Next == None:
                newnode= Node(val)
                newnode.Prev= head_iterator
                head_iterator.Next=newnode
                self.Tailpointer= newnode
    
    # Function that adds a node after a ctertain node:


    # Function that adds a node after a ctertain node:
    def Add_Node_after(self,insert_val, node_val):
        Head_iterator= self.Headpointer
        
        while Head_iterator!=None:
            #if the target value is the last node
            if Head_iterator.data==node_val and self.Tailpointer.data==node_val:
                newnode= Node(insert_val)
                Head_iterator.Next= newnode
                newnode.Prev= Head_iterator
                self.Tailpointer= newnode
                break
            #if the target value is any other  node
            elif Head_iterator.data==node_val and Head_iterator!=self.Tailpointer:
                newnode= Node(insert_val)
                newnode.Next= Head_iterator.Next
                Head_iterator.Next.Prev= newnode
                newnode.Prev= Head_iterator
                Head_iterator.Next=newnode
                break       
            else:
                Head_iterator= Head_iterator.Next
    
    # Function that adds a node before a ctertain node:
    def Add_Node_Bf(self, insert_val, target_val):      
        Head_Iterator= self.Headpointer
        # if the target vlaue is the First Node:
        while Head_Iterator.Next!=None:
            if Head_Iterator.data==target_val and Head_Iterator.data==self.Headpointer.data:
                newnode= Node(insert_val)
                newnode.Next= Head_Iterator
                Head_Iterator.Prev=newnode
                self.Headpointer= newnode
                break
            
            elif Head_Iterator.Next.data==target_val and Head_Iterator.data!=self.Headpointer.data:
                newnode= Node(insert_val)
                #link them right to left       
                newnode.Next= Head_Iterator.Next
                Head_Iterator.Next.Prev= newnode
                newnode.Prev= Head_Iterator
                Head_Iterator.Next=newnode
                break
            
            else:
                Head_Iterator= Head_Iterator.Next

       
    #Delete first or last node   
    def Delet_Node(self, node_val):

        #if the deleting node is the first node
        if  self.Headpointer.data==node_val:
            self.Headpointer= self.Headpointer.Next
            self.Headpointer.Prev= None
            
        #if deleting node is the last node
        elif self.Tailpointer.data== node_val:
            self.Tailpointer= self.Tailpointer.Prev
            self.Tailpointer.Next= None
        
        #Deleting any nodes besides first or last
        else:
            Head_ptr= self.Headpointer
            while Head_ptr!=None:
                if Head_ptr.data==node_val:
                    Head_ptr.Next.Prev= Head_ptr.Prev
                    Head_ptr.Prev.Next= Head_ptr.Next
                    Head_ptr.Next= None
                    Head_ptr.Prev= None
                    break

                else:
                    Head_ptr=Head_ptr.Next

    #Travser nodes left to right
    def Traverse_Nodes(self):
        Head_iterator= self.Headpointer
        while Head_iterator!=None:
            print("Left->Right order:",Head_iterator.data)
            Head_iterator=Head_iterator.Next
        
    
    #Traverse nodes right to left
    def Reverse_Traverse_Nodes(self):
        Tail_ptr= self.Tailpointer
        while Tail_ptr!=None:
            print("Right->Left:",Tail_ptr.data)
            Tail_ptr= Tail_ptr.Prev
        

liknked_list= Create_List()

liknked_list.Add_Nodes(10)
liknked_list.Add_Nodes(11)
liknked_list.Add_Nodes(12)
liknked_list.Add_Nodes(13)
liknked_list.Add_Nodes(14)

liknked_list.Add_Node_after(100,14)
liknked_list.Add_Node_after(200,12)

liknked_list.Add_Node_Bf(500,10)
liknked_list.Add_Node_Bf(900,100)

liknked_list.Add_Node_after(1500,900)


liknked_list.Delet_Node(900)

liknked_list.Reverse_Traverse_Nodes()

liknked_list.Traverse_Nodes()



                   





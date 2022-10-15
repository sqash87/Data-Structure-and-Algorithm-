
#1: Implementing stack, push(), pop(), min() that has 0(1) time complexity
#1) Stack allows constant add and remive elements 
#2) Stacks are used in recursive algorithm.


from ast import Delete


class Stack():
    #When an object is crated, this constructor will create an empty list.
    def __init__(self):
        self.list=[]
        self.min_val_list=[]
        

    #This function will add element to the stack
    def push(self, elem):
        self.list.append(elem)
        
        if len(self.list)<2:
            self.min_val_list.append(self.list[0])
        
        #Addig element to the min_Val_list when the recently added element in the stack 
        # is smaller than the recenly added element in min_val_list.
        
        else:
            if self.list[-1]<self.min_val_list[-1]:
                self.min_val_list.append(self.list[-1])

        
    #This function will pop the last element
    def pop(self):
         
         # if the last element of the stack is same as the last element of the min_val_list,
         # delete the last elem from the min_val_list.
         if self.list[-1] == self.min_val_list[-1]:
            del self.min_val_list[-1]
        
         #pop the stack
         return self.list.pop()
    
    def min(self):
        return self.min_val_list[-1]



stack= Stack()

stack.push(20)
stack.push(25)
stack.push(30)
stack.push(15)
stack.push(33)
stack.push(40)

stack.push(70)
stack.push(55)
stack.push(12)
stack.push(10)

stack.pop()
stack.pop()
stack.pop()


print(stack.min())




#2: implemneting Queue with Doubly linked list.
#Headpointer points at the newnode while tailpointer points at the first node.
#As we pop element from the right, we update the Tailpointer.
#As we add element to the left, we update the Headpointer.

from selectors import EpollSelector


#creating nodes.
class Node:
    def __init__(self,val):
        self.left= None
        self.right= None
        self.data= val


class Queue:
    
    # creates head and tail pointer
    def __init__(self):
        self.Headpointer= None
        self.Tailpointer= None

    #Adding nodes to the left.
    def Create_Node(self, val):
        #if its the first node
        if self.Headpointer is None:
            newnode= Node(val)
            self.Headpointer= newnode
            self.Tailpointer= self.Headpointer
        #after first node.
        else:
            head_iterator= self.Headpointer
            newnode= Node(val)
            head_iterator.left= newnode
            head_iterator.left.right= head_iterator
            self.Headpointer= newnode
            
    def Delete_Node(self):
        self.Tailpointer = self.Tailpointer.left
        self.Tailpointer.right.left=None
        self.Tailpointer.right= None

    def ChekQuantity(self):
        if self.Headpointer == None:
            return False
        else:
            return True 


    def print(self):
        while self.Headpointer !=None:
            print(self.Headpointer.data)

            self.Headpointer= self.Headpointer.right

    
queue= Queue()

queue.Create_Node(4)
queue.Create_Node(5)
queue.Create_Node(6)
queue.Create_Node(7)

queue.Delete_Node()
queue.Delete_Node()

queue.Create_Node(8)
queue.Create_Node(9)
queue.Create_Node(10)

if queue.ChekQuantity() == True:
    print("Queue contains elements")
else:
     print("Queue does not contains elements")


queue.print()






#3: Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

list1 = [-1,0,1,2,-1,-4]
Final_list=[]
Zero_List=[]
Check_list=[]

index1= 0
index2=1
index3=0
while index1<len(list1)-1:
    while index2<=len(list1)-1:
        Final_list.append( [list1[index1],list1[index2]] )
        index2= index2+1
    
    index1=index1+1
    index2= index1+1


while index3<len(Final_list):
    index4=0
    while index4<len(list1)-1:
        val= list1[index4]
        if index4!= list1.index(Final_list[index3][0]) and index4!=list1.index(Final_list[index3][1]):
            if Final_list[index3][0]+ Final_list[index3][1]+val==0 and (Final_list[index3][0] not in Check_list or Final_list[index3][1] not in Check_list or val not in Check_list) :
                
                Zero_List.append([ Final_list[index3][0],Final_list[index3][1],val])
                
                Check_list.append(Final_list[index3][0])
                Check_list.append(Final_list[index3][1])
                Check_list.append(val)

        
        index4=index4+1
    
    index3=index3+1

print(Zero_List)




                                                #*******************************



#4: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. 
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some threshold. 
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks, 
# and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() 
# should behave identically to a single stack (that is, pop() should 
# return the same values as it would if there were just a single stack).

class Stack:
    #constructor that creates a list inside another list.
    def __init__(self,capacity):
        self.list1=[[]]
        self.capacity=capacity

    #pusing elements to each sublist
    def push(self,val):
        #getting index of sublist
       index_sublist=len(self.list1)-1
       # if the sublist hasn't reached the capacity, push to the individul sublist
       if len(self.list1[index_sublist])<self.capacity:
            self.list1[index_sublist].append(val)

        #if the sublist reaches the capacity, create a new sublist
        #sublist index will be updated as we add new list inside the list.
       else:
            self.list1.append([])
            #getting the sublist index
            index_sublist=len(self.list1)-1
            self.list1[index_sublist].append(val)

    #deleting the last element from the last stack
    def pop(self):
        index_sublist= len(self.list1)-1
        del self.list1[index_sublist][-1]
        if len(self.list1[index_sublist])==0:
            del self.list1[index_sublist]

    #Deleting the last element from a specific index.
    def pop_at(self, sublist_index):
        del self.list1[sublist_index][-1]
        index=sublist_index

        #rearraging the sublist so each sublist cointains at least the capacit amount of elements from left to right.
        while index<len(self.list1)-1:
            elem = self.list1[index+1].pop(-1)
            self.list1[index].append(elem)
            index=index+1
      
           
    def print(self):
        print(self.list1)
    


stack=Stack(3)

stack.push(1)
stack.push(2)
stack.push(3)

stack.push(4)
stack.push(5)
stack.push(6)

stack.push(7)
stack.push(8)
stack.push(9)

stack.push(10)
stack.push(11)
stack.push(12)


stack.pop_at(2)
stack.pop_at(1)


stack.print()


                                #*******************************************  


#5: write a program to sort a stack so the smallest items are on top. You can use maximum two stacks. 

def Sort_Stack(stack=[]):

    temp_stack=[]
    #adding first element from the stack into the temporary stack.
    temp_stack.append(stack.pop())
    
    #As long as thge length of the stack is greater than 0:
    while len(stack)>0:
        #popping one element from the stack
        stack_val=stack.pop()

        #compare that one element with all elements inside the temp_stack
        while len(temp_stack)>0:
            #getting the top element from the temp_stack
            temp_stack_val= temp_stack[-1]
            
            #if the element from the stack is less than the element from the temp_stack,
            #pop() that elemeny from the temp_stack and add that into stack.
            if stack_val<temp_stack_val:
                stack.append(temp_stack.pop())
            #if the element from the stack is greater than the element from the temp_stack,
            elif stack_val>temp_stack_val:
                #add that element into temp_stack
                temp_stack.append(stack_val)
                break
    
        if len(temp_stack)==0:
            temp_stack.append(stack_val)
        
    
    while len(temp_stack)>0:
        stack.append(temp_stack.pop())
    
    del temp_stack
    print(stack)
    
            


list1=[25,15,11,4,17,12,23,29,37]

Sort_Stack(list1)

        


        



        



 





    
    










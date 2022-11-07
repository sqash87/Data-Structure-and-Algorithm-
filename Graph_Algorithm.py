
                        
                        
    #********************* Graph With Adjacency Matrix ***************************


class Graph:
    #Whenever we create an object, constructor that will crate a 2D-Matrix

    def __init__(self,nodes):
        self.nodes= nodes
        self.matrix =[]
        #by defauly we will crate the graph as directed but add_note()
        #can change this.


        for row in range(self.nodes):
            self.matrix.append([0 for column in range(self.nodes)])

    #adding nodes:
    #type= True = Directed and type=False= undirected
    def add_node(self, node1, node2, weight, type):

        if (node1 and node2)<=self.nodes and (node1 and node2) >-1:
            #initializing value to the matrix(not appending)
            self.matrix[node1][node2]= weight

        #for undirected graph
        if type!=True:
            self.matrix[node2][node1]= weight

    #Deleting Nodes
    def del_node(self, node1, node2):
        if (node1 and node2)<=self.nodes and (node1 and node2) >-1:
            self.matrix[node1][node2]= 0
        #for undirected graph
        if type!=True:
            self.matrix[node2][node1]= 0

    
    
    #Printing Nodes
    def print_matrix(self):
        print(self.matrix)


        
graph= Graph(3)

graph.add_node(0,0,5,True)
graph.add_node(0,1,7,True)
graph.add_node(1,0,8,True)

graph.add_node(1,2,9,False)

graph.add_node(2,1,6,False)

graph.print_matrix()
        
                     
            #********************* Graph adjacent list ***************************

from collections import deque

#Implementing a graph with adjacent list:

class Graph:
    
    #constructor will create a dictionary
    def __init__(self, nodes, bool):
        self.nodes= nodes
        #by default it will be a directed graph.
        self.directed= bool
        self.dict= { node: [] for node in range(self.nodes)}

    # function that will add nodes:
    def add_edge(self,node1, node2, weight):
        self.dict[node1].insert(node1,(node2,weight))
        
        # if the graph not directed:
        if self.directed!=True:
            self.dict[node2].insert(node2,(node1,weight))

    # function that will remove nodes:
    def del_nodes(self,node1,node2,weight):
        self.dict[node1].remove((node2,weight))

    #function to print
    def print_list(self):
        return self.dict
    
                                #********************  DSF  ***********************

    def DSF(self, node):
        #Stack will contain all the children
        
        Stack=[]
        #DSF_list will contain all the sorted nodes
        DSF_list= []
        
        #1:
        #A:Put the first node inside the set.
        
        DSF_list.append(node)
        #B: Gettng the children of first the node and put them stack.
        children = self.dict[node]
        for item in children:
            Stack.append(item[0])

        #2:As long as the stack doesn't run out of elements
        while len(Stack)>0:
            
            #A:gettingb a node from the tp of the stack and delete it.
            elem1= Stack.pop()
            
            #B:Adding that node in the DSF_list
            DSF_list.append(elem1)
            
            #C:etting the children of the recently poped element
            children= self.dict[elem1]
            
            #D: Checking if the children are already inside the DSF_list
            for item in children:
                
                #E: If children are not in the DSF_list:
                if item[0] not in DSF_list:
                    
                    #F: Add the children to the Stack.
                    Stack.append(item[0])
            
        #G converting the list to dict and revert back to list to get rid of duplication
        DSF_list= list(dict.fromkeys(DSF_list))
        print(DSF_list)

                                            #************* BSF  **************
    
    def BFS(self,node):
        #it will contain all the children of the nodes.
        Queue= deque([])
        
        #it will contain all the BFS nodes
        BFS_list=[]

        #1:add the first node to the BFS_list first
        BFS_list.append(node)
        
        #2: add the children of the first node to the queue

        children= self.dict[node]
        for items in children:
            Queue.appendleft(items[0])

        #3: While the Queue is not empty:

        while len(Queue)>0:
            #A: pop() the first item from the right 
            node= Queue.pop()
            #B: Add that element in the list
            BFS_list.append(node)
            #C: Find the children of that node:
            children= self.dict[node]

            #D: Checking if the children are already inside the BSF_list
            for items in children:
                #E: If children are not in the BSF_list:
                if items[0] not in BFS_list:
                    #F: Add those children to the back of the Queue
                    Queue.appendleft(items[0])
        
        BFS_list= list(dict.fromkeys(BFS_list))

        print(BFS_list)
                                 
                                    #*********** path Between Nodes *************#


    #Find if there is a path between two nodes.
    def Find_path(self,node1,node2):
        Stack=[]
        DFS_list=[]

        DFS_list.append(node1)
        #finding the children of the node1

        children= self.dict[node1]
        #addig children of the nodes in the stack
        for items in children:
            Stack.append(items[0])
        
        while len(Stack)>0:
            node= Stack.pop()

            if node==node2:
                return (print("Path Exists"))
            else:
                DFS_list.append(node)
                children= self.dict[node]
                
                for items in children:
                    if items[0] not in DFS_list:
                        Stack.append(items[0])
            
        return (print("path does not Exist"))

graph= Graph(11,False)

graph.add_edge(0,2,1)
graph.add_edge(0,4,1)
graph.add_edge(2,3,1)
graph.add_edge(2,5,1)
graph.add_edge(2,7,1)
graph.add_edge(2,8,1)

graph.add_edge(3,9,1)
graph.add_edge(3,10,1)
graph.add_edge(4,3,1)

graph.add_edge(5,6,1)
graph.add_edge(5,7,1)
graph.add_edge(5,8,1)

graph.add_edge(6,7,1)
graph.add_edge(7,8,1)
graph.add_edge(9,2,1)

graph.DSF(0)
graph.BFS(0)

graph.Find_path(3,8)

bool= graph.Find_path(8,3)


                                #********** Longest Cycle  *************#

#Find the longest cycle in the graph 
# when each node of the graph can have at most one outgoing edge.
def Find_cycle(edge):
      
    #visited nodes
    visited_nodes=[]
    # Stack will contain children of visited node.
    Stack=[]

    #contains cycle numbers.
    cycle_number=[]
    
    #creating a dictionary 
    dict= { node: [] for node in range(len(edge))}
    
    #keep track of key index
    key_index=0
    #keep track of the values
    val_index=0
    
    #convert the list of edges into adjacent list.
    while key_index<len(edge):
        dict[key_index].insert(key_index,(edge[val_index]))
        key_index=key_index+1
        val_index=val_index+1
    
    #adding the first node in the visited list.
    visited_nodes.append(0)
    #getting the children of that node.
    children= dict[0]
    #adding the children of that node in the stack
    Stack.append(children[0])

    #as long as the stack is not empty:
    while len(Stack)>0:
        #getting a node from the stack
        node= Stack.pop()
        
        #currenty visited node was added in the visited list.
        visited_nodes.append(node)
        
        # checking if the key(node) exits in the dictionary:
        if node in dict:
            # children of the recently added node:
            children= dict[node]
        else:
            continue

        #if the children of the recently visited node is already in the visited list: 
        if children[0] in visited_nodes:
            #get the index value of that children in the visited node 
            index_of_node= visited_nodes.index(children[0])
            
            #and index of the recently added node in the vites node
            index_recent_node= len(visited_nodes)-1
            
            #save it in the cycle number list.
            cycle_number.append((index_recent_node-index_of_node)+1)
        else:
            Stack.append(children[0])
    
    if len(cycle_number)>0:
        return  max(cycle_number)
    else:
        return -1

    
edge=[2,-1,3,1]

longest_cycle= Find_cycle(edge)

print(longest_cycle)

                            #*************  Connected Components  ********************
    
#connected components:
# A set of nodes forms a connected component in an undirected graph 
# if any node from the set of nodes can reach any other node by traversing edges.
#Determine the total connected components of a an undirectd graph:

def Connected_components(total_node,edges):
    #implementing graph with dictionary
    graph={node:[] for node in range(total_node)}
    
    #list contains all the keys(nodes) of the graph.
    Nodes=[]
    
    #list contains all the visited lists.
    visited_list=[]
    
    #Stack for each DFS
    Stack=[]
    
    #total number of DFS Tree
    count=0
    
    #converting the list of list into the adjacent list.
    for item in edges:
        graph[item[0]].insert(item[0],(item[1]))
        graph[item[1]].insert(item[1],(item[0]))
    
    #Adding the all keys(nodes) into the Nodes list.
    for keys in graph:
        Nodes.append(keys)
    
    # for each item of Nodes list
    for item in Nodes:
        #if an node is not in the visited list:
        if item not in visited_list:
            
            #add that node in the visited list and apply **DSF** on it by:
            visited_list.append(item)
            
            # Checking if the Key(node) is in the dictionaty(Spafe practice)
            if item in graph:
                #Finding the children of that node
                children= graph[item]
            else:
                continue

            for items in children:
                #add the children of that node in the Stack
                Stack.append(items)
            #while the temporary stack is not empty:
            while len(Stack)>0:
                #pop a node from the stack
                node=Stack.pop()
                #add that node in the visited_list
                visited_list.append(node)
                
                # Checking if the Key(node) is in the dictionaty(Spafe practice)
                if node in graph:
                    #Find the children of that poppedn node
                    children= graph[node]
                    for items in children:
                        #if those children are not in the visited list:
                        if items not in visited_list:
                            #add them in the temporary Stack.
                            Stack.append(items) 
                #if the key is not in the ductionary: Skip the current iteration of the loop.
                else:
                    continue
            
            count=count+1
            #clear the temporary stack after each DFS
            Stack.clear()
        # If the next item(node) is already in the visited node: skip it to the next one
        else:
            continue

    return count


list1=[[0,2],[1,2],[0,1],[0,3],[1,3],[0,4],[8,9],[8,10],[10,11],[5,6],[5,7]]
list2= [[0,1],[1,2],[3,4]]
list3=[[0,1],[1,2],[2,3],[3,4]]

Total_connected_components= Connected_components(5,list3)
print("Total_connected_components:",Total_connected_components)

Total_connected_components= Connected_components(5,list2)
print("Total_connected_components:",Total_connected_components)

Total_connected_components= Connected_components(12,list1)
print("Total_connected_components:",Total_connected_components)


#**************** Topological Sort *************************


def Topological_sort(edges,total_nodes):
   
    #initialize an adjacent list:
    graph={node:[] for node in range(total_nodes)}

    #convert the list of edges into an adjacent list
    for item1,item2 in edges:
        graph[item1].append(item2)

    #contains all the nodes
    Nodes=[]

    #contains all the visited nodes:
    visited_nodes=[]

    #contains the topological order
    Topological_stack=[]

    #1: Adding all the keys (nodes) of the dictionary in the Node list:
    for keys in graph:
        Nodes.append(keys)

    # 2: Running a for loop on the Nodes:
    for node in Nodes:
        #3: only choosing the node that are not in the Topological_Stack
        if node not in Topological_stack:
            #adding that chosen node on the visited list.
            visited_nodes.append(node)
            #As long as the length of the visited list is greater than 0:
            while len(visited_nodes)>0:
                unvisted_child = True
                #as long as the a node has children that are not already in the Topological_sort or a node has no children:
                while unvisted_child==True:     
                    #getting the top element from the visited node list.
                    node= visited_nodes[-1]
                    #Getting the children of that node
                    children= graph[node] 
                    
                    #if the node has children:
                    if children :
                        child_count=0
                        #looping through the children:
                        for child in children:
                            #if one child is found that is not in the Topological Stack:
                            if child not in Topological_stack:
                                # insert that node in the visited node 
                                # and go back to getting the top element from the visited node list again
                                visited_nodes.append(child)             
                                break
                            #if the child are in the visited_node list, count the # of child of that node.
                            else:
                               child_count=child_count+1
                        
                        # if all the chldren of that node are in the topological list:
                        if child_count==len(children):
                            #pop that node from the visited list.
                            node=visited_nodes.pop()
                            #add that node in the topological stack.
                            Topological_stack.append(node)
                            #set the unvisted_child to False and go back to getting the top element from the visited node list again
                            unvisted_child= False
                    
                    # if the node has no children:    
                    else:
                        #pop that node from the visited list.
                        node=visited_nodes.pop()
                        #add that node in the topological stack.
                        Topological_stack.append(node)
                        #set the unvisted_child to False and go back to getting the top element from the visited node list again
                        unvisted_child= False                            
    
    #reversing the stack containing the Topological sort.
    Topological_stack.reverse()
    
    print("Topplogical order:",Topological_stack)
 
    
#list of Nodes that I will perfom DFS on
    
edges= [[0,1],[0,2],[0,6],[1,4],[1,3],[2,3],[2,6],[3,4],[3,5],[5,6]]

edges2=[[5,2],[5,0],[4,0],[4,1],[2,3],[3,1]]

Topological_sort(edges,7)

Topological_sort(edges2,6)


























    



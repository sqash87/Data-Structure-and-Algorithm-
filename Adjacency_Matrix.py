
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
        
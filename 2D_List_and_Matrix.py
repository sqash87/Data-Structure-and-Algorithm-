
#1 Rotate the matrix 90 degree clock wise(in place)
# Step 1: Find the Transpose of the matrix
# Step 2: Horizontal reflection

Matrix=([1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],
[25,26,27,28,29,30],[31,32,33,34,35,36])

def Rote_Matrix(matrix):
    cor1=0
    cor2=1

    while cor1<len(matrix)-1:
        while cor2<len(matrix):
           
            temp1=matrix[cor1][cor2]
            temp2=matrix[cor2][cor1]
            
            matrix[cor2][cor1]= temp1
            matrix[cor1][cor2]= temp2        
            cor2= cor2+1  
        
        cor1= cor1+1
        cor2= cor1+1
    
    # Horizontal reflection of the trnasposed Matrix
    if len(matrix)%2!=0:
        cor1= 0
        cor2= 0
        cord2= len(matrix)-1
        midpoint= len(matrix)/2
        while cor1<len(matrix):
            while cor2<midpoint:
               
                temp1= matrix[cor1][cor2]
                temp2= matrix[cor1][cord2]
            
                matrix[cor1][cor2] = temp2
                matrix[cor1][cord2]= temp1

                cor2= cor2+1
                cord2= cord2-1
            
            cor1= cor1+1
            cor2= 0
            cord2= len(matrix)-1
        
        print(matrix)
    #if the matrix is Even
    else:
        cor1= 0
        cor2= 0
        cord2= len(matrix)-1
        midpoint= (len(matrix)-1)/2
        while cor1<len(matrix):
            while cor2<=midpoint:
               
                temp1= matrix[cor1][cor2]
                temp2= matrix[cor1][cord2]
            
                matrix[cor1][cor2] = temp2
                matrix[cor1][cord2]= temp1

                cor2= cor2+1
                cord2= cord2-1
            
            cor1= cor1+1
            cor2= 0
            cord2= len(matrix)-1
        
        print(matrix)      

Rote_Matrix(Matrix)
                                                #*************

#2: if an element of a matrix is 0, set the row and column of that element 0.
Matrix=[[1,2,0,4],[5,6,7,8],[9,0,11,12]]
def Find_Zero(matrix):
    cor1=0
    cor2=0
    row_list= set()
    column_list= set()
    M= len(matrix)
    N= len(matrix[0])

    # Step1: 
    # Fist finding all the zeros in the matrix 
    # and putting the row and column numbers of those 0 in row and column sets.
    while cor1<M:
        while cor2<N:
            if matrix[cor1][cor2]==0:
                row_list.add(cor1)
                column_list.add(cor2)     
                cor2= cor2+1      
            else:
                cor2= cor2+1
        cor1= cor1+1
        cor2=0
    
    #Step2:
    #cnverting the set into lists
    row_list= list(row_list)  
    column_list= list(column_list)
  

    #Step3:
    #setting the rows 0
    index1=0
    index2=0
    while index1<len(row_list):
        cor1= row_list[index1]
        j=0
       
        while j<N:
            matrix[cor1][j]=0
            j=j+1
        
        index1= index1+1
   
    #Step4:
    #setting the columns 0
    while index2<len(column_list):
        cor2= column_list[index2]
        p=0
        while p<M:
            matrix[p][cor2]=0
            p=p+1
        
        index2= index2+1
    
    
    print(matrix)
        
Find_Zero(Matrix)
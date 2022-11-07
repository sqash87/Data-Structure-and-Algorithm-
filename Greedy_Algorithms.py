


#print out the the meximal sets of intervals:

def Maximal_Interval(list1):
    # sort the list1 in assending order with respect to the [x,y] y 
    # so I can get the earliest interval
    list1.sort(key=lambda x: x[1])
    
    #1: sorted list contains the intervals
    Sorted_list=[]
    
    #2: Find the earliest end time (y)of [x,y]
    earliest_end_time= list1[0][1]
    
    #3: adding the interval that conatins the earliest end time in the sorted_list.
    Sorted_list.append(list1[0])

    #4: loop through the list1 except that ones are already in the sorted list:
    for items in list1:
        if items not in Sorted_list:
            #5: Choosing intervals where the starting time is larger than the immediate finishing time(earliest_end_time).
            if items[0]>earliest_end_time:
                #if we find a interval that satisfies that condition:
                #reassign the value of earliest_end_time
                earliest_end_time= items[1]
                #add the item in the sorted_list
                Sorted_list.append(items)
            else:
                continue
    
    print(Sorted_list)

list1= [[5,7],[17,21],[10,13],[19,22],[15,18],[14,16],[15,20],[25,30],[23,27],[8,10]]

Maximal_Interval(list1)

#Given an array of meeting time intervals consisting of start and end times
#find the minimum number of conference rooms required simultenuoisly.
#For example, Given [[0, 30],[5, 10],[15, 20]], return 2.

def Min_Room(list1):
    #contains the visited nodes
    visited_intervals=[]
    #1: Sort the list in descending order with the second element of the list:
    list1.sort(key=lambda x:x[1], reverse=True)
    
    #2: Find the start time of an interval that ends the latest
    start_time_of_latest_end_interval= list1[0][0]
    
    #3: Compare the start time of the latest interval(first interval) with the end time of the next interval 
        #as long as they are not in the visited list. 
    for items1 in list1:     
        if items1 not in visited_intervals: 
            #if the end time of the next interval is greater than or equal to the start time of the previous interval:  
            if items1[1]>=start_time_of_latest_end_interval:
                #4: Add that next interval in the visitedb list.
                visited_intervals.append(items1)
                #5: Then reassign the start time of the interval with the start time of the next interval.
                start_time_of_latest_end_interval= items1[0]
            else:
                continue        
        else:
            continue
        
    print(len(visited_intervals))



list1= [[5,7],[10,13],[8,10]]
list2= [[5,10],[15,20],[0,30]]
list3= [[7,10],[2,4]]

Min_Room(list1)
Min_Room(list2)
Min_Room(list3)


#There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
#You are giving candies to these children subjected to the following requirements:
    
    #1: Each child must have at least one candy.
    #2: Children with a higher rating get more candies than their neighbors.

#Return the minimum number of candies you need to have to distribute the candies to the children.


def Candy_distribute(list1):
    
    #getting the indices of the sorted list
    sorted_indices=sorted(range(len(list1)), key=lambda k: list1[k])

    #Assigning 1 candy to all the indices of candy_distribution list.
    candy_distribution=[1]*len(list1)

    for index1 in sorted_indices:
    
        #sorted_indices: [0, 4, 3, 2, 1] points to the values of the original list
        #index1=0 points to the first element of the original list:
        if index1==0:
            if len(list1)>1:
                if list1[0]>list1[1]:
                    candy_distribution[index1]= candy_distribution[index1+1]+1
            else:
                pass
        
        #index=4 points to the last element of the original list:
        elif index1==len(list1)-1:
            if list1[-1]>list1[-2]:
                candy_distribution[index1]= candy_distribution[index1-1]+1
        
        # Any other indices:
        else:
            #checking if the value of the chosen index is greater than both left and right neighbors:
            if list1[index1]>list1[index1-1] and list1[index1]>list1[index1+1]:
                print(candy_distribution[index1-1],candy_distribution[index1+1]+1)
                candy_distribution[index1]= max( candy_distribution[index1-1],candy_distribution[index1+1])+1

            #checking if the value of the chosen index is greater than its left neighbor and if it is:
            #then update the number of candies of a particular value(original list) corresponding with the sorted index.
            elif list1[index1]>list1[index1-1]:
                candy_distribution[index1]= candy_distribution[index1-1]+1

            #checking if the value of the chosen index is greater than its right neighbor:
            #then update the number of candies of a particular value(original list) corresponding with the sorted index.
            elif list1[index1]>list1[index1+1]:
                candy_distribution[index1]= candy_distribution[index1+1]+1
            
            #if the value of the chosen index is equal to both left and right: don't add any candy.
            else:
                pass

    print(candy_distribution,":",sum(candy_distribution))

list1=[1,2,87,87,87,2,1]
#list1=[1,7,3,2,1]
#list1= [1]

Candy_distribute(list1)


#******************* Method 2 ***************************#

        
def Candy(Children):
    
    #Total Number of children
    length=len(Children)
    
    #Distribute 1 candy to all the children
    Candies= [1]*len(Children)
   
   #looping through the children L-->R:
    for child in range(len(Children)-1):
        #starting from the 1st child, 
        #updating right child's candy with respect to immediate left child's candy.
        if Children[child]<Children[child+1]:
            Candies[child+1]= max(Candies[child],Candies[child+1])+1
    
    #looping through the children R-->L
    for child in range(length-2,-1,-1):
        #staring from the second to the last child, 
        #Updating current child's candy with respect to immediate right child's candy.
        if Children[child]>Children[child+1]:
            Candies[child]= max(Candies[child], Candies[child+1])+1
    
    print(sum(Candies))


list1=[1,7,3,2,1]

Candy(list1)
        






        
        



        
        






        







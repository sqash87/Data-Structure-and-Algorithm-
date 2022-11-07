
#Binary Search:
def Bibary_Search(list1,val):
    low_index=0
    high_index= len(list1)-1
    midpoint= (low_index+high_index)//2

    #As long as the low_index and high_index are not the same
    while low_index!=high_index:
        
        if val==list1[midpoint]:
            return midpoint
        
        #updating the midpoint each time low_index chnages 
        elif val>list1[midpoint]:
            low_index=midpoint+1
            midpoint= (low_index+high_index)//2
        
        #updating the midpoint each time high_index chnages    
        else:
            high_index= midpoint-1
            midpoint= (low_index+high_index)//2


    if high_index==low_index:
        return high_index

#Linear Search
def linerar(list1, val):
    for item in list1:
        if val in list1:
            return list1.index(val)


list1= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
Found_item_index= Bibary_Search(list1,3)
print("Index of the found item:", Found_item_index)
print("Value of the item:",list1[Found_item_index])

Found_item_index2= linerar(list1,3)
print("Index of the found item:", Found_item_index2)
print("Value of the item:",list1[Found_item_index2])





#Hash Map:

#Hash Function: Creates a hash value which is an index value of an array
#Set function: Map the (key,val) to that particular index.
  
  #Process: 
  # Set function checks whether a key already axists at a particular index,
  # if it does,then the set function will simply update the (key,val) pair in that index.
  # if key doesn't exists then set() will append (key, val) in that index.
  # With this process, if two keys have same Hash value, then set() would simply go 
  # to that particular index and a new append(key,val)

#Get Function: It will get the vlaue of the key after converting the key into Hash value.


import re
from traceback import print_tb


class Hashtbale:
  def __init__(self):
    self.Max=6
    self.arr= [[] for elem in range(self.Max)]
  
  def Get_Hash(self, key):
    hash=0
    for item in key:
      hash=hash+ord(item)
    return hash % self.Max
  
  def Set_Value(self,key,val):
   
    Hash_Val= self.Get_Hash(key)
    #Searcing the index to see if the key exists
    found = False
      #if it does, update that index with new value.
    for index, elem in enumerate(self.arr[Hash_Val]):     
      if elem[0]==key:
        self.arr[Hash_Val]=[[key,val]]
        found= True
    #if the key doesn't exist, then add a new (key,val)
    if found==False:
      self.arr[Hash_Val].append([key,val])
  
  def Get_value(self,key):
    Hash_value= self.Get_Hash(key)
    for elems in self.arr[Hash_value]:
     if elems[0]==key:
      print(elems[1])
    
  def Del_value(self,key):
    Hash_value= self.Get_Hash(key)
    for index, elem in enumerate(self.arr[Hash_value]):
      if elem[0]==key:
        del self.arr[0][index]
        break

          
  def Print_Hash_Table(self):
    print(self.arr) 
      
      

ht= Hashtbale()

ht.Set_Value("March",3)
ht.Set_Value("April",4)
ht.Set_Value("May",5)
ht.Set_Value("June",6)
ht.Set_Value("May",12)

ht.Get_value("June")



ht.Print_Hash_Table()



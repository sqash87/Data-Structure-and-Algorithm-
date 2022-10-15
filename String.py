
#1:Determine if the string has all unique charaters.

def is_unique(mystring):
    index=0
    while index<len(mystring):
        if mystring.count(mystring[index])>1:
            return False
        index= index+1
    return True


mystring="abcdce"

if is_unique(mystring) is True:
    print("String contains unique characters")
else:
    print("String contains duplicated Value")

                                            
                                            
                                           

#2: Write a method to replace all the spaces in a string with ‘%20’. 

mystring= "ad egh kol   "
#strip()spaces at the beginning and at the end of the string:
mystring= mystring.strip()

mystring= mystring.replace(" ", "%20")

print(mystring)


#3: Given two strings write a method to check if one string is a permutation of other. 
def Is_permutation(string1, string2):
    if len(string1)!=len(string2):
        return False
    else:
        #Assigning an arry of 128 with False
        temp_str=[False]*128
        
        for element in range(0, len(string1)):
            val= ord(string1[element])
            #when i see the char inside the temp_str assign True
            if temp_str[val] is False:
                temp_str[val]= True
            #if we again see the similar char insid ethe temp_str, pass
            elif temp_str[val] is True:
                pass
        
        for element2 in range(0, len(string2)):
            val1= ord(string2[element2])
            #if i encounter a char that has not been assigned true, that means string2 has new characters. 
            if temp_str[val1] is False:
                return False

    return True

if Is_permutation("abcd","cabe") is True:
    print("They are permutation of each other")
else:
    print("They are **NOT** permutation of each other")

                                                    
                                                    #*************



#4 Checking palindrome or not
def Is_plin(string1):
    midpoint= int(len(string1)/2)
    if len(string1)%2==0:
        left_srt= string1[0:midpoint]
        right_str= string1[len(string1)-1:midpoint-1:-1]
        index=0
        while index< len(left_srt):
            if left_srt[index]!=right_str[index]:
                return False
            index=index+1
    
    #for odd string middle element can be anything.
    else:
        left_srt= string1[0:midpoint]
        right_str= string1[len(string1)-1:midpoint:-1]
        index=0
        while index< len(left_srt):
            if left_srt[index]!=right_str[index]:
                return False
            index=index+1
        
    return True

    
if Is_plin("abdncmcbdba") is True:
    print("It is Palindrome")

else:
    print("It is not Plindrome")

                                   
                                    #*************


#5 Check whether a string is a permutation of a palindrome.
#If it is an even number of palindrome, each character will be repeated even number of time.
#If it an odd number of palindrome, each character will be repeated even number of time 
#but the middle character will be repeated odd number of time.

def Is_permu(string1):
    #arry contains element that repeats odd number of times
    odd_elm=[]
    index=0
    while index<len(string1):
        #if a character has a repeatition of odd number of times 
        if string1.count(string1[index])%2!=0:
            odd_elm.append(string1[index])
        
        elif len(odd_elm)>1 and odd_elm[-1]!=odd_elm[0]:
            return False
        
        index=index+1

    return True

if Is_permu("abdabdbcbdca") is True:
    print(" it is permutation")

else:
    print("it is not a plaindrome")

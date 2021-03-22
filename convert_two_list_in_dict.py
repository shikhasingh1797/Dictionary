list1=['one','two','three','four','five']
list2=[1,2,3,4,5,] 
#print ("Original key list is : " + str(list1)) 
#                                                                                                                                                print ("Original value list is : " + str(list2)) 
res = {} 
for key in list1: 
    for value in list2: 
        res[key] = value 
        list2.remove(value) 
        break    
# Printing resultant dictionary  
print ("Resultant dictionary is : " +  str(res)) 
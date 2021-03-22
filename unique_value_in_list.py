list1=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
a=[]
for key in list1:
    for i in key:
        if key[i] in a:
            pass
        else:
            a.append(key[i])
print(a)
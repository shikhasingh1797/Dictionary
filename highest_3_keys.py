list2 = {
    'a':50, 
    'b':58,
    'c': 56,
    'd':40,
    'e':100, 
    'f':20
    } 
key_list=list2.keys()
b=list(key_list)
val_list=list2.values()
a=list(val_list)
max1=0
max2=0
max3=0
key1=0
key2=0
key3=0
i=0
new_list=[]
while i<len(a):
    if a[i]>max1:
        max1=a[i]
        key1=b[i]
    i=i+1
new_list.append(key1)
j=0
while j<len(a):
    if max2<a[j]<max1:
        max2=a[j]
        key2=b[j]
    j=j+1
new_list.append(key2)
c=0
while c<len(b):
    if max3<a[c]<max2:
        max3=a[c]
        key3=b[c]
    c=c+1
new_list.append(key3)
print(new_list)
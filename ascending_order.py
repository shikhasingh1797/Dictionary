dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
key_list=dic.keys()
b=list(key_list)
val_list=dic.values()
a=list(val_list)
new_list=[]
i=0
while i <len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            tmp=a[i]
            a[i]=a[j]
            a[j]=tmp
        j=j+1
    i=i+1
d=zip(b,a)
print(dict(d))
#print(a)




#l1=[1,2,3,4]
#l2=['a','b','c','d']
#d1=zip(l1,l2)
#print (d1)#Output:<zip object at 0x01149528>
#Converting zip object to dict using dict() contructor.
#print (dict(d1))
#Output:{1: 'a', 2: 'b', 3: 'c', 4: 'd'}


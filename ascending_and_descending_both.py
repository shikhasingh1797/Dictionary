dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
key_list=dic.keys()
keyV=list(key_list)
val_list=dic.values()
valA=list(val_list)
new_list=[]
# i=0
# while i <len(a):
#     j=0
#     while j<len(a):
#         if a[i]<a[j]:
#             tmp=a[i]
#             a[i]=a[j]
#             a[j]=tmp
#         j=j+1
#     i=i+1
# d=zip(b,a)
# print(dict(d))

# print(keyV)
# print(valA)
i=0
d={}
while i<len(keyV):
    d[keyV[i]]=valA[i]
    i=i+1
print(d)



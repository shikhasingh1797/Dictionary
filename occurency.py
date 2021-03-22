a="mississippi"
b={}
i=0
while i<len(a):
    count=0
    j=0
    c={}
    while j<len(a):
        if a[i]==a[j]:
            count=count+1
        j=j+1
    #if b not in c:
        #print("dfg")
        #c[i]=b[i]
    b[a[i]]=count
    i=i+1
print(b)

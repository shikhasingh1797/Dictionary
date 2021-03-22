dict =  {
   'Alex': ['subj1', 'subj2', 'subj3','sub4'], 
   'David': ['subj1', 'subj2']}
count=0
for i in dict.values():
    for j in range(len(i)):
        count=count+1
print("total value=",count)
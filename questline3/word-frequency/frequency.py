d={}
a=input('enter the para:')
w=a.split()
for i in w:
    if i  not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
sorted_val=sorted(d.items())
d2=dict(sorted_val)

for i in d:
    print(i,'-->',d[i])
    

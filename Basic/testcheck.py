def precedence(a):
    c=["first","second","third"]
    for i in range(0,len(c)):
        if(c[i]==a):
            return i

lis=["third","first","second"]
new=[]
x=0
k=0
for i in range(0,len(lis)):
    for j in range(i+1,len(lis)):
        if(precedence(lis[i])>precedence(lis[j])):
        
            t=lis[i]
            lis[i]=lis[i+1]
            lis[i+1]=t
   
print(lis)        

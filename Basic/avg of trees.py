n=int(input("no of trees : "))
sum=0
trees=[]
for i in range(0,n):
    k=int(input("values of trees : "))
    trees.append(k)
    sum+=trees[i]
avg=sum/n
print(round(avg,3))                

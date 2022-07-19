s=input()
diary=open("text.txt","w")
for i in range(len(s)):
    diary.write(str(ord(s[i])))
    if(i!=len(s)-1):
        diary.write(',')
diary.close()    
diary=open("text.txt","r")
string=""
for i in diary.readline():
    string=string+i
print(string)
k=string.split(',')
for i in k:
    print(chr(int(i)),end="")
diary.close()

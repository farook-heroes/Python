from tkinter import *


root=Tk()
root.geometry("400x400")

get=Entry(root,width=10)
get.pack()

def val():
    
    s=get.get()
    get.delete(0,END)
    diary=open("text.txt","w")
    for i in range(len(s)):
        diary.write(str(ord(s[i])))
        diary.write(' ')
    diary.close()    
def decrypt():
    diary=open("text.txt","r")
    string=""
    for i in diary.readline():
        string=string+i
    
    k=string.split()
    
    for i in k:
        print(chr(int(i)),end="")
    
    diary.close()       

submit=Button(root,text="button",command=val)
submit.pack()
deal=Button(root,text="decrypt",command=decrypt)
deal.pack()




root.mainloop()


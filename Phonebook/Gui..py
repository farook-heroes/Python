from tkinter import *
from tkinter import messagebox  
import add
import delete
import search
import view
root=Tk()
root.geometry('300x600')
root.title("Phonebook")
def add1():
    top1=Toplevel()
    name=Label(top1,text="Name :")
    getter_name=Entry(top1,width=50)
    phone_no=Label(top1,text="Phone No :")
    getter_phone=Entry(top1,width=50)
    def printer():
        add.addition(getter_name.get(),getter_phone.get())
        getter_name.delete(0,END)
        getter_phone.delete(0,END)
        messagebox.showinfo("Result","Added Sucessfully")  
    name.grid(row=0,column=0)
    getter_name.grid(row=0,column=1)
    phone_no.grid(row=1,column=0)
    getter_phone.grid(row=1,column=1)
    add_button=Button(top1,text="Add",command=printer,padx=50,pady=50)
    add_button.grid(row=2,column=0)
    
def delete1():
    top=Toplevel()
    idf=Label(top,text="ID :")
    getter_idf=Entry(top,width=50)
    idf.grid(row=0,column=0)
    getter_idf.grid(row=0,column=1)
    def printer():
        delete.deleter(int(getter_idf.get()))
        getter_idf.delete(0,END)
        messagebox.showinfo("Result","Deletied Sucessfully")
    delete_button=Button(top,text="delete",command=printer,padx=50,pady=50)
    delete_button.grid(row=1,column=0)
  
def search1():
    top=Toplevel()
    name=Label(top,text="Name :")
    getter_name=Entry(top,width=50)
    name.grid(row=0,column=0)
    getter_name.grid(row=0,column=1)
    def printer():
        k=search.searchbyname(getter_name.get())
        getter_name.delete(0,END)
        m=2
        n=0
        for i in k:
            res=Label(top,text=str(i))
            res.grid(row=m,column=n)
            m=m+1
    search_button=Button(top,text="Search",command=printer,padx=50,pady=50)
    search_button.grid(row=1,column=0)
def view1():
    top = Toplevel()
    c=view.viewer()
    m=0
    n=0
    for i in c:
        res=Label(top,text=str(i))
        res.grid(row=m,column=n)
        m+=1

button1=Button(root,text="Add",command=add1,padx=50,pady=50)
button2=Button(root,text="Delete",command=delete1,padx=50,pady=50)
button3=Button(root,text="Search",command=search1,padx=50,pady=50)
button4=Button(root,text="View",command=view1,padx=50,pady=50)
text=Label(root,text="Phonebook",pady=50)

blanktext=Label(root,text="                    ")
blanktext1=Label(root,text="                    ")
blanktext2=Label(root,text="                    ")
blanktext3=Label(root,text="                    ")
blanktext4=Label(root,text="                    ")
blanktext.grid(row=0,column=0,columnspan=3)
text.grid(row=0,column=3)



button1.grid(row=1,column=3)

button2.grid(row=2,column=3)

button3.grid(row=3,column=3)

button4.grid(row=4,column=3)


root.mainloop()

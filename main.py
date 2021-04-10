from tkinter import *

root = Tk()

i = 1
e = Entry(root, width=50, fg="#000000", bg="red", borderwidth=5)
e.grid(row="0", column="0")
e.insert(0, "Enter your name:")

def myClick():
    global i
    i +=1
    myLabel = Label(root, text=e.get())
    myLabel.grid(row=i, column=i)

#state=DISABLED

myButton = Button(root, text="Send", padx="50", pady="25", command=myClick, fg="white", bg="blue")
myButton.grid(row="1", column="1")


root.mainloop()
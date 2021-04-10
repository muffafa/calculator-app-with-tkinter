from tkinter import *

history = []
isReset = False
haveNewEntry = False

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(number):
    global isReset
    global haveNewEntry

    haveNewEntry = True

    if isReset:
        e.delete(0, END)
        isReset = False
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_operations(operant):
    global isReset
    global haveNewEntry


    if isReset:
        isReset = False
        current = str(e.get())
        currentlist = current.split("=")
        #print(currentlist)
        current = currentlist[1]
        e.delete(0, END)
        e.insert(0, str(current))
        haveNewEntry = True

    if haveNewEntry:
        current = str(e.get())
        e.delete(0, END)
        e.insert(0, str(current)+ str(operant))
        haveNewEntry = False
    elif (str(e.get())!=""):
        current = str(e.get())
        result_str = ""
        #print(len(current))
        for i in range(0, len(current)):
            if i != len(current)-1:
                result_str = result_str + current[i]
        e.delete(0, END)
        e.insert(0, str(result_str) + str(operant))


def button_equal():
    global history
    global isReset
    global haveNewEntry

    if haveNewEntry:
        current = str(e.get())
        e.delete(0, END)
        result = eval(current)
        answer = "=" + str(result)
        e.insert(0, answer)

        history.append(current + answer)
        print(history)
        isReset = True
        haveNewEntry = False

#Define Buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_clear = Button(root, text="Clear", padx=29, pady=20, command= button_clear)

button_add = Button(root, text="+", padx=37.4, pady=20, command=lambda: button_operations("+"))
button_subtract = Button(root, text="-", padx=39, pady=20, command=lambda: button_operations("-"))
button_division = Button(root, text="/", padx=39, pady=20, command=lambda: button_operations("/"))
button_multiplication = Button(root, text="*", padx=39, pady=20, command=lambda: button_operations("*"))

button_equal = Button(root, text="=", padx=39, pady=20, command= button_equal)


#Display buttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_equal.grid(row=4, column=1)
button_clear.grid(row=4, column=2)


button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiplication.grid(row=3, column=3)
button_division.grid(row=4, column=3)

root.mainloop()
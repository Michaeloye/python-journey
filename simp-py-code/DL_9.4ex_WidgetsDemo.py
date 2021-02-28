from tkinter import *

window = Tk()
window.title("Testing")
frame_1 = Frame(window) 
frame_1.pack()
checkbutton_bold = Checkbutton(frame_1, text = "Bold")
v1 = IntVar()
radiobutton_red = Radiobutton(frame_1, text = "Red", bg = "red", variable = v1, value = 1)
radiobutton_yellow = Radiobutton(frame_1, text = "Yellow", bg = "yellow",variable = v1, value = 2)

def getname():
    print(name_value.get()) # to return the name inputted to the name input

frame_2 = Frame(window)
frame_2.pack()
label = Label(frame_2, text = "Please enter your name")
name_value = StringVar()
name = Entry(frame_2, textvariable = name_value)
button = Button(frame_2, text = "Get Name", command = getname)
message = Message(frame_2, text = "It is a widgets demo") 

checkbutton_bold.grid(row = 1, column = 1)
radiobutton_red.grid(row = 1, column = 2)
radiobutton_yellow.grid(row = 1, column = 3)

label.grid(row = 2, column = 1)
name.grid(row = 2, column = 2)
button.grid(row = 2, column = 3)
message.grid(row = 2, column = 4)

window.mainloop()


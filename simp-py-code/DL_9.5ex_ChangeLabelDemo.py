from tkinter import *

class Change_Label_Demo:
    def __init__(self):
        window = Tk() # create a window
        window.title("Change_Label_Demo") # assign a title to the window
        frame_1 = Frame(window) # create a frame
        frame_1.pack()
        self.label = Label(frame_1, text = "hello ") # create a label
        
        frame_2 = Frame(window) # create a frame
        frame_2.pack()
        message = Message(frame_2, text = "Please enter text: ")
        
        self.entry_value = StringVar() # create a String variable 
        
        entry = Entry(frame_2, textvariable = self.entry_value) # assingn the entry value a text variable if it is a text if an integer and interger variable
        
        button = Button(frame_2, text = "Change Text", command = self.change_text)
        
        self.v1 = IntVar()
        radio_button1 = Radiobutton(frame_2, bg = "red", text = "Red", variable = self.v1, value = 0) # the two radio button's variable have to be assigned to the same thing inorder to make it optional
        radio_button2 = Radiobutton(frame_2, bg = "yellow", text = "Yellow", variable = self.v1, value = 1)
        
        self.label.grid(row = 1, column = 1)
        message.grid(row = 2, column = 1)
        entry.grid(row = 2, column = 2)
        button.grid(row = 2, column = 3)
        radio_button1.grid(row = 2, column = 4)
        radio_button2.grid(row = 2, column = 5)
        
        window.mainloop() # create an event loop 
    
    def change_text(self):
        if self.v1.get() == 0:
            self.label["fg"] = "red"
        elif self.v1.get() == 1:
            self.label["fg"] = "yellow"
        
        self.label["text"] = self.entry_value.get()

Change_Label_Demo()
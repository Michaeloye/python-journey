from tkinter import *

class Pack_Manager_Demo_1:
    def __init__(self):
        window = Tk()
        label_1 = Label(window, text = "blue", bg = "blue")
        label_2 = Label(window, text = "red", bg = "red")
        label_3 = Label(window, text = "green", bg = "green")
        
        label_1.pack()
        label_2.pack(fill = BOTH, expand = 1) # fill option is used in pack manager to assign where the entity will occupy it can be X, Y, or BOTH... expand option is used to in the pack manager to assign additional space to the widget box
        label_3.pack(fill = BOTH)
        
        window.mainloop()
        
Pack_Manager_Demo_1()

class Pack_Manager_Demo_2:
    def __init__(self):
        window = Tk()
        self.label_1 = Label(window, text = "blue", bg = "blue")
        self.label_2 = Label(window, text = "red", bg = "red")
        self.label_3 = Label(window, text = "green", bg = "green")
        
        self.label_1.pack(side = LEFT) # side option is used in the pack manager to assign where the widgets will be
        self.label_2.pack(side = LEFT, fill = BOTH, expand = 1) # fill option is used in pack manager to assign where the entity will occupy it can be X, Y, or BOTH... expand option is used to in the pack manager to assign additional space to the widget box
        self.label_3.pack(side = LEFT, fill = BOTH)
        
        window.mainloop()
        
Pack_Manager_Demo_2()

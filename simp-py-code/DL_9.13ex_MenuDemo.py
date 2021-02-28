from tkinter import *

class Menu_Demo:
    def __init__(self):
        window = Tk()
        menu_bar = Menu(window) # create a menu in the window
        window.config(menu = menu_bar)
        
        Operation_Menu = Menu(menu_bar, tearoff = 0) # tearoff is set to 0 inorder to prevent the dropdown menu from being detachable 
        menu_bar.add_cascade(label = "operation", menu = Operation_Menu)
        Operation_Menu.add_command(label = "Add")
        Operation_Menu.add_command(label = "Subtract")
        Operation_Menu.add_separator()
        Operation_Menu.add_command(label = "Multiply")
        Operation_Menu.add_command(label = "Subtract")
        
        Exit_Menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "Exit", menu = Exit_Menu)
        Exit_Menu.add_command(label = "Quit")        
        
        window.mainloop()
        
Menu_Demo()

class Menu_Demo:
    def __init__(self):
        window = Tk()
        menu_bar = Menu(window)
        window.config(menu = menu_bar)
        
        Operation_Menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "Operation", menu = Operation_Menu)
        
        Operation_Menu.add_command(label = "Add", command = self.Add)
        Operation_Menu.add_command(label = "Subtract", command = self.Subtract)
        
        Operation_Menu.add_separator()
        
        Operation_Menu.add_command(label = "Multiply", command = self.Multiply)
        Operation_Menu.add_command(label = "Divide", command = self.Divide)
        
        Exit_Menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "Exit", menu = Exit_Menu)
        Exit_Menu.add_command(label = "Quit")
        
        frame_1 = Frame(window)
        frame_1.pack()
        
        label_1 = Label(frame_1, text = "Number 1:")
        self.Number_1 = DoubleVar()
        entry_1 = Entry(frame_1, width = 5, textvariable = self.Number_1, justify = RIGHT)
        
        label_2 = Label(frame_1, text = "Number 2:")
        self.Number_2 = DoubleVar()
        entry_2 = Entry(frame_1, width = 5, textvariable = self.Number_2, justify = RIGHT)
        
        label_3 = Label(frame_1, text = "Result:")
        self.Result = StringVar()
        entry_3 = Entry(frame_1, width = 5, textvariable = self.Result, justify = RIGHT) # answer will be displayed in entry_3
        
        label_1.grid(row = 2, column = 1)
        entry_1.grid(row = 2, column = 2)
        
        label_2.grid(row = 2, column = 3)
        entry_2.grid(row = 2, column = 4)
        
        label_3.grid(row = 2, column = 5)
        entry_3.grid(row = 2, column = 6)
        
        
        window.mainloop()
        
    def Add(self):
        self.Result.set(str(self.Number_1.get() + self.Number_2.get()))
    
    def Subtract(self):
        self.Result.set(str(self.Number_1.get() - self.Number_2.get()))
    
    def Multiply(self):
        self.Result.set(str(self.Number_1.get() * self.Number_2.get()))
    
    def Divide(self):
        self.Result.set(str(self.Number_1.get() / self.Number_2.get()))
        
Menu_Demo()
        


        
        
        
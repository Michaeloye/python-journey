from tkinter import *

class ProcessButtonEvent:
    def __init__(self) :
        window = Tk()
        
        button_yes = Button(window, text = "yes", command = self.pressbutton_yes) #if self.function is not put in command the function would not run that is if only function name is placed 
        
        button_true = Button(window, text = "true", command = self.pressbutton_true)
        
        button_yes.pack()
        button_true.pack()
        
        window.mainloop()
    def pressbutton_yes(self):
        window = Tk()
        
        label = Label(window, text = "You clicked Yes")
        
        label.pack()
        
        window.mainloop()
    def pressbutton_true(self):
        print("You clicked True")
    
       
ProcessButtonEvent() #to invoke the __init__ method
    
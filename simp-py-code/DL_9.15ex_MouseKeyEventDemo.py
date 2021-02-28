from tkinter import *

class MouseKeyEventDemo:
    def __init__(self):
        
        window = Tk()
        window.title("Event Demo")
        
        self.canvas = Canvas(window, width = 500, height = 300, bg = "white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.Process_Mouse_Event)
        
        self.canvas.bind("<Key>", self.Process_Key_Event)
        self.canvas.focus_set() # to give the canvas a border 
        window.mainloop()
        
    def Process_Mouse_Event(self, event):
        print("Position in the screen   ", event.x_root, event.y_root)
        print("Where you clicked   ", event.x, event.y)
        print("what button did you click ?   ", event.num)
        x_axis = event.x
        y_axis = event.y
        if x_axis in range(240, 260) and y_axis in range(240, 260):
            print("Correct")
    def Process_Key_Event(self, event):
        print("Keysym?   ", event.keysym)
        print("Char?   ", event.char)
        print("keycode?   ", event.keycode)

MouseKeyEventDemo()
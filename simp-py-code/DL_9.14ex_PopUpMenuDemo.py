from tkinter import *

class Pop_Up_MenuDemo:
    def __init__(self):
        window = Tk()
        window.title("Pop up menu")
        self.pop_up_menu = Menu(window, tearoff = 0)
        self.pop_up_menu.add_command(label = "Draw a line", command = self.Draw_a_Line)
        self.pop_up_menu.add_command(label = "Draw an oval", command = self.Draw_an_Oval)
        self.pop_up_menu.add_command(label = "Draw a rectangle", command = self.Draw_a_Rectangle)
        self.pop_up_menu.add_command(label = "Clear", command = self.Clear)
        
        self.canvas = Canvas(window, width = 400, height = 300, bg = "white")
        self.canvas.pack()
        
        self.canvas.bind("<Button-3>", self.popup)
        window.mainloop()
        
    def Draw_a_Line(self):
        self.canvas.create_line(10, 10, 190, 90, tags = "line")
    def Draw_an_Oval(self):
        self.canvas.create_oval(10, 10, 190, 90, tags = "oval")
    def Draw_a_Rectangle(self):
        self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect")
    def Clear(self):
        self.canvas.delete("line", "oval", "rect")
    def popup(self, event):
        self.pop_up_menu.post(event.x_root, event.y_root)
        
Pop_Up_MenuDemo()
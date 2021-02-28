from tkinter import *

class Canvas_Demo:
    def __init__(self):
        window = Tk()
        frame_1 = Frame(window)
        frame_1.pack()
        
        self.canvas = Canvas(frame_1, width = 200, height = 100, bg = "white")
        self.canvas.pack()
        
        frame_2 = Frame(window)
        frame_2.pack()
        
        button_rectangle = Button(frame_2, text = "Rectangle", command = self.process_button_rectangle)
        button_oval = Button(frame_2, text = "Oval", command = self.process_button_oval)
        button_arc = Button(frame_2, text = "Arc", command = self.process_button_arc)
        button_polygon = Button(frame_2, text = "Polygon", command = self.process_button_polygon)
        button_line = Button(frame_2, text = "Line", command = self.process_button_line)
        button_string = Button(frame_2, text = "String", command = self.process_button_string)
        button_clear = Button(frame_2, text = "Clear", command = self.process_button_clear)
        
        button_rectangle.grid(row = 1, column = 1)
        button_oval.grid(row = 1, column = 2)
        button_arc.grid(row = 1, column = 3)
        button_polygon.grid(row = 1, column = 4)
        button_line. grid(row = 1, column = 5)
        button_string.grid(row = 1, column = 6)
        button_clear.grid(row = 1, column = 7)
        
        window.mainloop()
    
    def process_button_rectangle(self):
        self.canvas.create_rectangle(10, 10, 200, 100, tags = "rect", fill = "red", activefill = "blue") # fill: assigns color to the shape, activefill: assigns color to the shape when the mouse hovers over if
    def process_button_oval(self):
        self.canvas.create_oval(10, 10, 200, 100, tags = "oval")
    def process_button_arc(self):
        self.canvas.create_arc(10, 10, 200, 100, start = 60, extent = 70, tags = "arc")
    def process_button_polygon(self):
        self.canvas.create_polygon(10, 10, 200, 100, 70, 100, tags = "poly")
    def process_button_line(self):
        self.canvas.create_line(10, 10, 200, 100, tags = "line")
    def process_button_string(self):
        self.canvas.create_text(50, 50, text = "Hello", tags = "string")
    def process_button_clear(self):
        self.canvas.delete("rect", "oval", "arc", "poly", "line", "string")
        
        
Canvas_Demo()
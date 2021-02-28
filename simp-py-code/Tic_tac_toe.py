# Tik tac toe
from tkinter import *
import tkinter.messagebox

class Tiktactoe:
    def __init__(self):
        window = Tk()
        window.title("Tic Tac Toe")
        
        # make a counter that is sensitive to number of times the mouse is clicked

        self.window_counter = 0
        self.window_counter_square_1 = 0
        self.window_counter_square_2 = 0
        self.window_counter_square_3 = 0
        self.window_counter_square_4 = 0
        self.window_counter_square_5 = 0
        self.window_counter_square_6 = 0
        self.window_counter_square_7 = 0
        self.window_counter_square_8 = 0
        self.window_counter_square_9 = 0
        
        # make frames
        frame_1 = Frame(window)
        frame_2 = Frame(window)
        frame_3 = Frame(window)
        frame_4 = Frame(window)
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        
        """the user should decide what to start with x or o"""
        self.button_picked = IntVar()
        radio_button_o = Radiobutton(frame_4, text = "O", font = "Times 13", variable = self.button_picked, value = 0)
        radio_button_x = Radiobutton(frame_4, text = "X", font = "Times 13", variable = self.button_picked, value = 1)
        
        # first row
        self.input_1 = StringVar()
        self.entry_1 = Label(frame_1, textvariable = self.input_1, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_2 = StringVar()
        self.entry_2 = Label(frame_1, textvariable = self.input_2, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_3 = StringVar()
        self.entry_3 = Label(frame_1, textvariable = self.input_3, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        
        # second row
        self.input_4 = StringVar()
        self.entry_4 = Label(frame_2, textvariable = self.input_4, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_5 = StringVar()
        self.entry_5 = Label(frame_2, textvariable = self.input_5, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_6 = StringVar()
        self.entry_6 = Label(frame_2, textvariable = self.input_6, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        
        # third row
        self.input_7 = StringVar()
        self.entry_7 = Label(frame_3, textvariable = self.input_7, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_8 = StringVar()
        self.entry_8 = Label(frame_3, textvariable = self.input_8, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        self.input_9 = StringVar()
        self.entry_9 = Label(frame_3, textvariable = self.input_9, font = "Times 30 bold", bg = "white", width = 3, justify = CENTER, cursor = "arrow")
        
        self.decider = StringVar() # check which is the winner; x or o
        self.label_1 = Label (frame_4, text = "hello")
        # bind the entries to an event
        
        self.entry_1.bind("<Button-1>", self.square_1)
        self.entry_2.bind("<Button-1>", self.square_2)
        self.entry_3.bind("<Button-1>", self.square_3)
        self.entry_4.bind("<Button-1>", self.square_4)
        self.entry_5.bind("<Button-1>", self.square_5)
        self.entry_6.bind("<Button-1>", self.square_6)
        self.entry_7.bind("<Button-1>", self.square_7)
        self.entry_8.bind("<Button-1>", self.square_8)
        self.entry_9.bind("<Button-1>", self.square_9)
        
        self.entry_1.grid(row = 1, column = 1)
        self.entry_2.grid(row = 1, column = 2)
        self.entry_3.grid(row = 1, column = 3)
        self.entry_4.grid(row = 2, column = 1)
        self.entry_5.grid(row = 2, column = 2)
        self.entry_6.grid(row = 2, column = 3)
        self.entry_7.grid(row = 3, column = 1)
        self.entry_8.grid(row = 3, column = 2)
        self.entry_9.grid(row = 3, column = 3)
        
        """the user should decide what to start with x or o ...radio_button_o.grid(row = 4, column = 1)
        radio_button_x.grid(row = 4, column = 2"""
        self.label_1.grid(row = 4, column = 3)
        window.mainloop()
        if self.input_1.get() == "X" and self.input_2.get() == "X" and self.input_3.get() == "X":
            self.decider.set("Nice")
    def square_1(self, event):
        
        self.window_counter_square_1 += 1
        if self.window_counter_square_1 == 1:# to make sure that when a particular label is clicked twice it doesn't change from X to O or from O to X
            self.window_counter += 1
            
            if self.window_counter % 2 == 0:
                self.input_1.set("O")
                
                
            else:
                self.input_1.set("X")
            
            
    def square_2(self, event):
        
        self.window_counter_square_2 += 1
        if self.window_counter_square_2 == 1:
            self.window_counter += 1
            
            if self.window_counter % 2 == 0:
                self.input_2.set("O")
                
                
            else:
                self.input_2.set("X") 
                
    def square_3(self, event):
        
        self.window_counter_square_3 += 1
        if self.window_counter_square_3 == 1:
            self.window_counter += 1
            if self.window_counter % 2 == 0:
                self.input_3.set("O")
                
                
            else:
                self.input_3.set("X") 
                    
    def square_4(self, event):
        
        self.window_counter_square_4 += 1
        if self.window_counter_square_4 == 1:
            self.window_counter += 1
            if self.window_counter % 2 == 0:
                self.input_4.set("O")
                
                
            else:
                self.input_4.set("X") 
                
    def square_5(self, event):
        
        self.window_counter_square_5 += 1
        if self.window_counter_square_5 == 1:
            self.window_counter += 1
            if self.window_counter % 2 == 0:
                self.input_5.set("O")
                
                
            else:
                self.input_5.set("X") 
                
    def square_6(self, event):
        
        self.window_counter_square_6 += 1
        if self.window_counter_square_6 == 1:
            self.window_counter += 1
            if self.window_counter % 2 == 0:
                self.input_6.set("O")
                
            else:
                self.input_6.set("X") 
                
    def square_7(self, event):
        
        self.window_counter_square_7 += 1
        if self.window_counter_square_7 == 1:
            self.window_counter += 1
            
            if self.window_counter % 2 == 0:
                self.input_7.set("O")
                
            else:
                self.input_7.set("X") 
        
    def square_8(self, event):
        
        self.window_counter_square_8 += 1
        if self.window_counter_square_8 == 1:
            self.window_counter += 1
            
            if self.window_counter % 2 == 0:
                self.input_8.set("O")
                
            else:
                self.input_8.set("X") 
                    
    def square_9(self, event):
        
        self.window_counter_square_9 += 1
        if self.window_counter_square_9 == 1:
            self.window_counter += 1
            
            if self.window_counter % 2 == 0:
                self.input_9.set("O")
               
            else:
                self.input_9.set("X") 
                
    
Tiktactoe()
"""
class Tiktactoe:
    def __init__(self):
        window = Tk()
        self.canvas = Canvas(window, bg = "white", width = 300, height = 300)
        self.canvas.pack()
        self.canvas.focus_set()
        
        # draw vertical lines
        self.canvas.create_line(100, 0, 100, 300)
        self.canvas.create_line(200, 0, 200, 300)
        
        # draw horizontal lines
        self.canvas.create_line(0, 100, 300, 100)
        self.canvas.create_line(0, 200, 300, 200)
        
        self.canvas.bind("<Button-1>", self.process_click)
        
        window.mainloop()
    
    def process_click(self, event):
        i = 1
        while i < 9:
            # all vertical boxes by the left
            if (event.x in range(0, 100) and event.y in range(0, 100)):
                answer = self.canvas.create_text(50, 50, text = "X", font = "Times 90 bold", fill = "blue")
                                 
            elif (event.x in range(0, 100) and event.y in range(100, 200)): 
                self.canvas.create_text(50, 150, text = "X", font = "Times 90 bold", fill = "blue")
            elif (event.x in range(0, 100) and event.y in range(200, 300)):            
                self.canvas.create_text(50, 250, text = "X", font = "Times 90 bold", fill = "blue")
            
            # all vertical boxes in the middle
            elif (event.x in range(100, 200) and event.y in range(0, 100)): 
                self.canvas.create_text(150, 50, text = "X", font = "Times 90 bold", fill = "blue")
            elif (event.x in range(100, 200) and event.y in range(100, 200)): 
                self.canvas.create_text(150, 150, text = "X", font = "Times 90 bold", fill = "blue")
            elif (event.x in range(100, 200) and event.y in range(200, 300)):
                self.canvas.create_text(150, 250, text = "X", font = "Times 90 bold", fill = "blue")
            
            # all vertical boxes by the right side
            
            elif (event.x in range(200, 300) and event.y in range(0, 100)):
                self.canvas.create_text(250, 50, text = "X", font = "Times 90 bold", fill = "blue")
            elif (event.x in range(200, 300) and event.y in range(100, 200)): 
                self.canvas.create_text(250, 150, text = "X", font = "Times 90 bold", fill = "blue")
            elif (event.x in range(200, 300) and event.y in range(200, 300)):
                self.canvas.create_text(250, 250, text = "X", font = "Times 90 bold", fill = "blue")            
            i += 1
            
                
                                                                                       
Tiktactoe()"""
"""
window = Tk()

#variable is stored in the window object
window.counter = 0

def clicked():
    window.counter += 1
    L['text'] = 'Button clicked: ' + str(window.counter)
        
b = Button(window, text="Click Me", command=clicked)
b.pack()

L = Label(window, text="No clicks yet.")
L.pack()

window.mainloop()"""




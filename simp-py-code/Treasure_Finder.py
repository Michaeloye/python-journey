"""from tkinter import *

class Treasure:
    def __init__(self):
        window = Tk()
        
        frame = Frame(window)
        frame.pack()
        
        # make a label that shows how close the user is to the answer it is referred to in Found_Treasure function 
        self.label = Label(frame, text = " ") # use self because the label will be referred to in Found_Treasure function
        self.label.grid(row = 2, column = 3)
        
        self.treasure_image = PhotoImage(file = "coca_cola_can.gif")
        self.canvas = Canvas(window, width = 700, height = 500, bg = "white")
        # draw vertical lines from the top of the canvas to the bottom of the canvas
        self.canvas.create_line(100, 0, 100, 500) 
        self.canvas.create_line(200, 0, 200, 500)
        self.canvas.create_line(300, 0, 300, 500)
        self.canvas.create_line(400, 0, 400, 500)
        self.canvas.create_line(500, 0, 500, 500)
        self.canvas.create_line(600, 0, 600, 500)
        
        # draw horizontal lines from the left of the canvas to the right of the canvas
        self.canvas.create_line(0, 100, 700, 100)
        self.canvas.create_line(0, 200, 700, 200)
        self.canvas.create_line(0, 300, 700, 300)
        self.canvas.create_line(0, 400, 700, 400)
        self.canvas.focus_set()
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.Found_Treasure)
        
        window.mainloop()
    def Found_Treasure(self, event):
        # answer_x is in range 200 to 300 and answer_y is in range 200 and 300
        
        print(event.x, event.y)
        
        if (event.x in range(200, 300 + 1) and (event.y in range(200, 300 + 1))):
            self.label["text"] = "Congratulations you found the treasure"
            self.canvas.create_image(250, 250, image = self.treasure_image)
        
        # handling the top left of the answer square and bottom right of the answer square
        elif (event.x in range(100, 200 + 1) and event.y in range(100, 200 + 1)) or (event.x in range(300, 400 + 1) and event.y in range(300, 400 + 1)):
            self.label["text"] = "Hotter"
        
        # handling the square above the answer square and the square below the answer square
        elif (event.x in range(200, 300 + 1) and event.y in range(100, 200 + 1)) or (event.x in range(200, 300 + 1) and event.y in range(300, 400 + 1)):
            self.label["text"] = "Hotter"
        
        # handling the square left of the answer square and the square right of the answer square
        elif (event.x in range(100, 200 + 1) and event.y in range(200, 300 + 1)) or (event.x in range(300, 400 + 1) and event.y in range(200, 300 + 1)):
            self.label["text"] = "Hotter"
        
        # handling the square top right of the answer square and the square bottom left respectively
        elif (event.x in range(300, 400 + 1) and event.y in range(100, 200 + 1)) or (event.x in range(100, 200 + 1) and event.y in range(300, 400 + 1)):
            self.label["text"] = "Hotter"
        
        # handling all the extreme Left squares
        elif ((event.x in range(0, 100 + 1)) and ((event.y in range(0, 100 + 1)) or (event.y in range(100, 200 + 1)) or (event.y in range(200, 300 + 1)) or (event.y in range(300, 400 + 1)) or (event.y in range(400, 500 + 1)))):
            self.label["text"] = "Hot"
        
        # handling all the topmost squares
        elif((event.y in range(0, 100 + 1)) and ((event.x in range(100, 200 + 1)) or (event.x in range(200, 300 + 1)) or (event.x in range(300, 400 + 1)) or (event.x in range(400, 500 + 1)))):
            self.label["text"] = "Hot"
        
        # handling all bottom squares
        elif((event.y in range(400, 500 + 1)) and ((event.x in range(100, 200 + 1)) or (event.x in range(200, 300 + 1)) or (event.x in range(300, 400 + 1)) or (event.x in range(400, 500 + 1)))):
            self.label["text"] = "Hot"
        
        # handling all squares one squares away from the answer square
        elif ((event.x in range(400, 500 + 1)) and ((event.y in range(100, 200 + 1)) or (event.y in range(200, 300 + 1)) or (event.y in range(300, 400 + 1)))):
            self.label["text"] = "Hot"
            
        # handling all squares two squares away from the answer square
        elif ((event.x in range(500, 600 + 1)) and ((event.y in range(0, 100 + 1)) or (event.y in range(100, 200 + 1)) or (event.y in range(200, 300 + 1)) or (event.y in range(300, 400 + 1)) or (event.y in range(400, 500 + 1)))):
            self.label["text"] = "Cold"        
        
        # handling all right most squares
        elif ((event.x in range(600, 700 + 1)) and ((event.y in range(0, 100 + 1)) or (event.y in range(100, 200 + 1)) or (event.y in range(200, 300 + 1)) or (event.y in range(300, 400 + 1)) or (event.y in range(400, 500 + 1)))):
            self.label["text"] = "Colder"
                                                    
Treasure()"""
from tkinter import *
from random import *
class Treasure:
    def __init__(self):
        self.answer_x = randrange(50, 650, 100) # get random integers 50, 150, 250, ... 650
        self.answer_y = randrange(50, 450, 100) # get random integers 50, 150, 250, ... 450     
        
        window = Tk()
        
        frame = Frame(window)
        frame.pack()
        
        # make a label that shows how close the user is to the answer it is referred to in Found_Treasure function 
        self.label = Label(frame, text = " ") # use self because the label will be referred to in Found_Treasure function
        self.label.grid(row = 2, column = 3)
        
        self.treasure_image = PhotoImage(file = "coca_cola_can.gif")
        self.canvas = Canvas(window, width = 700, height = 500, bg = "white")
        # draw vertical lines from the top of the canvas to the bottom of the canvas
        self.canvas.create_line(100, 0, 100, 500) 
        self.canvas.create_line(200, 0, 200, 500)
        self.canvas.create_line(300, 0, 300, 500)
        self.canvas.create_line(400, 0, 400, 500)
        self.canvas.create_line(500, 0, 500, 500)
        self.canvas.create_line(600, 0, 600, 500)
        
        # draw horizontal lines from the left of the canvas to the right of the canvas
        self.canvas.create_line(0, 100, 700, 100)
        self.canvas.create_line(0, 200, 700, 200)
        self.canvas.create_line(0, 300, 700, 300)
        self.canvas.create_line(0, 400, 700, 400)
        self.canvas.focus_set()
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.Found_Treasure)
        
        window.mainloop()
           
    def Found_Treasure(self, event):
        
        # if answer_x and answer_y are inside the function each time the function is called a new random number will be generated
        
        print(self.answer_x, self.answer_y)
        print(event.x, event.y)
        
        if (event.x in range(self.answer_x - 50, self.answer_x + 51) and (event.y in range(self.answer_y -50, self.answer_y + 51))):
            self.label["text"] = "Congratulations you found the treasure"
            self.canvas.create_image(self.answer_x, self.answer_y, image = self.treasure_image)
        
            """ Hotter """
        # handling the left of the answer square and right of the answer square
        elif (event.x in range(self.answer_x - 150, self.answer_x - 49) and event.y in range(self.answer_y - 50, self.answer_y + 51 )) or (event.x in range(self.answer_x + 50, self.answer_x + 151) and (event.y in range(self.answer_y - 50, self.answer_y + 51))):
            self.label["text"] = "Hotter"
        
        # handling the square above the answer square and the square below the answer square
        elif (event.x in range(self.answer_x - 50, self.answer_x + 51) and event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.x in range(self.answer_x - 50, self.answer_x + 51) and event.y in range(self.answer_y + 50, self.answer_y + 151)):
            self.label["text"] = "Hotter"
        
        # handling the square left top of the answer square and the square right top of the answer square respectively
        elif (event.x in range(self.answer_x - 150, self.answer_x - 49) and event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.x in range(self.answer_x + 50, self.answer_x + 151) and event.y in range(self.answer_y - 150, self.answer_y - 49)):
            self.label["text"] = "Hotter"
        
        # handling the square bottom left of the answer square and the square bottom right of the answer square respectively
        elif (event.x in range(self.answer_x - 150, self.answer_x - 49) and event.y in range(self.answer_y + 50, self.answer_y + 151)) or (event.x in range(self.answer_x + 50, self.answer_x + 151) and event.y in range(self.answer_y + 50, self.answer_y + 151)):
            self.label["text"] = "Hotter"
            """ Hotter """
            
            """ Hot"""
        # handling all the extreme Left squares
        elif ((event.x in range(self.answer_x -250, self.answer_x - 149)) and ((event.y in range(self.answer_y - 250, self.answer_y - 149)) or (event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.y in range(self.answer_y - 50, self.answer_y + 51)) or (event.y in range(self.answer_y + 50, self.answer_y + 151)) or (event.y in range(self.answer_y + 150 , self.answer_y + 251)))):
            self.label["text"] = "Hot"
        
        # handling all the extreme Right squares
        elif ((event.x in range(self.answer_x + 150, self.answer_x + 251)) and ((event.y in range(self.answer_y - 250, self.answer_y - 149)) or (event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.y in range(self.answer_y - 50, self.answer_y + 51)) or (event.y in range(self.answer_y + 50, self.answer_y + 151)) or (event.y in range(self.answer_y + 150 , self.answer_y + 251)))):
            self.label["text"] = "Hot"
        
        # handling all the topmost squares
        elif((event.y in range(self.answer_y - 250, self.answer_y - 149)) and ((event.x in range(self.answer_x - 150, self.answer_x - 51)) or (event.x in range(self.answer_x - 50, self.answer_x + 51)) or (event.x in range(self.answer_x + 50, self.answer_x + 151)))):
            self.label["text"] = "Hot"
        
        # handling all bottom squares
        elif((event.y in range(self.answer_y + 150, self.answer_y + 251)) and ((event.x in range(self.answer_x - 150, self.answer_x - 51)) or (event.x in range(self.answer_x - 50, self.answer_x + 51)) or (event.x in range(self.answer_x + 50, self.answer_x + 151)))):
            self.label["text"] = "Hot"
            """" Hot """
            
            """ Cold """
        # handling squares two squares to the left of the answer square
        elif ((event.x in range(self.answer_x - 350, self.answer_x - 249)) and ((event.y in range(self.answer_y - 350, self.answer_y - 249)) or (event.y in range(self.answer_y - 250, self.answer_y - 149)) or (event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.y in range(self.answer_y - 50, self.answer_y + 51)) or (event.y in range(self.answer_y + 50, self.answer_y + 151)) or (event.y in range(self.answer_y + 150 , self.answer_y + 251))or (event.y in range(self.answer_y + 250, self.answer_y + 351)))):
            self.label["text"] = "Cold"
            
        # handling squares two squares to the right of the answer square
        elif ((event.x in range(self.answer_x + 250, self.answer_x + 351)) and ((event.y in range(self.answer_y - 350, self.answer_y - 249)) or (event.y in range(self.answer_y - 250, self.answer_y - 149)) or (event.y in range(self.answer_y - 150, self.answer_y - 49)) or (event.y in range(self.answer_y - 50, self.answer_y + 51)) or (event.y in range(self.answer_y + 50, self.answer_y + 151)) or (event.y in range(self.answer_y + 150 , self.answer_y + 251))or (event.y in range(self.answer_y + 250, self.answer_y + 351)))):
            self.label["text"] = "Cold"   
        
        # handling squares two  squares top of the answer square
        elif ((event.y in range(self.answer_y - 350, self.answer_y - 249)) and ((event.x in range(self.answer_x - 250, self.answer_x - 149)) or (event.x in range(self.answer_x - 150, self.answer_x - 49)) or (event.x in range(self.answer_x - 50, self.answer_x + 51)) or (event.x in range(self.answer_x + 50, self.answer_x + 151)) or (event.x in range(self.answer_x + 150, self.answer_x + 251)))):
            self.label["text"] = "Cold"
        
        # handling squares tow squares below the answer square
        elif ((event.y in range(self.answer_y + 250, self.answer_y + 351)) and ((event.x in range(self.answer_x - 250, self.answer_x - 149)) or (event.x in range(self.answer_x - 150, self.answer_x - 49)) or (event.x in range(self.answer_x - 50, self.answer_x + 51)) or (event.x in range(self.answer_x + 50, self.answer_x + 151)) or (event.x in range(self.answer_x + 150, self.answer_x + 251)))):
            self.label["text"] = "Cold"
            """ Cold """
            
            """ Colder """
        else:
            self.label["text"] = "Colder"
            
            """ Colder """
        
Treasure()            


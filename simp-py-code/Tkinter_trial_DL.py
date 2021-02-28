from tkinter import * # Import all definitions from tkinter

window = Tk() # Create a window
label = Label(window, text = "Welcome to Python") # Create a label
button = Button(window, text = "Click Me") # Create a button
label.pack() # Place the label in the window
button.pack() # Place the button in the window

window.mainloop()

window = Tk()
label = Label(window, text = "Welcome to Python", cursor = "plus", justify = LEFT)
button = Button(window, text = "Click")
button.pack() # pack manager packs it row by row therefore the button comes before the label
label.pack()

window.mainloop() # This creates an event loop which processes the events until you close the main window

# so therefore you have to create a window again using window = Tk() else it would give an error
def pressbutton():
    label["text"] = "Hi" # to change the text written... from "thank you" to "Hi"

window = Tk()
label = Label(window, text = "Hello there")
button = Button(window, text = "Thank you", bg = "skyblue",command = pressbutton)
label.pack()
button.pack()
window.mainloop() 

window = Tk()
frame1 = Frame(window)
frame1.pack()
label = Label(frame1, text = "Hello")
button = Button(frame1, text = "okay")
label.grid(row = 1, column = 1)
button.grid(row = 1, column = 2)
window.mainloop()


window = Tk() # Create a window
window.title("Grid Manager Demo") # Set title

message = Message(window, text ="This Message widget occupies three rows and two columns")
message.grid(row = 1, column = 1, rowspan = 3, columnspan = 2)
Label(window, text = "First Name:").grid(row = 1, column = 3)
Entry(window).grid(row = 1, column = 4, padx = 5, pady = 5)
Label(window, text = "Last Name:").grid(row = 2, column = 3)
Entry(window).grid(row = 2, column = 4)
Button(window, text = "Get Name").grid(row = 3, padx = 5, pady = 5, column = 4, sticky = E)
image_1 = PhotoImage(file = "download.gif")
canvas = Canvas(window, width = 300, height = 400)
canvas.create_image(70,90, image = image_1)
canvas.grid(row = 4, column = 7)
window.mainloop() # Create an event loop



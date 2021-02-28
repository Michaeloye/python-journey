from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
class FileEditor:
    def __init__(self):
        window = Tk()
        menu_bar = Menu(window)
        window.config(menu = menu_bar) # Display menu bar
        
        # create a pulldown menu and add it to the menu bar
        operation_menu = Menu(menu_bar, tearoff = 0)
        menu_bar.add_cascade(label = "File", menu = operation_menu)
        # after a cascade has been created add command to the cascade
        operation_menu.add_command(label = "Open", command = self.openfile) # add command (the function to execute the command)
        operation_menu.add_command(label = "Save", command = self.savefile)
        
        # add frame
        frame = Frame(window)
        frame.pack()
        
        # add scroll to the vertical side of the GUI 
        
        scroll_bar = Scrollbar(frame)
        scroll_bar.pack(side = RIGHT, fill = Y)
        
        # add text to the GUI
        self.text = Text(frame, width = 40, height = 30, wrap = WORD, yscrollcommand = scroll_bar.set) # use "self" because text will be referred to in later lines
        self.text.pack()
        scroll_bar.config(command = self.text.yview)

        window.mainloop()
        
    def openfile(self):
        file_to_read = askopenfilename()
        infile = open(file_to_read, "r")
        self.text.insert(END, infile.read()) # read from the file and show it in the text widget     
        infile.close()
    def savefile(self):
        file_to_save = asksaveasfilename()
        outfile = open(file_to_save, "w")
        
        # write to the file
        
        outfile.write(self.text.get(1.0, END)) # write the texts that are in the text widget into the file to be saved
        outfile.close()
FileEditor()

# The menu bar is created so as to allow the user decide what to do. The askopenfilename() in line 34 calls out a dialog box to enable the user choose
#what file to be opened the text from the file is read and written in the text widget line 36.
# The asksaveasfilename() in line 39 calls out a dialog box to enable the user type in the name the document should be saved as, if the document
#existed before the same name can be typed in order to overwrite the document, the file is then saved in by writing the texts in the text widget onto
#the file selected to be saved or to a new file, the text from text widget is gotten by using the .get() method in line 44
# This program creates a text area using the Text widget tied with a scrollbar (line 23 - line 29) the text widget and scrollbar are placed in frame1
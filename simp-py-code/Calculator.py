from tkinter import *
from math import *
class Calculator:
    def __init__(self):
        # append the inputs to the list
        self.list_1 = []
        window = Tk()
        window.title("Calculator")
        menu_bar = Menu(window) 
        window.config(menu = menu_bar) # Display menu bar
        
        # Create pull down menu and add to the menu bar
        mode_menu = Menu(menu_bar, tearoff = 0) # tearoff is used to prevent the menu from being removed
        menu_bar.add_cascade(label = "Mode", menu = mode_menu)
        mode_menu.add_command(label = "Comp", command = self.Comp) # the command Comp is the normal settings of a calculator
        mode_menu.add_command(label = "Equation", command = self.Equation) # the command Equation is the equation mode 
        
        #create frames
        frame_1 = Frame(window)
        frame_2 = Frame(window)
        frame_3 = Frame(window)
        frame_4 = Frame(window)
        frame_5 = Frame(window)
        frame_6 = Frame(window)
        frame_7 = Frame(window)
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        frame_4.pack()
        frame_5.pack()
        frame_6.pack()
        frame_7.pack()
        
        # create entry
        self.input_1 = StringVar()
        self.entry_1 = Entry(frame_1, textvariable = self.input_1, font = "Arial 40 bold", width = 50)
        self.result = StringVar()
        self.entry_2 = Label(frame_2, textvariable = self.result, font = "Arial 40 bold", bg = "white", width = 42, justify = LEFT)
        
        self.entry_1.grid(row = 1, column = 1)
        self.entry_2.grid(row = 2, column = 1, sticky = E)
        
        # create the calculator buttons
        button_AC = Button(frame_3, text = "AC", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.AC)   
        
        button_7 = Button(frame_4, text = "7", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_7)
        button_8 = Button(frame_4, text = "8", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_8)
        button_9 = Button(frame_4, text = "9", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_9)
        button_open_bracket = Button(frame_4, text = "(", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_open_bracket)
        button_close_bracket = Button(frame_4, text = ")", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_close_bracket)
        button_sin = Button(frame_4, text = "sin", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_sin)
        button_sin_inverse = Button(frame_4, text = "asin", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_sin_inverse)
        
        button_4 = Button(frame_5, text = "4", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_4)
        button_5 = Button(frame_5, text = "5", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_5)
        button_6 = Button(frame_5, text = "6", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_6)
        button_multiplication = Button(frame_5, text = "X", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_multiplication)
        button_division = Button(frame_5, text = "/", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_division)
        button_cos = Button(frame_5, text = "cos", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_cos)
        button_cos_inverse = Button(frame_5, text = "acos", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_cos_inverse)
        
        button_1 = Button(frame_6, text = "1", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_1)
        button_2 = Button(frame_6, text = "2", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_2)
        button_3 = Button(frame_6, text = "3", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_3)
        button_subtraction = Button(frame_6, text = "-", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_subtraction)
        button_addition = Button(frame_6, text = "+", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_addition)
        button_tan = Button(frame_6, text = "tan", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_tan)
        button_tan_inverse = Button(frame_6, text = "atan", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_tan_inverse)        
        
        button_0 = Button(frame_7, text = "0", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_0)
        button_decimal_point = Button(frame_7, text = ".", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.button_decimal_point)
        button_del = Button(frame_7, text = "Del", width = 10, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.Del)
        button_equal = Button(frame_7, text = "=", width = 12, font = "Arial 19 bold", bg = "grey", fg = "white", command = self.answer)
        button_log = Button(frame_7, text = "log", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white")
        button_log_inverse = Button(frame_7, text = "log-1", width = 5, font = "Arial 19 bold", bg = "grey", fg = "white")        
        
        
        # Arrange the buttons 

        button_AC.grid(row = 3, column = 1, sticky = W)
        
        button_7.grid(row = 5, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_8.grid(row = 5, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_9.grid(row = 5, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_open_bracket.grid(row = 5, sticky = W, column = 4, ipadx = 10, ipady = 10)
        button_close_bracket.grid(row = 5, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_sin.grid(row = 5, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_sin_inverse.grid(row = 5, column = 7, sticky = W, ipadx = 10, ipady = 10)
        
        button_4.grid(row = 6, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_5.grid(row = 6, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_6.grid(row = 6, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_multiplication.grid(row = 6, column = 4, sticky = W, ipadx = 10, ipady= 10)
        button_division.grid(row = 6, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_cos.grid(row = 6, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_cos_inverse.grid(row = 6, column = 7, sticky = W, ipadx = 10, ipady = 10)
        
        button_1.grid(row = 7, column = 1, sticky = W, ipadx = 10, ipady= 10)
        button_2.grid(row = 7, column = 2, sticky = W, ipadx = 10, ipady= 10)
        button_3.grid(row = 7, column = 3, sticky = W, ipadx = 10, ipady= 10)
        button_subtraction.grid(row = 7, column = 4, sticky = W, ipadx = 10, ipady = 10)
        button_addition.grid(row = 7 , column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_tan.grid(row = 7, column = 6, sticky = W, ipadx = 10, ipady = 10)
        button_tan_inverse.grid(row = 7, column = 7, sticky = W, ipadx = 10, ipady = 10)        
        
        button_0.grid(row = 8, column = 1, sticky = W, ipadx = 10, ipady = 10)
        button_decimal_point.grid(row = 8, column = 2, sticky = W, ipadx = 10, ipady = 10)
        button_del.grid(row = 8, column = 3, sticky = W, ipadx = 10, ipady = 10)
        button_equal.grid(row = 8, column = 4, sticky = W, ipadx = 10, ipady = 10)
        button_log.grid(row = 8, column = 5, sticky = W, ipadx = 10, ipady = 10)
        button_log_inverse.grid(row = 8, column = 6, sticky = W, ipadx = 10, ipady = 10)         
        
        window.mainloop()
        
        
    def Comp(self):
        pass
    def Equation(self):
        pass
    def button_7(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(7)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.insert(self.entry_1.index(INSERT), 7)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 7)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)       
    
    def button_8(self):
                 
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(8)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here"""
            self.list_1.append(8)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
            print("hello")
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 8)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)        
        
        
        
    def button_9(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(9)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(9)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 9)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)       
    
    def button_open_bracket(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)              
    
    def button_close_bracket(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(")")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(")")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), ")")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)           
    
    def button_sin(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("sin(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("sin(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "sin(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)                
    
    def button_sin_inverse(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("asin(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("asin(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "asin(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)                    
    
    def button_4(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(4)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(4)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 4)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)       
    
    def button_5(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(5)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(5)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 5)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)        
    def button_6(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(6)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(6)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 6)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)               
    
    def button_multiplication(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("*")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("*")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "*")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_division(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("/")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("/")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "/")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_cos(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("cos(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("cos(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "cos(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_cos_inverse(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("acos(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("acos(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "acos(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)                  
    
    def button_1(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(1)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(1)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 1)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_2(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(2)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(2)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 2)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_3(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(3)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(3)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 3)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
    def button_subtraction(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("-")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("-")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "-")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_addition(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("+")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("+")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "+")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_tan(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("tan(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("tan(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "tan(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_tan_inverse(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append("atan(")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append("atan(")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), "atan(")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)                     
    
    def button_0(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(0)
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(0)
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), 0)
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def button_decimal_point(self):
        # to make it possible for the user to type where the cursor is
        if self.entry_1.index(INSERT) == 0:
            self.list_1.append(".")
            
        elif self.entry_1.index(INSERT) == (len(self.list_1)):
            """Fix the problem here... going to the num before the last num"""
            self.list_1.append(".")
            # this to make the cursor move if the cursor is on the last elememt
            
            self.entry_1.icursor(END)
            # or self.entry_1.icursor(len(self.list_1))
        
        else:
            self.list_1.insert(self.entry_1.index(INSERT), ".")
            self.entry_1.icursor(self.entry_1.index(INSERT) + 1)
        
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)      
        
    def AC(self):
        self.entry_1.delete(0, END) # delete everything inputed in the entry from the first index to the last index 
        # or
        # self.result.set("")
        
        # Working with lists therefore need to clear the list for the AC button to work properly if this is not done even after using the AC button 
        # once any other entry button is clicked the whole previously entered data will reappear
        self.list_1.clear()
        
    def Del(self):
        # removing the last data in the list 
        # del what is before the cursor
        self.list_1.remove(self.list_1[self.entry_1.index(INSERT) - 1])
        
        # to make the cursor move when the character is deleted
        self.entry_1.icursor(self.entry_1.index(INSERT) - 1)
        
        # showing the list_1 in the entry
        self.input_1.set(self.list_1)
        
        
        # prevent the entry from scattering when the del button is pressed
        processed_form = ""
        for element in self.list_1:
            processed_form += str(element)        
        # set the input to the processed form
        self.input_1.set(processed_form)         
    
    
    
    # process the input
    def process_input(self):
        # since list is used to store the inputs this is to prevent the result from giving the exact same input
        processed_form = ""
        # for element in self.list_1.index("tan(")
        for element in self.list_1:
            processed_form += str(element)
        try:
            if "tan(" in processed_form:
                
                answer = eval(processed_form.replace("tan(", "tan(radians("))
            else:
                answer = eval(processed_form)
            return answer
        except:
            return "Error"
    def answer(self):
        self.result.set((self.process_input()))
    
Calculator()

# How to handle sin to give answer as a calculator in degrees mode
# to get answer of sin inverse in degrees
print(asin(1) * 180/pi)
""" identifing where the cursor is in the entry 
window = Tk()
entry_1 = Entry(window)
entry_1.pack()
print(entry_1.index(INSERT))
window.mainloop()"""
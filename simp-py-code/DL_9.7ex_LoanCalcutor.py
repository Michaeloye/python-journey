from tkinter import *

class Loan_Calculator:
    def __init__(self):
        window = Tk()
        
        
        label_1 = Label(window, text = "Annual Interest Rate")
        self.Annual_Interest_Rate = DoubleVar()
        entry_1 = Entry(window, textvariable = self.Annual_Interest_Rate, justify = RIGHT)
        
        label_2 = Label(window, text = "Number of Years",)
        self.Number_of_Years = DoubleVar()
        entry_2 = Entry(window, textvariable = self.Number_of_Years, justify = RIGHT)
        
        label_3 = Label(window, text = "Loan Amount")
        self.Loan_Amount = DoubleVar()
        entry_3 = Entry(window, textvariable = self.Loan_Amount, justify = RIGHT)
        
        label_4 = Label(window, text = "Monthly Payment")
        self.label_5 = Label(window, text = "", justify = RIGHT) # use self because label_5 will be referred to in a function
        
        label_6 = Label(window, text = "Total Payment")
        self.label_7 = Label(window, text = "", justify = RIGHT) # use self because label_7 will be referred to in a function
        
        button = Button(window, text = "Compute Payment", command = self.Compute_Payment)
        
        label_1.grid(row = 1, column = 1, sticky = W)
        entry_1.grid(row = 1, column = 2,)
        
        label_2.grid(row = 2, column = 1)
        entry_2.grid(row = 2, column = 2)
        
        label_3.grid(row = 3, column = 1, sticky = W)
        entry_3.grid(row = 3, column = 2)
        
        label_4.grid(row = 4, column = 1, sticky = W)
        self.label_5.grid(row = 4, column = 2, sticky = E) 
        
        label_6.grid(row = 5, column = 1, sticky = W)
        self.label_7.grid(row = 5, column = 2, sticky = E)
        
        button.grid(row = 6, column = 2)
        window.mainloop()
    def Compute_Payment(self):
        monthly_payment = self.getMonthly_Payment(self.Annual_Interest_Rate.get()/1200, self.Number_of_Years.get(), self.Loan_Amount.get())
        total_payment = monthly_payment * 12 * self.Number_of_Years.get()
        self.label_5["text"] = str(monthly_payment)
        self.label_7["text"] = str(total_payment)
    def getMonthly_Payment(self, Monthly_Interest_Rate, Number_of_Years, Loan_Amount):
        monthlyPayment = Loan_Amount * Monthly_Interest_Rate / (1- 1 / (1 + Monthly_Interest_Rate) ** (Number_of_Years * 12))
        return monthlyPayment        
        
    
    

Loan_Calculator()
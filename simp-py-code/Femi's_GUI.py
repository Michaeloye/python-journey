#MY FIRST GUI APP
#LOAN CALCULATOR
from tkinter import *
class LoanCalculator:
    def __init__(self):
        window=Tk()
        Label(window,text="LOAN CALCULATOR\nBY David Oluwafemi",font="Times 8 bold italic").pack(side=TOP)
        frame=Frame(window)
        frame.pack()
        Label(frame,text="Annual Interest Rate:",font="Times 8 normal").grid(row=1,column=1,sticky=W)
        Label(frame,text="Number of Years:",font="Times 8 normal").grid(row=2,column=1,sticky=W)
        Label(frame,text="Loan Amount:",font="Times 8 normal").grid(row=3,column=1,sticky=W)
        Label(frame,text="Monthly Payment:",font="Times 8 normal").grid(row=4,column=1,sticky=W)
        Label(frame,text="Total Payment:",font="Times 8 normal").grid(row=5,column=1,sticky=W)
        self.AIR=StringVar()
        Entry(frame,textvariable=self.AIR,font="Times 8 normal italic").grid(row=1,column=2,sticky=E)
        self.NOY=StringVar()
        Entry(frame,textvariable=self.NOY,font="Times 8 normal italic").grid(row=2,column=2,sticky=E)
        self.LA=StringVar()
        Entry(frame,textvariable=self.LA,font="Times 8 normal italic").grid(row=3,column=2,sticky=E)
        self.MP=StringVar()
        Label(frame,textvariable=self.MP,font="Times 8 normal italic").grid(row=4,column=2,sticky=E)
        self.TP=StringVar()
        Label(frame,textvariable=self.TP,font="Times 8 normal italic").grid(row=5,column=2,sticky=E)
        Button(frame,text="Compute Payment",command=self.computePayment,font="Times 8 normal italic").grid(row=6,column=2,sticky=E)
        
        window.mainloop()
    
    
    def computePayment(self):
        monthlyPayment=self.getMonthlyPayment(float(self.LA.get()),float(self.AIR.get())/1200,int(self.NOY()))
        self.MP.set(format(monthlyPayment,"10.2f"))
        totalPayment = float(self.MP.get()) * 12 * int(self.NOY.get())
        self.TP.set(format(totalPayment,"10.2f"))
    def getMonthlyPayment(self,lA,aIR,nOY):
        monthlyPayment = lA * mIR / (1-1 / (1 + mIR) ** (nOY *  12))
        return monthlyPayment
LoanCalculator()

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import pandas as pd
import numpy as np

class UI(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.width= 900
        self.height= 500
        self.canvas = Canvas(self, width = self.width, height = self.height)
        self.canvas.pack()
        #self.info= PhotoImage(file='img/info.png')
        
        # monthly income, monthly expense, current age, retirement age, student loan amount left, [years to pay off student loan], car loan, mortgage]
        # we won't worry about mortgage and car loan 
        inputs = [100,20,10,12,100,[10,20,30],4,5]
        moving_avg = [0.4,0.4,]
        self.graph(self.width,self.height,inputs,moving_avg)


    # principal is how much you borrowed
    def simpleIntRate(principal,rate,years):
        dailyRate = rate/365
        daily_int = principal*dailyRate
        # assuming month is 30 day cycle
        month_pay = daily_int*30
        year_int = month_pay*12
        return year_int*years

# double check unsure about this one
    def compoundIntRate(principal,rate,years): 
        new_Principal = principal
        dailyRate = rate/365
        totalInterest = principal*dailyRate
        # assuming a month is a 30 day cycle
        total = 0
        interest = 0
        for i in range(0,30):
            interest = new_Principal*dailyRate
            new_Principal += interest
            total += interest
        return total*years

# yearVect is a vector of possible years to repay the loan default/baseline is 10
# we can also add to the length of th vector too 
    def amortizedStudentLoan(principal,rate,yearVect,fedLoan):
        loan_projections = []
        amt = 0
        total = 0
        annuity = 0
        # first value in yearVect should be default 10 years
        for i in range(0,len(yearVect)): 
            # its a federal loan
            if (fedLoan):
                amt = simpleIntRate(principal,rate,yearVect[i])
            
            else:
                amt = compoundIntRate(principal,rate,yearVect[i])
        
            total = principal + amt
            annuity = total/(yearVect[i]*12)
            loan_projections.append(annuity)
    
        for i in range(0,len(loan_projections)):
            print(loan_projections[i])


    def retirement(monthlyExp,ma_sp,post_retire_yr, pre_retire_yr):
        infl = 0.025
        totalExp = 0
        annualExp = monthlyExp*12
        base_annualExp = annualExp*((1+infl)**pre_retire_yr)
    
        for i in range(0,post_retire_yr):
            base_annualExp = base_annualExp*(1+infl)
            totalExp += base_annualExp
        
        # totalExp is the amount needed at retirement to live until death
        
        # total amount divided into equal segments
        part = totalExp/pre_retire_yr 
    
        # array that stores savings at each time period
        savings = []
        for i in range(0,pre_retire_yr):
        # subtract by 1 due to indexing in the exponent
            discounts = (1 + ma_sp[i])**(pre_retire_yr-i-1)
            savings.append(part/discounts)
    
    
    # first savings amount is 1st payment amount... till last savings amount
    #print out the numbers for savings
        for i in range(0,len(savings)):
            print("Year", i+1)
            print(": ",savings[i])
            
        return savings

    # a vector inputs storing information user inputs
    def graph(self,width,height,inputs,moving_avg):
        self.canvas.create_rectangle(0,0,width,height,fill="medium sea green",width=0)
        self.canvas.create_rectangle(width/12,height/8,11*width/12,11*height/12,fill="white")
        
        
        # retirement fields filled out 
        if (inputs[2]!=0 and inputs[3]!=0):
            death_age = 80
           # savings = retirement(inputs[0],moving_avg,death_age-inputs[3],inputs[3]-inputs[2])
           #for i in range(0,len(savings)):
                #canvas.create_oval()
            self.canvas.create_text(width/2, height/15, text="Annual Retirement Savings",font="Arial 20 bold")
            
        # this is for student loans( being a bit lazy here)
        else:
            principal = inputs[4]
            #an array here 
            years = inputs[5]
            self.canvas.create_text(width/2, height/15, text="Student Loan Payments",font="Arial 20 bold")
            for i in range(0,len(inputs[)
            self.canvas.create_text()
            
            
                
        
        


predUI = UI()
predUI.mainloop()
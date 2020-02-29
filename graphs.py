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
        
        # monthly income, monthly expense, current age, retirement age, student loan amount left, [years to pay off student loan],rate, car loan, mortgage]
        # we won't worry about mortgage and car loan 
        inputs = [100,20,58,60,100,[10,20,30],0.04,5]
        moving_avg = [0.4,0.4,]
        self.graph(self.width,self.height,inputs,moving_avg)


    # principal is how much you borrowed
    def simpleIntRate(self,principal,rate,years):
        dailyRate = rate/365
        daily_int = principal*dailyRate
        # assuming month is 30 day cycle
        month_pay = daily_int*30
        year_int = month_pay*12
        return year_int*years

# double check unsure about this one
    def compoundIntRate(self,principal,rate,years): 
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
    def amortizedStudentLoan(self,principal,rate,yearVect,fedLoan):
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
        
        return loan_projections


    def retirement(self,monthlyExp,ma_sp,post_retire_yr, pre_retire_yr):
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
        print(pre_retire_yr)
        print(len(ma_sp))
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
        
        # save button 
        self.canvas.create_rectangle(width-50,10,width-10,50,fill="white")
        self.canvas.create_text(width-30,30,text="Save",font="Arial 10 bold")
        
        # back button 
        #self.canvas.create_rectangle(width-30,10,)
        
        # retirement fields filled out 
        if (inputs[2]!=0 and inputs[3]!=0):
            death_age = 80
            savings = self.retirement(inputs[0],moving_avg,death_age-inputs[3],inputs[3]-inputs[2])
           #for i in range(0,len(savings)):
                #canvas.create_oval()
            self.canvas.create_text(width/2, height/15, text="Annual Retirement Savings",font="Arial 20 bold")
            diff = 11*width/12 - (width/12)
            num = inputs[3]-inputs[2]
            
            space = diff/(num+1)
            height_range = (11*height/12 - height/8) -10
            for i in range(0,len(savings)):
                self.canvas.create_text((width/12)+space*(i+1),height-height/20,text = str(i+1),font="Arial 15 bold")
                self.canvas.create_oval((width/12) + (space*(i+1)) -5 ,height/2 -5,(width/12) + space*(i+1)+5,height/2 +5,fill="black")
                #self.canvas.create_text((width/12) + space*(i+1),height/2,text=str(savings[i]),font="Arial 10 bold")
                self.canvas.create_text((width/12) + (space*(i+1)),(height/2)-20,text=str(savings[i]),font="Arial 10 bold")
            
        # this is for student loans( being a bit lazy here)
        else:
            principal = inputs[4]
            #an array here 
            years = inputs[5]
            rate = inputs[6]
            
            # can be true for now 
            fedLoan = True
            self.canvas.create_text(width/2, height/15, text="Student Loan Payments",font="Arial 20 bold")
            
            diff = 11*width/12 - (width/12)
            space = diff/(len(years)+1)
            
            # dummy loan vector 
            loans = [1000,900,800]
            
            #loans = amortizedStudentLoan(principal,rate,years,fedLoan)
            #range = max(loans)-min(loans)
            
            # plotting values for graph (bar graph style)  
            #height_range = (11*height/12 - height/8) -10
            # drawing the years on the bottom
            
            length = len(years)
            print(years)
            for i in range(0,length):
                print("hi")
            #for i in range(0,len(years)):
                #print("hi")
               # place = (10*width/12)+space*(i+1)
                #print(place)
                #self.canvas.create_text((width/12)+space*(i+1),height-height/20,text = str(years[i]),font="Arial 15 bold")
                # dollar per space
               # space = height_range/range
               # self.canvas.create_rectangle((width/12)+space*(i+1)-8,loans[i]*space,(width/12)+space*(i+1)+8,height/15,fill="red")
            
            
            
           
            
            #self.canvas.create_rectangle( ,width/20, 
            
                        
            
                


predUI = UI()
predUI.mainloop()
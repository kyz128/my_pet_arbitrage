# Taking average student loan interest rate at 5.8%
# have total amount of student loans 
# Congress sets interest rates yearly based on the 10-year Treasury note
# assumes federal loans of simple interest
# feature for compound interest on private loans 
# need annual interest on loan and divide it by 365 to get daily interest rate
# find the amortized payments of the total 

# principal is how much you borrowed
def simpleIntRate(principal,rate,years):
    dailyRate = rate/365
    daily_int = principal*dailyRate
    # assuming month is 30 day cycle
    month_pay = daily_int*30
    year_int = month_pay*12
    return year_int*years

def compoundIntRate(principal,rate,years): 



# yearVect is a vector of possible years to repay the loan default/baseline is 10
# we can also add to the length of th vector too 
def amortizedStudentLoan(principal,rate,yearVect,fedLoan):
    loan_projections = []
    amt = 0
    total = 0
    annuity = 0
    # first value in yearVect should be defaul 10 years
    for i in range(0,len(yearVect)): 
        # its a federal loan
        if (fedLoan):
            amt = simpleIntRate(principal,rate,yearVect[i])
            
        else:
            amt = compoundIntRate(principal,rate,yearVect[i])
        
        total = principal + amt
        # subtracted 1 because you don't pay when 
        annuity = total/((yearVect[i]*12)-1)
        loan_projections.append(annuity)
    
    
       
    
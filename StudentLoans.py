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
    return year_int

def compoundIntRate(principal,rate,years):
       
    
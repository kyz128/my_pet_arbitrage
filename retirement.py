    # monthly expense, array of moving averages for the n payment times including retirement year
    # years to ret until retirement, inflation (2.5%) 
    # PRE retire length array must be the same as moving average spot rate array!
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
        
ma_sp = [0.04,0.03,0.02,0.01]
post_retire_yr = 2
pre_retire_yr = 4
monthlyExp = 100
retirement(monthlyExp,ma_sp,post_retire_yr, pre_retire_yr)

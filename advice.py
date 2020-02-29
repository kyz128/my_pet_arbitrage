import random

advices= ["Always have 2K ($2000) in your bank account to spend in case of an emergency!", 
"Don’t spend more than 30% of your credit limit",
"When stocks are down, invest in the bond market!", 
"Know your FICO score and seek to improve it!",
"Start Saving for your 401k Plan ASAP!", 
"Invest in a diversified portfolio of stocks. \
A good starting place is in a S&P 500 index fund.", 
"Pay off your credit card balance on time! You will lose money if you make \
late payments by paying a whopping 25% interest rate fee.",
"Reinvest your savings in a diversified stock portfolio! Hold it for a \
minimum 10-15 years to realize significant gains!",
"Money compounds when reinvested. So invest your savings early!",  
"Stay within your budget. It will pay off later! Trust me!",
"Pay off your car loans ASAP. Interest compounds!"]

def generate_advice():
	return random.choice(advices)
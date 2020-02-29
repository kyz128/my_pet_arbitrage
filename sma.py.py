import numpy as np 

past_returns= np.loadtxt("sp500_arr.gz")
print(past_returns[-3:])
def moving_average(series, n, starting_pt):
	return np.sum(series[starting_pt:starting_pt+n])/n

def get_ma_arr(years):
	return np.array([moving_average(past_returns, 3, i) for i in range(years)])

print(get_ma_arr(20))

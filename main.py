import pandas as pd
from kai_jun import SMA
from joel import streakIdentifier
data = pd.read_csv('MSFT.csv')



cleaned = [float(x[1:]) for x in data['Close/Last']]    # list comprehension
data['Close/Last'] = cleaned
# print(data.info())

'''
period = input('select SMA days(must be integer):')
if period.isdigit() and 2<=int(period)<=len(data):
    period = int(period)
else:
    print('your input is invalid select 2 or more days without exceeding data series')
    exit()
'''
result = streakIdentifier(data, SMA, period=20, period1=50)
print(result)
'''
data['custom_SMA']=SMA(data['Close/Last'],period)    #positional argument

# test validation
data['test_SMA'] = data['Close/Last'].rolling(window=period).mean()
print(data)

'''
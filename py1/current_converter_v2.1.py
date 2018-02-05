"""
    Author:Arvin Shaffer
    Function:Exchange rate
    Version:1.0
    Date:02/01/2018
    New Function:According to the input to determine whether the RMB or the dollar, the corresponding conversion calculation
"""

#exchange rate
usd_vs_rmb = 6.77
#The input of currency with unit
currency_str_value = input('Please enter the amount of currency with unit：')
#get the unit
unit = currency_str_value[-3:]
currency_value = eval(currency_str_value[:-3])

if unit == 'CNY':
    # Calculate the value
    usd_value = currency_value / usd_vs_rmb
    # Output the result
    print('The amount of USD (USD) is：', usd_value)
elif unit == "USD":
    rmb_value = currency_value*usd_vs_rmb
    print('The amount of RMB (RMB) is：', rmb_value)
else:
    print("please input a right RMB or USD currency!")

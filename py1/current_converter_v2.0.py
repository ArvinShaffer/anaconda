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

print(unit)


# #String to number
# rmb_value = eval(rmb_str_value)
# #Calculate the value
# usd_value = rmb_value/usd_vs_rmb
# #Output the result
# print('The amount of USD (USD) is：', usd_value)













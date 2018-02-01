"""
    Author:Arvin Shaffer
    Function:Exchange rate
    Version:1.0
    Date:02/01/2018
"""

#exchange rate
usd_vs_rmb = 6.77
#input RMB
rmb_str_value = input('Please enter the amount in RMB (CNY)：')
#String to number
rmb_value = eval(rmb_str_value)
#Calculate the value
usd_value = rmb_value/usd_vs_rmb
#Output the result
print('The amount of USD (USD) is：', usd_value)













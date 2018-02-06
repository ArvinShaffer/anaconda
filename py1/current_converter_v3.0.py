"""
    Author:Arvin Shaffer
    Function:Exchange rate
    Version:1.0
    Date:02/01/2018
    2.0 New Function:According to the input to determine whether the RMB or the dollar, the corresponding conversion calculation
    3.0 New Function:The program runs until the user chooses to quit!
"""

#exchange rate
usd_vs_rmb = 6.77

currency_str_value = input('Please enter the amount of currency with unit(Exit the program, please enter(Q))：')

i = 0
while currency_str_value != 'Q':
    i = i + 1
    print('The number of loop:',i)
    #get the unit
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        #input the CNY
        rmb_str_value = currency_str_value[:-3]
        rmb_value = eval(rmb_str_value)
        # Calculate the value
        usd_value = rmb_value / usd_vs_rmb
        # Output the result
        print('The amount of USD (USD) is：', usd_value)
    elif unit == "USD":
        usd_str_value = currency_str_value[:-3]
        usd_value = eval(usd_str_value)
        rmb_value = usd_value*usd_value
        print('The amount of RMB (RMB) is：', rmb_value)
    else:
        print("please input a right RMB or USD currency!")
    print('********************************************************************************************************')
    currency_str_value = input('Please enter the amount of currency with unit(Exit the program, please enter(Q))：')

print('program is quit！')



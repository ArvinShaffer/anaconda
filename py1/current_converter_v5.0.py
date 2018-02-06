"""
    Author:Arvin Shaffer
    Function:Exchange rate
    Version:1.0
    Date:02/01/2018
    2.0 New Function:According to the input to determine whether the RMB or the dollar, the corresponding conversion calculation
    3.0 New Function:The program runs until the user chooses to quit!
    4.0 New Function:Exchange rate conversion function into the function!!
    5.0 New Function:(1)Make the program structured.(2)Simple function definition lambda
"""

def convert_currency(im, er):
    """
    Exchange rate
    :param im:the amount of money
    :param er: exchange rate
    :return:
    """
    out = im*er
    return out

def main():
    """
    main function
    :return:
    """
    #exchange rate
    usd_vs_rmb = 6.77

    currency_str_value = input('Please enter the amount of currency with unit(Exit the program, please enter(Q))：')

    #get the unit
    unit = currency_str_value[-3:]

    if unit == 'CNY':
        exchange_rate = 1 / usd_vs_rmb
    elif unit == "USD":
        exchange_rate = usd_vs_rmb
    else:
        exchange_rate = -1

    if exchange_rate != -1:
        in_money = eval(currency_str_value[:-3])
        #call function convert_currency()
        out_money = convert_currency(in_money, exchange_rate)
        print('Converted amount:', out_money)
    else:
        print('This currency is not supported!')

if __name__ == '__main__':
    main()

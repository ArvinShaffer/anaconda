"""
    Author:Arvin Shaffer
    Function:Air Quality Index Calculation
    Version:1.0
    Date:03/5/2018
"""

def cal_linear(iaqi_lo, iaqi_hi, bp_lo, bp_hi, cp):
    """
        Zoom in range
    """
    iaqi = (iaqi_hi - iaqi_lo) * (cp - bp_lo) / (bp_hi - bp_lo) + iaqi_lo
    return iaqi


def cal_pm_iaqi(pm_val):
    """
        Calculate the IAQI of pm2.5
    """
    if 0 <= pm_val < 36:
        iaqi = cal_linear(0, 50, 0, 35, pm_val)
    elif 36 <= pm_val < 76:
        iaqi = cal_linear(50, 100, 35, 75, pm_val)
    elif 76 <= pm_val < 116:
        iaqi = cal_linear(100, 150, 75, 115, pm_val)
    else:
        pass


def cal_co_iaqi(co_val):
    """
        Calculate the IAQI for CO
    """
    if 0 <= co_val < 3:
        iaqi = cal_linear(0, 50, 0, 3, co_val)
    elif 3 <= co_val < 5:
        iaqi = cal_linear(50, 100, 2, 4, co_val)
    else:
        pass


def cal_aqi(param_list):
    """
        AQI Calculate
    """
    pm_val = param_list[0]
    co_val = param_list[1]

    pm_iaqi = cal_pm_iaqi(pm_val)
    co_iaqi = cal_co_iaqi(co_val)

    iaqi_list = []
    iaqi_list.append(pm_iaqi)
    iaqi_list.append(co_iaqi)

    aqi = max(iaqi_list)
    return aqi

def main():
    print('Please enter the following information, separated by spaces!')
    input_str = input('(1)PM2.5 (2)CO:')
    str_list = input_str.split(' ')
    pm_val = float(str_list[0])
    co_val = float(str_list[1])

    param_list = []
    param_list.append(pm_val)
    param_list.append(co_val)

    # Call AQI calculation function
    aqi_val = cal_aqi(param_list)

    print('The air quality index is：{}'.format(aqi_val))

if __name__ == '__main__':
    main()

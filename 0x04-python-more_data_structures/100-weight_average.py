#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        mult = 0
        sum_all = 0
        for x in my_list:
            mult += x[0] * x[1]
        for x in my_list:
            sum_all += x[1]
        return mult/sum_all

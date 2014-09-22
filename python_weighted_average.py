# -*- coding: utf-8 -*-
'''
FileName        python_weighted_average.py
Description     Calculate weighted average with values in Python List 
Author          alirazabhayani
Date            22/09/2014
Time            18:42:30
Version         0.1
Usage           python python_weighted_average.py
Notes           LIst composed of Value and its weight 
Python_Version      2.7.6
'''

def weighted_average(value_weight_list):
    '''
    Takes a list of lists [value, weight] and
    returns weighted average as calculated by
    Sum of all values * weights / Sum of all weights
    '''

    numerator = sum([v * w for v,w in value_weight_list])
    denominator = sum([w for v,w in value_weight_list])
    if(denominator != 0):
        return(float(numerator) / float(denominator))
    else:
        return None


def main():
    raw_list = [[80, 5], [90, 6]]
    print weighted_average(raw_list)

 
if __name__ == '__main__':
    main()
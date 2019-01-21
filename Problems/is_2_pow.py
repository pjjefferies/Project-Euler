# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 21:16:08 2019

@author: PaulJ
"""

def is_2_pow(a_num):
    if a_num == 1:
        return True
    if a_num % 2 != 0:
        return False
    return is_2_pow(a_num/2)


sol_str = ''
num_str = ''
fun_str = ''

for i in solutions:
    num_str += (str(i) + ', ')
    fun_str += ((str(solutions[i]) + ', '))
    if is_2_pow(i):
        sol_str += (num_str[:-2] + '\n' + fun_str[:-2] +
                    '\n\n')
        num_str = ''
        fun_str = ''

with open('169_function.csv', 'w') as file:
    file.write(sol_str)

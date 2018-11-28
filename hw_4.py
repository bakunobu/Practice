#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 22:11:37 2018

@author: bakunobu
"""


pow_of_two = [2 ** i for i in range(10)]


def create_pow_list(n):
    """accepts int, returns a list of powers of 2 from 0 to int"""
    return map(lambda x: 2 ** x, range(n+1))


def find_one(my_list, x):
    """Checks if x(int) is a power of two, list of powers must be created
    and uploaded first"""
    if x in my_list:
        print(f'Foud at {my_list.index(x)}')

    else:
        print('Not in list')



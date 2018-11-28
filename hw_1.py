#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 06:49:14 2018

@author: bakunobu
"""


def ASCII_print(my_string):
    for i in my_string:
        print(ord(i))
    

def ASCII_converter(my_string):
    ord_str = list(ord(i) for i in my_string)
    return ord_str


def ASCII_converter_map(my_string):
    ascii_list = (list(map(ord, my_string)))
    return ascii_list
    

def sum_of_codes(my_list):
    return sum(my_list)  


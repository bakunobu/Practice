#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 21:59:19 2018

@author: bakunobu
"""


my_dict = {6: 'cappa', 1: '1', 2: '2', 3: '3', 4: 'four'}

my_list = list(my_dict.keys())

my_list.sort()

for k in my_list:
    print(k)

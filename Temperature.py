# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:43:44 2025

@author: Devayan
"""

fahrenheit = int(input("Please type in a temperature(F): "))
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit} degrees Fahrenheit equals {celsius} degrees Celsius")

if celsius < 0:
    print("Brr! It's cold in here!")
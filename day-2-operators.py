"""
Objective: In this challenge, you will work with arithmetic operators.
Check out the Tutorial tab for learning materials and an instructional
video.
"""

"""
Task: Given the meal price (base cost of a meal), tip percent (the
percentage of the meal price being added as tip), and tax percent (the
percentage of the meal price being added as tax) for a meal, find and print
the meal's total cost. Round the result to the nearest integer.
"""

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):
	"""
	"""

    add_tip = meal_cost * (tip_percent / 100)
    add_tax = meal_cost * (tax_percent / 100)
    final_cost = round(meal_cost + add_tip + add_tax)
    print(final_cost)


if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

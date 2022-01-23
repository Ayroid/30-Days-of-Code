
import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    # Write your code here
    tip=0.01*tip_percent*meal_cost
    tax=0.01*tax_percent*meal_cost
    cost=meal_cost+tip+tax
    cost=round(cost)
    print(cost)


meal_cost = float(input().strip())

tip_percent = int(input().strip())

tax_percent = int(input().strip())

solve(meal_cost, tip_percent, tax_percent)

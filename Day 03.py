from lib2to3.pgen2.token import GREATER
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

if(N%2):
    print("Weird")
else:
    if N in range(2,6) or N>20:
        print("Not Weird")
    elif N in range(6,21):
        print("Weird")



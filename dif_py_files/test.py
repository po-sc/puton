import math
from math import *


def main (z, x):
    a = 90 * (85 * z + 1) ** 4 - x
    b = 9 * x - 19 * math.sin(z) ** 6
    c = 44 * (x ** 2 - 0.2 - z ** 3) ** 2 + z ** 6
    d = 67 * (77 + 31 * z **2 + 31 * x ** 3) ** 2
    return a / b + sqrt(c / d)
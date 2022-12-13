#!/usr/bin/env python3
# -- coding: utf-8 --

import math

if __name__ == '__main__':
    x = float(input())
    y = float(input())
    if 1 >= math.sqrt(x ** 2 + y ** 2) >= 0.25:
        print("Входит в кольцо")
    else:
        print("Не входит в кольцо")


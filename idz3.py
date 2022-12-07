#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for i in range(105, 999, 7):
    h = i//100
    d = (i%100)//10
    u = i%10
    if h + d + u == 7:
        print(i)
#!/bin/python3

import math
import os
import random
import re
import sys

def solution(n: int):
    """
    """

    solution_list = [
        f"{n} x 1 = {n * 1}",
        f"{n} x 2 = {n * 2}",
        f"{n} x 3 = {n * 3}",
        f"{n} x 4 = {n * 4}",
        f"{n} x 5 = {n * 5}",
        f"{n} x 6 = {n * 6}",
        f"{n} x 7 = {n * 7}",
        f"{n} x 8 = {n * 8}",
        f"{n} x 9 = {n * 9}",
        f"{n} x 10 = {n * 10}"
    ]

    for i in range(10):

        print(solution_list[i])


if __name__ == '__main__':
    n = int(input().strip())
    solution(n)

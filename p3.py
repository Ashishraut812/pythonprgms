import math
import os
import random
import re
import sys



if __name__ == '__main__':
    cnt = 1
    n = int(input())
    b = list(bin(n))
    cnt = 0
    cnnt = []
    for i in b[2:]:
        if i == '1':
            cnt += 1
            cnnt.append(cnt)
        else:
            cnt = 0

    print(max(cnnt))




    
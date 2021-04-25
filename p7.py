import sys 


N = int(input()) # number of days

def solution(arr = map(float, input().split())):

    arr = list(arr)
    max = max(arr)
    p = arr.index(max) + 1

    min = min(arr)
    q = arr.index(min) + 1

    return max,p,min,q


print(solution,sep=",")


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    k = max(arr)
    c = arr.count(k)

    for i in range(c):
        arr.remove(max(arr))
    print(max(arr))
    

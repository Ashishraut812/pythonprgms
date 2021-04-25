if __name__ == '__main__':
    ml = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ml.append([name,score])
    
    for _ in ml[0]:
        print(ml[_])
    # for i in ml:
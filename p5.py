T = int(input())

for _ in range(T):
    N = int(input())

    if N == 1:
        print("NO")
        continue
    # find all divisors

    divisors = set([1])

    i = 2
    while(i*i<=N):
        if N%i == 0:
            divisors.add(i)
            divisors.add(N//i)
        i = i + 1


    # add them up

    divisors_sum = sum(divisors)


    # check sum with N

    if divisors_sum == N:
        print("YES")
    else:
        print("NO")

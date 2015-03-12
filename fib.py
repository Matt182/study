def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n == -1 or n == -2:
        return -1
    elif n < -2:
        res = {}
        res[0] = -1
        res[-1] = -1
        i = -2
        while i > n:
            res[i] = res[i+1] + res[i+2]
            i -= 1
        return res[n+1]
    else:
        res = {}
        res[0] = 1
        res[1] = 1
        i = 2
        while i < n+1:
            res[i] = res[i-1] + res[i-2]
            i += 1
        return res[n-1]

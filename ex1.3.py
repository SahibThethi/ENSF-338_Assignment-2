def func(n):
    if n == 0 or n == 1:
        return n
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]
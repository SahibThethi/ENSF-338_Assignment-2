import timeit
import matplotlib.pyplot as plt

def func(n):
    if n == 0 or n == 1:
        return n
    else:
        return func(n-1) + func(n-2)

times = []
for i in range(36):
    t = timeit.timeit(lambda: func(i), number=1)
    times.append(t)

def func2(n):
    if n == 0 or n == 1:
        return n
    memo = [0, 1]
    for i in range(2, n+1):
        memo.append(memo[i-1] + memo[i-2])
    return memo[n]


times2 = []
for i in range(36):
    times2.append(timeit.timeit(lambda: func2(i), number=1))

print(times)
print(times2)

plt.plot(times)
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Normal Function')
plt.show()

plt.plot(times2)
plt.xlabel('Input (n)')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity of Optimized Function')
plt.show()
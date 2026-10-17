# ---------- Fibonacci numbers ----------

# 1) WITHOUT DP: plain recursion.
# Simple, but slow, because it recalculates the same values many times.
def fib_recursive(n):
    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


# 2) WITH DP: store every result in a list (f[i] = f[i-1] + f[i-2]).
# Each value is calculated only once, so it is fast.

def fib_dp(n):
    f = [0] * max(n + 1, 2)      # f[i] holds the i-th Fibonacci number
    f[0] = 0
    f[1] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


if __name__ == "__main__":
    print("Recursive:", fib_recursive(10))
    print("DP       :", fib_dp(10))

# ---------- 0/1 Knapsack ----------
# Goal: pick items (each once) to get the max value without passing weight W.


# 1) WITHOUT DP: plain recursion.
# For each item: either skip it or take it, and keep the better result.
# Slow because the same sub-problems are solved again and again.
def knapsack_recursive(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if wt[n - 1] > W:  # item too heavy, skip it
        return knapsack_recursive(W, wt, val, n - 1)
    return max(
        val[n - 1] + knapsack_recursive(W - wt[n - 1], wt, val, n - 1),
        knapsack_recursive(W, wt, val, n - 1),
    )


# 2) WITH DP: dp[i][w] = best value using the first i items with capacity w.
def knapsack(W, wt, val, n):
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                dp[i][w] = max(
                    val[i - 1] + dp[i - 1][w - wt[i - 1]], dp[i - 1][w]
                )  # take it or leave it
            else:
                dp[i][w] = dp[i - 1][w]  # too heavy, leave it

    return dp[n][W]


if __name__ == "__main__":
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    print("Recursive:", knapsack_recursive(W, wt, val, len(val)))
    print("DP       :", knapsack(W, wt, val, len(val)))

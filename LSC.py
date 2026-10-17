# ---------- Longest Common Subsequence (LCS) ----------


# 1) WITHOUT DP: plain recursion.
# Compares the last characters of both strings and tries every option.
# Slow for long strings because it repeats the same sub-problems.
def lcs_recursive(s1, s2, m=None, n=None):
    if m is None:
        m, n = len(s1), len(s2)
    if m == 0 or n == 0:
        return 0
    if s1[m - 1] == s2[n - 1]:
        return 1 + lcs_recursive(s1, s2, m - 1, n - 1)
    return max(lcs_recursive(s1, s2, m - 1, n), lcs_recursive(s1, s2, m, n - 1))


# 2) WITH DP: build a table where dp[i][j] = LCS length of
# the first i chars of s1 and the first j chars of s2.
def lcs(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1  # chars match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # take the best

    return dp[m][n]


if __name__ == "__main__":
    print("Recursive:", lcs_recursive("ABCBDAB", "BDCABA"))
    print("DP       :", lcs("ABCBDAB", "BDCABA"))

'''
# Code Explain:
- Time complexity: O(m*n)
- Space complexity: O(m*n)

[1] Base State
- base on grid definition
- dp[i][j]: the unique paths from (0, 0) to (i, j)
[2] State Transfer Equation
- base on movement
- dp[i][j] = dp[i-1][j] + dp[i][j-1]
- because those two grids can both go to ddp[i][j]
[3] Initialize Conditions
- edge: i, j = 0, 0
    - only `one` path to dp[0][j] or dp[i][0]
    - set to 1
[4] State Compression (optional)
[5] Terminate Conditions

# Pros and Cons:
## Pros:

## Cons:

# Notation:

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n for row in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    # This will help you understand sol3 better
    # pre[j]: dp[i-1][j]
    # cur[j]: dp[i][j]
    def uniquePaths2(self, m: int, n: int) -> int:
        pre = [1] * n
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]
            pre = cur[:]  # update from i-1 to i
        return pre[-1]

    # state compression to reduce space complexity
    # Space complexity: O(n)
    def uniquePaths3(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]


m, n = 3, 7
print(Solution().uniquePaths(m, n))

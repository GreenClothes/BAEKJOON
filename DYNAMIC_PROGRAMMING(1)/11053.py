# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().strip().split()))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
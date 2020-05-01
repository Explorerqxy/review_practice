
def knapsack(W,N,weights,values):
    dp = [[0 for i in range(W+1)] for j in range(N+1)]
    for i in range(1,N+1):
        w = weights[i-1]
        v = values[i-1]
        for j in range(W,0,-1):
            if j >= w:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w]+v)
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[N][W])  # 11

if __name__ == '__main__':
    W1 = input()
    N1 = input()
    weight1 = list(map(int,input().split(' ')))
    value1 = list(map(int, input().split(' ')))
    print(W1)
    print(N1)
    print(weight1)
    print(value1)
    # knapsack(W1, N1, weight1, value1)
    # W = 10
    # N = 3
    # weights = [3, 4, 5]
    # values = [4, 5, 6]
    # knapsack(W, N, weights, values)
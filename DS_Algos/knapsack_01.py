def knapsack(W, wt, val):
    n = len(wt)
    k = [[0 for _ in range(W+1)] for __ in range(n+1)]

    for i in range(1, len(wt)+1):
        for w in range(1, W+1):
            if wt[i-1] <= w:
                k[i][w] = max(val[i-1] + k[i-1][w-wt[i-1]], k[i-1][w])
            else:
                k[i][w] = k[i-1][w]
            
    return k[n][W]

assert knapsack(5, [1,2,3], [60,100,120]) == 220

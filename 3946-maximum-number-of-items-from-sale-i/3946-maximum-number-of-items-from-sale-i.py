class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cnt     = Counter(f for f,p in items)
        mxf,mnp = max(cnt.keys())+1,   min(p for f,p in items)
        wgt,dp  = [sum(cnt[w] for w in range(f, mxf+1, f)) for f,p in items], [0]*(budget+1)
        for weight,price in zip(wgt, (p for f,p in items)):
            for p in range(budget, price-1, -1):
                dp[p] = max(dp[p], dp[p - price] + weight)
        return  max((dp[p] + (budget-p)//mnp for p in range(mnp,budget+1)), default=0)
        
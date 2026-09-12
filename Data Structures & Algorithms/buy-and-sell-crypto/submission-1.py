class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left,right=0,1
        best=0
        while right<len(prices):
            if prices[right]<prices[left]:
                left=right
            else:
                profit=prices[right]-prices[left]
                best=max(best,profit)
            right+=1
        return best

        
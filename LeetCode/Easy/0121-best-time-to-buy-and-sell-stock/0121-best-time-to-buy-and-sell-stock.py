class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                if (sell-buy) > profit:
                    profit = sell - buy 
            else:
                buy = sell
            print(sell, buy)
        return profit
                    
        
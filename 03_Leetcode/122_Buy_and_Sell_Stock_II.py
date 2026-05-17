prices = [7,1,5,3,6,4]

buy = float("inf")
sell = 0

for price in prices:
    buy = min(buy, price)
    sell = max(sell, price - buy)
        
print(sell)
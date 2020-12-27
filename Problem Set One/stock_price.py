def stock(prices):
    dict1 = {}
    i = 0
    buy = sell = 0
    while prices:
        try:
            buy = min(prices)
        except:
            buy = 0
        try:
            sell = max(prices[prices.index(buy) + 1:])
        except:
            sell = 0
        try:
            prices.remove(buy)
        except:
            continue
        try:
            prices.remove(sell)
        except:
            continue

        dict1[sell - buy] = (buy, sell)
    sorted_dict = sorted(dict1.items(), key = lambda x: (x[0]))
    if sorted_dict:
        return sorted_dict[-1][0]
    else:
        return 0

print(stock([7,6,4,3,1,10]))
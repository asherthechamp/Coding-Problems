# Calculates the number of fruits that can be collected

def fruit_baskets(fruits):
    totals_array = []
    for i in range(0, len(fruits) - 1):
        j = i
        fruit = fruits[i]
        one = fruits[i]
        two = fruits[i+1]
        total = 0
        while fruit == one or fruit == two:
            total += 1
            j += 1
            try:
                fruit = fruits[j]
            except:
                break
        totals_array.append(total)
    return max(totals_array)

print(fruit_baskets([3,3,3,1,2,1,1,2,3,3,4]))
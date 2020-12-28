# Calculates the minimum cost of climbing stairs

def minCostClimbingStairs(cost: list[int]) -> int:
    index = 0
    totalCost = 0
    while (index + 1 < len(cost)):
        num1 = cost[index] + cost[index + 1]
        addable1 = cost[index +1]
        try:
            num2 = cost[index] + cost[index + 2]
            addable2 = cost[index + 2]
        except:
            num2 = cost[index] + 0
            addable2 = 0
        if index == 0:
            num1 = cost[index] + cost[index + 1]
            addable1 = cost[index] + cost[index + 1]
            try:
                num2 = cost[index] + cost[index + 2]
                addable2 = cost[index] + cost[index + 2]
            except:
                num2 = cost[index] + 0
                addable2 = 0
            try:
                num3 = cost[index + 1] + cost[index + 2]
                addable3 = cost[index + 2]
            except:
                num3 = cost[index + 1] + 0
                addable3 = 0
            try:
                num4 = cost[index + 1] + cost[index + 3]
                addable4 = cost[index + 3]
            except:
                num4 = cost[index + 1] + 0
                addable4 = 0
        if index == 0:
            minimum = min(num1, num2, num3, num4)
        else:
            minimum = min(num1, num2)

        if minimum == num1:
            totalCost += addable1
        if minimum == num2:
            totalCost += addable2
        if minimum == num3:
            totalCost += addable3
        if minimum == num4:
            totalCost += addable4


        elif minimum == num1 or minimum == num3 :
            if num1 == num2 or num3 == num4:
                index += 2
            else:
                index += 1
        elif minimum == num2 or minimum == num4:
            index += 2

    return totalCost

print(minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
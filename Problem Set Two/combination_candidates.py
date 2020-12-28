# Creates combination of numbers from an arary that sum up to a target

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    factors = [1] * len(candidates)
    result_array = []
    for i in range(0, len(candidates)):
        factors[i] = target // candidates[i]
    for i in range(0, len(candidates)):
        for k in range(1, factors[i]+1):
            sum = 0
            sum += k * candidates[i]
            array = [candidates[i]] * k
            for j in range(0, len(candidates)):
                while (sum < target):
                    sum += candidates[j]
                    array.append(candidates[j])
                if sum == target and array not in result_array:
                    result_array.append(array)
                else:
                    break
    return result_array

print(combinationSum([2,3,6,7, 9], 9))
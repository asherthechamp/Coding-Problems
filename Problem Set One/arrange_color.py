# Arranges an array of colors in the order red - white - blue

def arrange_color(nums):
    result = []
    red = []
    white = []
    blue = []
    for i in range(0, len(nums)):
        if nums[i] == 0:
            red.append(0)
        if nums[i] == 1:
            white.append(1)
        if nums[i] == 2:
            blue.append(2)
    result = red + white + blue
    return result

print(arrange_color([2,0,2,1,1,0]))


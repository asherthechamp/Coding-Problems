# Implements bubble sort

def bubble_sort(array):
    sorted = False
    while not sorted:
        sorted = True
        j = 0
        for i in range(0, len(array) - 1 - j):
            if array[i] > array[i+1]:
                sorted = False
                array[i], array[i+1] = array[i+1], array[i]
            j += 1

myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(myList)
print(myList)
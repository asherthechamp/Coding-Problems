# Constructs a queue data structure

class QueueFn(list):
    def __init__(self, arr):
        self.arr = arr
    def enqueue(self, x):
        self.arr.append(x)
        return self.arr
    def dequeue(self):
        del self.arr[-1]
        return self.arr
    def peek(self):
        return self.arr[-1]


print(QueueFn([4, 3, 2, 1, 0]).enqueue(5))
print(QueueFn([4, 3, 2, 1, 0]).dequeue())
print(QueueFn([4, 3, 2, 1, 0]).peek())
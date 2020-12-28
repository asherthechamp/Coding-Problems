# Returns The Maximum value in a stack

class MaxStack:
  def __init__(self):
    self.Stack = []
    # Fill this in.

  def push(self, val):
    self.Stack.append(val)

  def pop(self):
    if (len(self.Stack) != 0):
        self.Stack.pop(-1)

  def max(self):
    maximum = self.Stack[0]
    for i in range(1, len(self.Stack)):
        if (self.Stack[i] > maximum):
            maximum = self.Stack[i]
    return maximum


    # Fill this in.

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print (str(s.max()))
# 3
s.pop()
s.pop()
print (str(s.max()))
# 2
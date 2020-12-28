# Find the floor and ceiling of a tree

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floor=None, ceil=None):
    if (root_node): 
        if (k > root_node.value):
            floor = root_node.value
            return findCeilingFloor(root_node.right, k, floor, ceil)
        elif (k < root_node.value):
            ceil = root_node.value
            return findCeilingFloor(root_node.left, k, floor, ceil)
        return (floor, ceil)
    return (floor, ceil)


# Fill this in.

root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print
print(str(findCeilingFloor(root, 5)))
# (4, 6)
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Takes in a linked list head and returns another linked list
# removing consecutive nodes that sum up to zero

def removeConsecutiveSumTo0(node):
    init_node = node
    while(node):
        sum = node.value
        start_node = node
        end_node = None
        while(node.next):
            sum += node.next.value
            if sum == 0:
                end_node = node.next
                break
            else:
                node = node.next
        if end_node:
            node = init_node
            node.next = end_node.next
        else:
            node = start_node.next
    return init_node

node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node = removeConsecutiveSumTo0(node)
while node:
    print(node.value)
    node = node.next

# 10

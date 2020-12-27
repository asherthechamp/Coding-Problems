# Removes kth node from a linked list

class Node:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
  def __str__(self):
    current_node = self
    result = []
    while current_node:
      result.append(current_node.val)
      current_node = current_node.next
    return str(result)

def remove_kth_from_linked_list(head, k):
    count = 1
    result_head = Node(head.val)
    appendable_node = result_head
    while head:
        if count + 1 == k:
            head.next = head.next.next
            appendable_node.next = head.next
            break
        count += 1
        head = head.next
        appendable_node = append_next(head, appendable_node)
    return result_head

def append_next(node, appendable):
    appendable.next = Node(node.val)
    return appendable.next

def another_one(head, k):
    movable = head
    i = k - 1
    while(i != 1):
        movable = movable.next
        i -= 1
    while(movable.next):
        movable.val = movable.next.val
        prev = movable
        movable = movable.next
    prev.next = None
    return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
# head = remove_kth_from_linked_list(head, 3)
# print(head)
# [1, 2, 4, 5]
head = another_one(head, 3)
print(head)
# [1, 2, 4, 5]
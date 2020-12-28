# calculates sum of two linked lists

class ListNode (object):
    def __init__(self, x):
        self.val = x
        self.next = None

def add_two_numbers(node, l1, l2, c =0):
    if (not(node)):
        node = ListNode((l1.val + l2.val + c) % 10)
    else:
        node.next = ListNode((l1.val + l2.val + c) % 10)
    if (l1.val + l2.val >= 10):
        c = 1
    else:
        c = 0
    if (l1.next and l2.next):
        add_two_numbers(node.next, l1.next, l2.next, c)
    return node

l1= ListNode (2)
l1.next = ListNode (4)
l1.next.next = ListNode (3)

l2 = ListNode (5)
l2.next = ListNode (6)
l2.next.next = ListNode (4)

l3 = ListNode(object)

result = add_two_numbers(l3, l1, l2)
while result:
    print (result.val),
    result = result.next
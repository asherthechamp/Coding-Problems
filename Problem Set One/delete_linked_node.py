# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Deletes a linked list node
class Solution:
    def deleteNode(self, node):
        prev = ListNode()

        if (node == None):
            return
        else:
            while (node.next != None):
                node.val = node.next.val
                prev = node
                node = node.next

            prev.next = None    
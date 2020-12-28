# Reverse a linked list

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printList(self):
        node = self
        output = ''
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print (output)
    def copy(self):
        newNode = ListNode(self.val)
        newNode.next = self.next
        return newNode

    def reverseIteratively(self, head):
        prev = None
        current = head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        head = prev
        return head

    def reverseRecursively(self, head, reverseNode):
        if(head.next):
            if(reverseNode.val == None):
                reverseNode = ListNode(head.next.val)
                reverseNode.next = ListNode(head.val)
                self.reverseRecursively(head.next, reverseNode)
            else:
                reverseNode.next = reverseNode.copy()
                reverseNode.val = head.next.val
                self.reverseRecursively(head.next, reverseNode)
        return reverseNode


testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()

resNode = ListNode(None)

resultNode = testHead.reverseRecursively(testHead, resNode)
resultNode2 = testHead.reverseIteratively(testHead)
resultNode.printList()
resultNode2.printList()

print("List after reversal: ")
testTail.printList()
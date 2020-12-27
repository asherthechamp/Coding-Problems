# Checks if there are two numbers in the array that sum up to k in the given node

# Creates a tree node class
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Creates if the sum of two numbers in the node equals k
def sum_k(node, k):
    parent = node
    while(node):
        # Takes in one node and checks if it can finds the complemnentary addened
        comp = k - node.val
        if bs(parent, comp) or bs(parent, comp):
            return True
        elif node.right:
            node = node.right
        else:
            node = node.left
    return False

# Searches for a node in the binary search tree

def bs(node, k):
    while(node):
        if node.val == k:
            return True
        elif k > node.val:
            node = node.right
        else:
            node = node.left
    return False

root = TreeNode(5)
root.left= TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(6)
root.right.right= TreeNode(7)

print(sum_k(root, 9))
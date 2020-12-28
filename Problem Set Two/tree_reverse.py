# Returns the inverse of a tree

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
  def preorder(self):
    print(self.value)
    if self.left: self.left.preorder()
    if self.right: self.right.preorder()

def invert(node):
    if node is None:
        return None

    node.left, node.right = node.right, node.left

    invert(node.left)
    invert(node.right)

    return node
  # Fill this in.

root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print("\n")
root = invert(root)
root.preorder()
# a c f b e d
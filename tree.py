class BTNode:
  def __init__(self, elem):
    self.elem = elem
    self.right = None
    self.left = None

def inorder(root):
  if root == None:
    return

  inorder(root.left)
  print(root.elem, end = ' ')
  inorder(root.right)

def tree_construction(arr, i = 1):
  if i>=len(arr) or arr[i] == None:
    return None
  p = BTNode(arr[i])
  p.left = tree_construction(arr, 2*i)
  p.right = tree_construction(arr, 2*i+1)
  return p


root2 = tree_construction([None, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', None, None, None, 'I', 'J', None, 'k'])
inorder(root2)

def LCA(root, x, y):
  if root == None:
    return None
  if root.elem == x or root.elem == y:
    return root

  l=LCA(root.left,x,y)
  r=LCA(root.right,x,y)

  if l and r:
    return root

  return l if l else r


root = BTNode(15)
root.left = BTNode(10)
root.right = BTNode(25)
root.left.left = BTNode(8)
root.left.right = BTNode(12)
root.left.left.left = BTNode(6)
root.left.left.right = BTNode(9)
root.right.left = BTNode(20)
root.right.right = BTNode(30)
root.right.left.left = BTNode(18)
root.right.left.right = BTNode(22)

def print_LCA(root,x,y):
  lca=LCA(root,x,y)
  if lca:
        print(f"LCA({x},{y}) = {lca.elem}")
  else:
        print(f"LCA of {x} and {y} is not found.")

print_LCA(root,6,12)
print_LCA(root,20,6)
print_LCA(root,18,22)
print_LCA(root,20,25)
print_LCA(root,10,12)
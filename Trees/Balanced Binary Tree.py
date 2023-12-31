class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class BinarySearchTree:
   def __init__(self):
      self.root = None

   def insert(self, data):
      if self.root is None:
         self.root = Node(data)
      else:
         self.insert_recursively(data, self.root)

   def insert_recursively(self, data, current_node):
      if current_node.data > data:
         if current_node.left is None:
            current_node.left = Node(data)
         else:
            self.insert_recursively(data, current_node.left)
      else:
         if current_node.right is None:
            current_node.right = Node(data)
         else:
            self.insert_recursively(data, current_node.right)

   def inorder(self, CNode):
      if CNode.left:
         self.inorder(CNode.left)
      if CNode.data:
         r.append(CNode.data)
      if CNode.right:
         self.inorder(CNode.right)

   def remove(self, data):
      self.root = self.remove_recursively(self.root, data)

   def remove_recursively(self, current_node, data):
      if current_node is None:
         return current_node

      if data < current_node.data:
         current_node.left = self.remove_recursively(current_node.left, data)
      elif data > current_node.data:
         current_node.right = self.remove_recursively(current_node.right, data)
      else:
         if current_node.left is None:
            return current_node.right
         elif current_node.right is None:
            return current_node.left

         current_node.data = self.find_min(current_node.right)
         current_node.right = self.remove_recursively(current_node.right, current_node.data)

      return current_node

   def find_min(self, current_node):
      while current_node.left is not None:
         current_node = current_node.left
      return current_node.data

   def maxdepthdfs(self,current):
      if current is None:
         return 0

      return  1 + max(self.maxdepthdfs(current.left), self.maxdepthdfs(current.right))

   def height(self, current):

      if not current:
         return True
      if(abs(self.maxdepthdfs(current.left) - self.maxdepthdfs(current.right))>2):
         return False
      else:
         return True

      if(current.left):
         self.height(current.left)
      if(current.right):
         self.height(current.right)

   def heightn(self,current):

      if current is None:
         return [True,0]

      ansb = (abs(self.maxdepthdfs(current.left)-self.maxdepthdfs(current.right))<2) and self.heightn(current.left) and self.heightn(current.right)
      print(ansb)
      return [ansb,1 + max(self.maxdepthdfs(current.left), self.maxdepthdfs(current.right))]

# def lsum(c):
#
#    if not c:
#       return maxi
#    maxi = max(maxi, maxi + c.data)
#    lsum(c.left)
#    lsum(c.right)
#    print(maxi)
#    return max(maxi,c.data + lsum(c.left) + lsum(c.right))
#






r = []

tree = BinarySearchTree()
tree.insert(5)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(3)

h = 0
tree.inorder(tree.root)
print("In-order traversal:", r)

# Remove a node
tree.remove(4)
r = []
h = 0
tree.inorder(tree.root)
print("In-order traversal after removing 4:", r)

# n * n
print(tree.height(tree.root))

#n time compexity
print(tree.heightn(tree.root))
maxi = 0
# print(lsum(tree.root,tree.root.data))

ans =   tree.root.data


def lsum(c):
   global ans
   if not c :
      return 0

   leftsum = lsum(c.left)
   rightsum = lsum(c.right)

   ans = max(ans, c.data + leftsum + rightsum, c.data + leftsum, c.data + rightsum)
   return c.data + max (leftsum,rightsum)


print(lsum(tree.root))

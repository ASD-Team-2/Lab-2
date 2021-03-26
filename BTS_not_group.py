
class Node:

    def __init__(self, key):

        self.left = None
        self.right = None
        self.key = key

# Insert method to create nodes
    def insert(self, key):

        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = Node(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key
# find_val method to compare the value with nodes
    def find_val(self, lkpval):
        if lkpval < self.key:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.find_val(lkpval)
        elif lkpval > self.key:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.find_val(lkpval)
        else:
            print(str(self.key) + ' is found')
# delete element            
    def remove(self, d):
    
   # Returns True if node successfully removed, False if not removed
    
    # Case 1: Empty Tree?
        if self.root == None:
            return False

    # Case 2: Deleting root node
        if self.root.data == d:
      # Case 2.1: Root node has no children
            if self.root.left is None and self.root.right is None:
                self.root = None
                return True
      # Case 2.2: Root node has left child
            elif self.root.left and self.root.right is None:
                self.root = self.root.left
                return True
      # Case 2.3: Root node has right child
            elif self.root.left is None and self.root.right:
                self.root = self.root.right
                return True
      # Case 2.4: Root node has two children
            else:
                moveNode = self.root.right
                moveNodeParent = None
                while moveNode.left:
                    moveNodeParent = moveNode
                    moveNode = moveNode.left
                self.root.data = moveNode.data
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
                return True		
    # Find node to remove
        parent = None
        node = self.root
        while node and node.data != d:
          parent = node
          if d < node.data:
            node = node.left
          elif d > node.data:
            node = node.right
    # Case 3: Node not found
        if node == None or node.data != d:
            return False
    # Case 4: Node has no children
        elif node.left is None and node.right is None:
            if d < parent.data:
                parent.left = None
            else:
                parent.right = None
            return True
    # Case 5: Node has left child only
        elif node.left and node.right is None:
            if d < parent.data:
                parent.left = node.left
            else:
                parent.right = node.left
            return True
    # Case 6: Node has right child only
        elif node.left is None and node.right:
            if d < parent.data:
                parent.left = node.right
            else:
                parent.right = node.right
            return True
    # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.right
            while moveNode.left:
                moveNodeParent = moveNode
                moveNode = moveNode.left
            node.data = moveNode.data
            if moveNode.right:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = moveNode.right
                else:
                    moveNodeParent.right = moveNode.right
            else:
                if moveNode.data < moveNodeParent.data:
                    moveNodeParent.left = None
                else:
                    moveNodeParent.right = None
            return True
#Sum of b-tree
    def sum_all(self): 
        if (root == None):
            return 0
        return (root.key + sum_all(self.left) + 
                       sum_all(self.right)) 
# Print the tree
    def print_tree(self):
        if self.left:
            self.left.PrintTree()
        print( self.key),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find_val(7))
print(root.find_val(14))
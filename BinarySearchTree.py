# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
            
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)
                
    def search(self, data):
        if self.root is None:
            return False
        else:
            return self._search(data, self.root)
            
    def _search(self, data, node):
        if data == node.data:
            return True
        elif data < node.data and node.left is not None:
            return self._search(data, node.left)
        elif data > node.data and node.right is not None:
            return self._search(data, node.right)
        else:
            return False
            

    # REMOVE
    def remove(self,data):
        if self.root is None:
            return self.root
        else:
            return self._remove(self.root,data)
    
    def _remove(self,root, key):
  
        # Base Case
        if root is None:
            return None
  
    # If the key to be deleted 
    # is smaller than the root's
    # key then it lies in  left subtree
        if key < root.data:
            root.left =  self._remove(root.left, key)
  
    # If the kye to be delete 
    # is greater than the root's key
    # then it lies in right subtree
        elif(key > root.data):
            root.right = self._remove(root.right, key)
  
    # If key is same as root's key, then this is the node
    # to be deleted
        else:
        # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
  
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        # Node with two children: 
        # Get the inorder successor
        # (smallest in the right subtree)
            else: 
                cur = root.right
                # loop down to find the leftmost leaf
                while(cur.left is not None):
                    cur = cur.left
  
                # Copy the in order successor's 
                # content to this node
                root.data = cur.data
  
        # Delete the in order successor
                root.right=self._remove(root.right,cur.data)
  
        return root
    
    
    # PRINT
    def inorder(self):
        self._inorder(self.root)
        print()
    
    def _inorder(self,root):
        if root is not None:
            self._inorder(root.left)
            print (root.data,end=" ")
            self._inorder(root.right)
            
    def preorder(self):
        self._preorder(self.root)
        print()
    
    def _preorder(self,root):
        if root is not None:
            print (root.data,end=" ")
            self._preorder(root.left)
            self._preorder(root.right)
            
    def postorder(self):
        self._inorder(self.root)
        print()
    
    def _postorder(self,root):
        if root is not None:
            self._posorder(root.left)
            self._posorder(root.right)
            print (root.data,end=" ")
            
    def print_tree(self):
        self._print_tree(self.root, " ")
        print()

    def _print_tree(self,root, indent):
        if root is not None:
            self._print_tree(root.right, indent + "   ")
            print(indent + str(root.data))
            self._print_tree(root.left, indent + "   ")
      
    # HEIGHT OF A TREE      
    def height(self):
        return self._height(self.root)


    def _height(self,root):
        if root is None:
            return 0
        return max(self._height(root.left),self._height(root.right))+1


      
newTree = BST()
newTree.insert(15)
newTree.insert(6)
newTree.insert(18)
newTree.insert(3)
newTree.insert(7)
newTree.insert(17)
newTree.insert(19)
newTree.insert(2)
newTree.insert(4)
newTree.insert(13)
newTree.insert(9)

# newTree.inorder()
# newTree.preorder()
# newTree.postorder()
newTree.print_tree()
print("------------------")
newTree.remove(15)
newTree.print_tree()       

print("Height: "+ str(newTree.height())) 
'''
For each node, all values in its left subtree are less than the value in the node, and all values in its right subtree are greater than the value in the node.
This property also implies that values in a BST must be unique.
Searching, adding, and removing can be done in O(log(N))
An inorder DFS traversal prioritizing left before right on a BST will handle the nodes in sorted order.
'''

class Node: 
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree: 
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if not self.root: 
            self.root = new_node
            return True
        
        temp = self.root
        while True: 
            # if value is already in the tree .. return 
            if new_node.value == temp.value: 
                return False
            # if value is less than, go left 
            if new_node.value < temp.value: 
                if temp.left is None: 
                    temp.left = new_node 
                    return True 
                temp = temp.left 
            # if value is greater than, go right 
            else: 
                if temp.right is None: 
                    temp.right = new_node
                    return True 
                temp = temp.right 
            
    def insert_resursive(self, root, val):
        if not root: 
            return Node(val)

        if val < root.val: 
            root.left = self.insert_resursive(root.left, val)
        elif val > root.val: 
            root.right = self.insert_resursive(root.right, val)
        return root 

    def find_min(self, root):
        # min val should always be bottom left 
        curr = root
        while curr and curr.left: 
            curr = curr.left
        return curr

    def remove(self, root, val):
        if not root: 
            return None 

        if val > root.val: 
            root.right = self.remove(root.right, val)
        elif val < root.val: 
            root.left = self.remove(root.left, val)
        else: 
            if not root.left: 
                return root.right
            elif not root.right: 
                return root.left 
            else: 
                min_node = self.find_min(root.right)
                root.val = min_node.val 
                root.right = self.remove(root.right, min_node.val) 
        return root         




def main():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    '''
         2
        / \
       1   3
            \
             4  
    '''

    '''
         4
        / \
       3   6
      /    / \
     2    5    7

    removing can be tricky when we want to remove 4 or 6   
    '''

if __name__ == "__main__":
    main()
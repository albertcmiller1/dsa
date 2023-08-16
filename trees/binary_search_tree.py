'''
another way to insert: 
TreeNode* insert(TreeNode* root, int val) {
    if (!root) {
        return new TreeNode(val);
    }

    if (val > root->val_) { 
        root->right = insert(root->right, val);
    } else if (val < root->val_) {
        root->left = insert(root->left, val);
    }
    return root;
}
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
        if self.root == None: 
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
# print(tree.root.value)
# print(tree.root.left.value)
# print(tree.root.right.value)
# print(tree.root.right.right.value)


def value_in_tree(root, target):
    if not root: return False

    if target > root.value: 
        return value_in_tree(root.right, target)
    elif target < root.value: 
        return value_in_tree(root.left, target)
    else: 
        return True

assert value_in_tree(tree.root, 3) == True
assert value_in_tree(tree.root, 8) == False


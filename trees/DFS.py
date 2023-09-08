def DFS_inorder(root):
    if not root: 
        return 
    DFS_inorder(root.left)
    print(root.value)
    DFS_inorder(root.right)

def DFS_preorder(root):
    # first value of preorder traversal will always be the root -> IMPORTANT 
    # the second valueue will always be the root of the left subtree 
    if not root: 
        return 
    print(root.value)
    DFS_preorder(root.left)
    DFS_preorder(root.right)

def DFS_postorder(root):
    if not root: 
        return 
    DFS_postorder(root.left)
    DFS_postorder(root.right)
    print(root.value)


from BST import BinarySearchTree
def make_tree():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    return tree

'''
        2
       / \
      1   3
           \
            4  
'''

def main():
    tree = make_tree()
    DFS_inorder(tree.root) # 1 2 3 4

if __name__ == "__main__":
    main()

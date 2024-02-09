def DFS_preorder(root):
    '''
    first value of preorder traversal will always be the root -> IMPORTANT 
    the second value will always be the root of the left subtree 
    '''
    if not root: 
        return 
    print(root.value)
    DFS_preorder(root.left)
    DFS_preorder(root.right)

def DFS_inorder(root):
    '''
    for any given node, its value is not printed until all values in the left subtree are printed, 
    and values in its right subtree are not prited until after that 
    '''
    if not root: 
        return 
    DFS_inorder(root.left)
    print(root.value)
    DFS_inorder(root.right)


def DFS_postorder(root):
    '''
    Notice that for any given node, no values in its right subtree are printed until all values in its left subtree are printed,
    and its own value is not printed until after that.
    '''
    if not root: 
        return 
    DFS_postorder(root.left)
    DFS_postorder(root.right)
    print(root.value)

def dfs_itererave(root):
    # https://www.youtube.com/watch?v=5LUXSvjmGCw&ab_channel=NeetCode
    # https://www.scaler.com/topics/iterative-inorder-traversal/
    stack = []
    curr = root

    while curr or stack: 
        while curr: 
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
    curr = curr.right



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

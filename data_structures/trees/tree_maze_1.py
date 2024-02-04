from BST import BinarySearchTree
def make_tree():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    return tree

'''
Determin if a path exists from the root of the tree to a leaf node. 
The path may not contain any zeroes. 
'''
def path_exists(root): 
    if not root or root.value == 0:
        return False
    
    if not root.left and not root.right: 
        return True

    if path_exists(root.left):
        return True

    if path_exists(root.right):
        return True

    return False


'''
Determine if a path exists from the root of the tree to a leaf node. 
It may not contain any zeros. 
Also show the path in an array if one exists. 
'''
def path_exists_2(root, path): 
    if not root or root.value == 0:
        return False
    
    path.append(root.value)

    if not root.left and not root.right: 
        return True

    if path_exists_2(root.left, path):
        return True

    if path_exists_2(root.right, path):
        return True

    path.pop()

    return False





if __name__ == "__main__":
    tree = make_tree()
    # assert path_exists(tree.root) == True
    
    path = []
    path_exists_2(tree.root, path)
    print(path)



'''
        2
       / \
      1   3
           \
            4  
'''

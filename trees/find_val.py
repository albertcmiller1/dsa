from BST import BinarySearchTree
def make_tree():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    return tree


def value_in_tree(root, target):
    if not root: return False

    if target > root.value: 
        return value_in_tree(root.right, target)
    elif target < root.value: 
        return value_in_tree(root.left, target)
    else: 
        return True



def main():
    tree = make_tree()
    assert value_in_tree(tree.root, 3) == True
    assert value_in_tree(tree.root, 8) == False

if __name__ == "__main__":
    main()
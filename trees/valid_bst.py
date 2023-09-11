'''
given the root of a binary tree, determine if it is a valid binary search tree
https://leetcode.com/problems/validate-binary-search-tree/


   5                     -inf < 5 < inf
3    7          -inf < 3 < 5,       5 < 7 < inf
    4  8                     5 !< 4 < 7,   7 < 8 < inf
false

   5         
3    7       
  4    8           
true
'''


from BST import BinarySearchTree
def make_tree():
    tree = BinarySearchTree()

    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(4)

    return tree


def bst_is_valid(root):

    def valid(node, lb, rb):
        if not node: 
            return True

        if not (lb < node.value and node.value < rb):
            return False

        return (
            valid(node.left,  lb,         node.value) and 
            valid(node.right, node.value, rb)
        ) 
        # every value in left  subtree has to be less   than parent, so parent is set to right boundry 
        # every value in right subtree has to be bigger than parent, so parent is set to left  boundry 

    return valid(root, float("-inf"), float("inf"))
        


def main():
    tree = make_tree()
    ans = bst_is_valid(tree.root)
    print(ans)

if __name__ == "__main__":
    main()
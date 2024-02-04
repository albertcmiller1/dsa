from collections import deque 
# https://dev.to/v_it_aly/python-deque-vs-listwh-25i9#:~:text=Second%2C%20because%20deques%20are%20implemented,node%20on%20a%20given%20position.

def BFS(root):
    queue = deque()

    if root: 
        queue.append(root)

    level = 0
    while queue:
        print("level: ", level)

        for _ in range(len(queue)):
            curr = queue.popleft()
            print(f"curr.value: {curr.value}")
            if curr.left: 
                queue.append(curr.left)
            if curr.right: 
                queue.append(curr.right)

            # if curr:
            #     queue.append(curr.left)
            #     queue.append(curr.right)

        level += 1


from BST import BinarySearchTree


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

    BFS(tree.root) # 2 1 3 4



if __name__ == "__main__":
    main()


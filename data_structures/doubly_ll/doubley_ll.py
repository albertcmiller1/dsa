class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None 

class doublyLinkedList: 
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def show(self):
        if not self.head: 
            print("no list to show.")

        curr = self.head
        while curr: 
            print(curr.value)
            curr = curr.next
        print(f"length: {self.length}")

    def append(self, value):
        new_node = Node(value)
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            new_node.prev = self.tail 
            self.tail = new_node
        self.length += 1
        return True

    def pop_tail(self):
        if self.length == 0:
            return None
        temp = self.tail 
        if self.length == 1: 
            self.head = None 
            self.tail = None 
        else: 
            self.tail = self.tail.prev 
            self.tail.next = None
            temp.prev = None 
        self.length -= 1
        return temp 



d_ll = doublyLinkedList(1)
d_ll.append(2)
d_ll.show()
d_ll.pop_tail()
d_ll.show()

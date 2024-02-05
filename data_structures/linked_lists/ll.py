class Node: 
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList: 
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
        if self.head: 
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        else: 
            self.head = new_node
            self.tail = new_node
        return True

    def pop_tail(self):
        if self.head.next: 
            curr = self.head 
            while curr.next.next: 
                curr = curr.next 
            old_tail = curr.next 
            curr.next = None
            self.length -= 1
            return old_tail 
        else:
            self.head = None
            self.length -= 1
       
    def prepend(self, value):
        new_node = Node(value)
        if self.head: 
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else: 
            self.head = new_node
            self.tail = new_node

    def pop_head(self):
        if self.head.next: 
            self.head = self.head.next
        else: 
            self.head = None
        self.length -= 1

    def get(self, index):
        if index < 0 or index >= self.length: 
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.next 
        return curr

    def set_value(self, index, value):
        temp = self.get(index)
        if temp: 
            temp.value = value 
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index >= self.length: 
            return False
        elif index == 0: 
            return self.prepend(value)
        elif index == self.length: 
            return self.append(value)
        else: 
            new_node = Node(value)
            temp = self.get(index-1)
            new_node.next = temp.next 
            temp.next = new_node
            self.length += 1
            return True

    def remove(self, index):
        if index < 0 or index >= self.length: 
            return False
        elif index == 0: 
            return self.pop_head()
        elif index == self.length: 
            return self.pop_tail()
        else: 
            prev = self.get(index-1)
            temp = prev.next 
            prev.next = prev.next.next
            self.length -= 1
            return temp

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = curr
        while curr: 
            next = curr.next 
            curr.next = prev
            prev = curr 
            curr = next

        self.head = prev




        

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.show()
print("\n")

ll.reverse()
ll.show()

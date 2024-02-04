'''
the in keyword uses the python build in list itorator 
'''


class ListNode: 
    def __init__(self, val): 
        self.val = val 
        self.next = None 

class LinkedList: 
    def __init__(self, head): 
        self.head = head 
        self.curr = None 

    # define iterator 
    def __iter__(self): 
        self.curr = self.head 
        return self 

    # Iterate 
    def __next__(self): 
        if self.curr: 
            val = self.curr.val 
            self.curr = self.curr.next
            return val 
        else: 
            raise StopIteration

        

head            = ListNode(1)
head.next       = ListNode(2)
head.next.next  = ListNode(3)
myList          = LinkedList(head)

for n in myList: 
    print(n)
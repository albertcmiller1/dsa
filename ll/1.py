class Node: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_ll(head):
    curr = head
    while curr: 
        print(curr.val)
        curr = curr.next
    return 


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

print_ll(head)
print("\n")

# find middle 
slow, fast = head, head.next 
while fast and fast.next: 
    slow = slow.next
    fast = fast.next.next
print(f"middle: {slow.val}")

print("\n")

# split 
second_half = slow.next 
slow.next = None

print_ll(head)
print("\n")
print_ll(second_half)
print("\n")


def reverse(head):
    curr = head
    prev = None
    while curr: 
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp 
    return prev 

# reverse second half
second = reverse(second_half)
print_ll(head)
print("\n")
print_ll(second)





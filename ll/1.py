class Node: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(head):
    curr = head
    while curr: 
        print(curr.val, id(curr))
        curr = curr.next
    print("\n")
    return 

def find_middle(head):
    # find middle 
    slow, fast = head, head.next 
    while fast and fast.next: 
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    curr = head
    prev = None
    while curr: 
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp 
    return prev 


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)


# print("id of head:   ", id(head))
middle = find_middle(head)
# print("id of middle: ", id(middle))

print("head: ")
print_ll(head)
# split 
second_half = middle.next 
middle.next = None
print("head after split: ")
print_ll(head)
print("second_half after split: ")
print_ll(second_half)

# reverse second half
second_half = reverse(second_half)
print("second_half after reverse: ")
print_ll(second_half)


first_half = head 
print("first half: ")
print_ll(first_half)


while first_half and second_half: 
    tmp1 = first_half.next
    tmp2 = second_half.next

    first_half.next = second_half
    second_half.next = tmp1

    first_half = tmp1
    second_half = tmp2

print("done: ")
print_ll(head)
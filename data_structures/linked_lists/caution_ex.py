
# this can give an error because the first expression (curr.next.val == curr.val) will be evaluated first 
# instead we need to check if there is indeed a curr.next
# error: 
# AttributeError: 'NoneType' object has no attribute 'val'
'''
curr = head 
while curr: 
    while curr.next.val == curr.val and curr.next:
        curr.next = curr.next.next 
    curr = curr.next
return head 
'''

# working example: 
'''
curr = head 
while curr: 
    while curr.next and curr.next.val == curr.val:
        curr.next = curr.next.next 
    curr = curr.next
return head 
'''
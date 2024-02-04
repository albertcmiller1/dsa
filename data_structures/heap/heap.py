import heapq

class Heap: 
    def __init__(self, nums): 
        self.heap = nums
        heapq.heapify(self.heap)

    def add(self, val): 
        heapq.heappush(self.heap, val)

    def pop(self): 
        heapq.heappop()

heap = Heap([4, 5, 3, 9])
print(heap.heap)
heap.add(9)
print(heap.heap[0])
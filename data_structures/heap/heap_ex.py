import heapq

# Note: Python's heapq implements a min heap
min_heap = [67, 341, 234, -67, 12, -976]
max_heap = [-n for n in min_heap]

# Min Heap 
heapq.heapify(min_heap)
heapq.heappush(min_heap, 7451)
heapq.heappush(min_heap, -5352)

# The numbers will be printed in sorted order
while min_heap:
    print(heapq.heappop(min_heap))

# Max Heap 
print("\n\n")
heapq.heapify(max_heap)
heapq.heappush(max_heap, 7451*-1)
heapq.heappush(max_heap, -5352*-1)

# The numbers will be printed in sorted order
while max_heap:
    print(-heapq.heappop(max_heap))


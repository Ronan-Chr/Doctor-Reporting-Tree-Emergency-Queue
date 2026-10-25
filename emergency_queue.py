class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency

# Defined minheap class for emergency queue
class MinHeap:
    def __init__(self):
        self.data = []

    # Heap method to insert a new patient into the heap
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.data[index].urgency < self.data[parent_index].urgency:
                self.data[index], self.data[parent_index] = self.data[parent_index], self.data[index]
                index = parent_index
            else:
                break


# Tests
p1 = Patient("Ronan", 6)
print(p1.name)  # Output: Ronan
print(p1.urgency)  # Output: 6

heap = MinHeap()
print(heap.data) # Output: []

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

    #Heap down method to maintain the heap property after removing the root
    def heapify_down(self, index):
        while True:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            smallest = index

            if (
                left_child < len(self.data)
                and self.data[left_child].urgency < self.data[smallest].urgency
            ):
                smallest = left_child

            if (
                right_child < len(self.data)
                and self.data[right_child].urgency < self.data[smallest].urgency
            ):
                smallest = right_child

            if smallest == index:
                break

            self.data[index], self.data[smallest] = (self.data[smallest], self.data[index])
            index = smallest


    #defined patient insert method to add a new patient to the heap
    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    #print method for actually seeing what the heap looks like when we call it
    def print_heap(self):
        for patient in self.data:
            print(f"Patient: {patient.name} ({patient.urgency})")

    #peek is for checking the patient list without removing the patient from the heap. This is useful for checking the next patient to be treated without modifying the queue.
    def peek(self):
        if len(self.data) == 0:
            return None
        return self.data[0]

    #Defined the remove min method 
    def remove_min(self):
        if len(self.data) == 0:
            return None

        if len (self.data) == 1:
            return self.data.pop()

        most_urgent=self.data[0]
        self.data[0] = self.data.pop()
        self.heapify_down(0)

        return most_urgent

# Tests
p1 = Patient("Ronan", 6)
print(p1.name)  # Output: Ronan
print(p1.urgency)  # Output: 6

heap = MinHeap()
print(heap.data) # Output: []


#HEAP TESTS (Help from AI to create these tests)
heap = MinHeap()

# Test heapify_up
heap.data = [
    Patient("Jordan", 3),
    Patient("Avery", 5),
    Patient("Taylor", 1)
]

heap.heapify_up(2)
print(heap.data[0].name)  # Taylor

# Test heapify_down
heap.data = [
    Patient("Avery", 5),
    Patient("Jordan", 3),
    Patient("Taylor", 1)
]

heap.heapify_down(0)
print(heap.data[0].name)  # Taylor

heap.insert(Patient("Kevin", 9))
heap.insert(Patient("Ann", 1))
heap.print_heap()

next_up = heap.peek()
print("Next patient to be treated:", next_up.name, next_up.urgency)
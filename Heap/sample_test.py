class MaxHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return str(self.heap)

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, key):
        self.heap.append(key)
        self.sift_up(len(self.heap) - 1)

    def extract_max(self):
        if self.is_empty():
            return None
        max_value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.sift_down(0)
        return max_value

    def sift_up(self, i):
        while i > 0 and self.heap[i] > self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def sift_down(self, i):
        while self.left(i) < len(self.heap) or self.right(i) < len(self.heap):
            largest = i
            if self.left(i) < len(self.heap) and self.heap[self.left(i)] > self.heap[largest]:
                largest = self.left(i)
            if self.right(i) < len(self.heap) and self.heap[self.right(i)] > self.heap[largest]:
                largest = self.right(i)
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
                i = largest

# Example usage
heap = MaxHeap()
heap.insert(10)
heap.insert(5)
heap.insert(15)
heap.insert(2)
heap.insert(7)

print("Max heap:", heap)
print("Extracted max:", heap.extract_max())
print("Max heap after extraction:", heap)

class QueueImpl:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.pop(0) if self.queue else None

def test_queue():
    queue = QueueImpl()
    
    # Enqueue elements
    queue.enqueue(10)
    queue.enqueue(20)
    print("Dequeued element:", queue.dequeue())  # Output: 10
    print("Dequeued element:", queue.dequeue())  # Output: 20
    print("Dequeued element from empty queue:", queue.dequeue())  # Output: None

    print("All Queue tests passed!")


# Test Queue
test_queue()

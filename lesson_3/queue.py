class NewQueue:

    def __init__(self):
        self.items = []

    def enq_item(self, item):
        self.items.append(item)

    def deq_item(self):
        if self.items:
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return self.items

    def size_queue(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items!r}"


queue = NewQueue()
queue.enq_item(1)
print(queue)
queue.deq_item()
print(queue)
print(queue.size_queue())

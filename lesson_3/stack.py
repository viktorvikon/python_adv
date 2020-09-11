class Stack:

    def __init__(self):
        self.items = []

    def push_item(self, item):
        self.items.append(item)

    def pop_item(self):
        if self.items:
            self.items.pop()
        else:
            print("Stack is empty")
            return self.items

    def peek(self):
        if self.items:
            print(self.items[len(self.items) - 1])
            return self.items[len(self.items) - 1]
        else:
            print("Stack is empty")
            return self.items

    def __str__(self):
        return f"{self.items!r}"


first_stack = Stack()
print("-" * 45)
print(first_stack)
first_stack.push_item(1)
first_stack.push_item(2)
first_stack.push_item(3)
first_stack.push_item(4)
print("-" * 45)
print(first_stack)
first_stack.peek()
first_stack.pop_item()
print("-" * 45)
print(first_stack)
print("-" * 45)

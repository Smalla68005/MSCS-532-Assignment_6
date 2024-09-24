class Stack:
    def __init__(self):
        self.stack =[]

    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
       return  self.stack.pop()
    
    def peek(self):
        return self.stack[-1] if self.stack else None
    
def test_stack():
    stack = Stack()
    
    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element:", stack.peek())  # Output: 30

    # Pop element
    print("Popped element:", stack.pop())  # Output: 30
    print("Top element after pop:", stack.peek())  # Output: 20

    # Test popping the last element
    stack.pop()
    print("Top element after popping last:", stack.peek())  # Output: 10

    print("All Stack tests passed!")


# Test Stack
test_stack()
class OperatorStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            exit(1)
        return self.stack.pop()
    
    def top(self):
        return self.stack[-1] if len(self.stack) != 0 else ''

    def pop_multiple(self):
        return float(self.stack.pop()), float(self.stack.pop())

    def is_empty(self):
        return len(self.stack) == 0

    def is_empty_2(self):
        return len(self.stack)

    def size(self):
        return self.stack.size()


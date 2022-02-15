class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def push(self, item):
        self.stack.append(item)

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def peek(self):
        peek_item = self.stack[-1]
        return peek_item

    def size(self):
        if len(self.stack) == 0:
            return None
        else:
            return len(self.stack)



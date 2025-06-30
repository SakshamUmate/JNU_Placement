class Stack:
    def __init__(self) -> None:
        self.stack =[]
        self.top = 0
    def push(self, data):
        self.stack.append(data)
        self.top += 1
    def pop(self):
        if self.top == 0:
            return None
        self.top -=1
        return self.stack.pop()
    def peek(self):
        if self.top == 0:
            return None
        return self.stack[-1]
    def is_empty(self):
        return self.top == 0
    def size(self):
        return self.top
    def __str__(self) -> str:
        return str(self.stack)
    def peep(self ,i=None):
        if self.top == 0:
            return 'Stack is empty'
        if i is None:
            return str(self.stack)
        if i < 1 or i >= self.top:
            return 'Index out of range'
        return self.stack[-i]
        
    
    
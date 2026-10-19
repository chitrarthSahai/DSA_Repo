import math
class MinStack:
    #the idea is to maintain the currentMin for each value pushed in the stack, this can be done by pushing a tuple of (val, currentMin) to the stack and then peeking/popping as required.
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        #If stack is not empty, peek the top to get currentMin and compute current minimum again for this push
        pushMin = val
        if self.stack:
            top = self.stack[-1]
            pushMin = min(top[1], val)
        
        self.stack.append((val, pushMin))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]
        

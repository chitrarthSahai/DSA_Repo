class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        self.queue.appendleft(x)

    def pop(self) -> int:
        #rotate the array to bring everything last to the front except the first element which becomes last and dequeues
        size = len(self.queue)
        self.queue.rotate(size-1)

        return self.queue.pop()
        

    def top(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return True if len(self.queue) == 0 else False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
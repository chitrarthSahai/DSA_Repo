class DoublyLinkedListNode:
    def __init__(self, site: str) -> None:
        self.site = site
        self.prev = None
        self.nxt = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = DoublyLinkedListNode(site=homepage)
        self.length = 1
        self.curptr = 0
        

    def visit(self, url: str) -> None:
        site = DoublyLinkedListNode(site=url)

        #We clear all the forward history by inserting new website after current node wiht next pointer as None
        self.current.nxt = site
        site.prev = self.current
        self.current = self.current.nxt

        self.curptr += 1
        self.length = self.curptr + 1


    def back(self, steps: int) -> str:
        #Calculate how much steps we need to move back the current pointer, if steps > curptr we can just go back upto curptr times and return the first DoublyLinkedListNode

        moveBack = min(steps, self.curptr)


        for i in range(moveBack):
            self.current = self.current.prev
            self.curptr -= 1

        return self.current.site

        

    def forward(self, steps: int) -> str:
        #Calculate how much steps we need to move forward, if steps > self.length - self.curptr - 1 then we can only go forward self.length - self.curptr - 1 times ahead.

        moveAhead = min(steps, (self.length - self.curptr - 1))

        for i in range(moveAhead):
            self.current = self.current.nxt
            self.curptr += 1
        
        return self.current.site


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
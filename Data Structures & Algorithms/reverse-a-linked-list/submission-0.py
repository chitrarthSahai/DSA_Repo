# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #We have to reverse the pointer of each node, but before breaking the link save the next item value 

        #initialize a current to start of head, this will become our new tail
        curr = head

        #initialize the previous element to null as we shift item

        prev = None

        while curr != None:
            #Save the next link
            nextVal = curr.next
            #break the link and point to previous
            curr.next = prev

            #First shift the previous to current
            prev = curr

            #Then use the nextVal stored to shift the current to next val
            curr = nextVal

        return prev

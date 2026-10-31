# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Recusrsive Solution - Time O(n), space O(n), not most optimal

        #if linked list ends, return None (Base condition)
        if not head:
            return None
        
        newHead = head

        #till head has next
        if head.next:
            # start going into the recursion depth, till the base condition above returns None,
            newHead = self.reverseList(head.next)
            #After the return from the base condition, this line runs with the last element of the linked list
            #reversing the pointer. 1->2. Head's next is 2, and 2's next is set back to 1, so basically creating a cyclic link for the time being
            head.next.next = head

        #Set the next pointer to null, to break the cyclic link above and make the current head point to other direction i.e. None
        head.next = None

        #return newHead for every recursion call, this returns the first node of the reveresed link list.
        return newHead





        

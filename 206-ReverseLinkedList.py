class Solution:
    head = [1,2,3,4,5]
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None

        return newHead
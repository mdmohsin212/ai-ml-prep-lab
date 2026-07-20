class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode()
        right = ListNode()
        
        l = left
        r = right
        tmp = head

        while tmp is not None:
            if tmp.val < x:
                l.next = tmp
                l = l.next
            else:
                r.next = tmp
                r = r.next
            tmp = tmp.next
        
        l.next = right.next
        r.next = None
        return left.next
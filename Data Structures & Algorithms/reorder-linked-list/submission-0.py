class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        prev = None
        cur = second
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        left = head
        right = prev
        while right is not None:
            leftnext = left.next
            rightnext = right.next
            left.next = right
            right.next = leftnext
            left = leftnext
            right = rightnext
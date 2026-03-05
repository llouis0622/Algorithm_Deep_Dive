class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0)
        cur = head
        while cur:
            prev = dummy
            while prev.next and prev.next.val < cur.val:
                prev = prev.next
            nxt = cur.next
            cur.next = prev.next
            prev.next = cur
            cur = nxt
        return dummy.next
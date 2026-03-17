class Solution:
    def isPalindrome(self, head):
        s = head
        e = head
        while e and e.next:
            s = s.next
            e = e.next.next
        prev = None
        cur = s
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        l = head
        r = prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
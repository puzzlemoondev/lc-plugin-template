from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        p1, p2 = l1, l2
        dummy_sum = ListNode(-1)
        p = dummy_sum
        carry = 0
        while p1 or p2 or carry:
            n = carry
            if p1:
                n += p1.val
                p1 = p1.next
            if p2:
                n += p2.val
                p2 = p2.next
            carry, digit = divmod(n, 10)
            p.next = ListNode(digit)
            p = p.next
        return dummy_sum.next
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
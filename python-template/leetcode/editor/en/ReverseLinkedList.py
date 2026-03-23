from typing import *
from leetcode.editor.common.node import *

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre, cur, nxt = None, head, head.next
        while cur:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt:
                nxt = nxt.next
        return pre
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
from typing import Optional
from leetcode.editor.common.node import ListNode

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy_head = ListNode(-1)
        merged = dummy_head
        while p1 and p2:
            if p1.val < p2.val:
                merged.next = p1
                p1 = p1.next
            else:
                merged.next = p2
                p2 = p2.next
            merged = merged.next
            merged.next = None

        remaining = p1 or p2
        if remaining:
            merged.next = remaining

        return dummy_head.next



        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
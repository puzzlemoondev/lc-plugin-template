from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nodes = []

        def traverse(node: Optional[TreeNode]) -> None:
            if node is None:
                return

            nodes.append(node.val)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return nodes
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
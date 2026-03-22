# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        nodes = []

        def traverse(node):
            if node is None:
                return

            if children := node.children:
                for child in children:
                    traverse(child)

            nodes.append(node.val)
            
        traverse(root)
        return nodes
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
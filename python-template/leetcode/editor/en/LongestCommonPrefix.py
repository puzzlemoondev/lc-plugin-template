from typing import *
from leetcode.editor.common.node import *


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return "".join(self._get_common_prefix_list(strs))

    @staticmethod
    def _get_common_prefix_list(strs: List[str]) -> list[str]:
        common_prefix: list[str] = []

        len_strs = len(strs)
        n = 0
        while True:
            cur: str | None = None
            for i in range(len_strs):
                if n >= len(strs[i]):
                    return common_prefix
                char = strs[i][n]
                if cur is None:
                    cur = char
                elif cur != char:
                    return common_prefix
            if cur is not None:
                common_prefix.append(cur)
                n += 1
        return common_prefix


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here

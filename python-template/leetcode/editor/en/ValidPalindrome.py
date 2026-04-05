# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self._sanitize(s)

        n = len(s)
        if n <= 1:
            return True

        left, right = 0, n - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    @staticmethod
    def _sanitize(s: str) -> str:
        return "".join(char.lower() for char in s if char.isalnum())


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here

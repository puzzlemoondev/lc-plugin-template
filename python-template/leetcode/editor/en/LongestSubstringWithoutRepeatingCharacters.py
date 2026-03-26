from collections import Counter

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = Counter()

        left = right = 0 # [left, right)
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            res = max(res, right - left)

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
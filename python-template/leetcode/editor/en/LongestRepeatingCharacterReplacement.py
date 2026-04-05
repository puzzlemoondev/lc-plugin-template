# leetcode submit region begin(Prohibit modification and deletion)
from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq = Counter()
        window_max_freq = 0

        # when to increase window size: right - left - window_max_freq <= k
        # when to decrease window size: right - left - window_max_freq > k
        n = len(s)
        left = right = 0
        res = 0
        while right < n:
            c = s[right]
            window_freq[c] += 1
            window_max_freq = max(window_max_freq, window_freq[c])
            right += 1
            while right - left - window_max_freq > k:
                d = s[left]
                window_freq[d] -= 1
                left += 1
            res = max(res, right - left)

        return res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here

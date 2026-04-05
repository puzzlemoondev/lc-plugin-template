from collections import Counter


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needs = Counter(s1)
        window = Counter()

        left = right = 0  # [left,right)
        valid_chars = 0

        while right < len(s2):
            # char to put into window
            c = s2[right]
            # INCREASE WINDOW
            right += 1
            # UPDATE WINDOW
            if c in needs:
                window[c] += 1
                if window[c] == needs[c]:
                    valid_chars += 1

            # check needs decrease window
            while right - left >= len(s1):
                # return when needs satisfied
                if valid_chars == len(needs):
                    return True
                d = s2[left]
                # DECREASE WINDOW
                left += 1
                # UPDATE WINDOW
                if d in needs:
                    if window[d] == needs[d]:
                        valid_chars -= 1
                    window[d] -= 1

        return False


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    solution = Solution()
    # your test code here

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = right = 0
        window = set[int]()
        while right < len(nums):
            if nums[right] in window:
                return True
            window.add(nums[right])
            right += 1
            while right - left > k:
                window.remove(nums[left])
                left += 1
        return False
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    solution = Solution()
    # your test code here
    
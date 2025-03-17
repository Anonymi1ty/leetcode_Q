#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# 同样可以使用快慢指针问题，将数组覆盖
# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i =0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
            
        
# @lc code=end


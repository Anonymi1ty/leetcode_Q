#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# 回文经典双指针问题（调用自带的方法要加.lower())
# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 先准备一个数组接收
        temp = []
        for character in s:
            if character.isalnum():
                temp.append(character.lower())
        # 设置前后指针
        i, j = 0, len(temp)-1
        while i <= j:
            if temp[i] != temp[j]:
                return False
            i += 1
            j -= 1
        return True
        
# @lc code=end


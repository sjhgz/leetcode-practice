#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            思路: 假设 sum_ 为 以下标为 i 的元素结尾，且和最大的连续子数组的和。
                因为满足条件的子序列，无论其首元素始于何处，其结尾的元素，必然是原数组中的某一个元素。
                抓住了这个点之后，就只需要考虑子序列一端的变化情况。
                这是解决这道题的关键思路点。

            思维误区: 同时考虑子序列两端的变化情况（如 什么时候该移除子序列首位的元素，
                    什么时候该加追加子序列尾部的元素）。这会让问题变得复杂，无从下手。
        """
        if not nums:
            return 0
        length = len(nums)
        if not length > 1:
            return nums[0]
        sum_ = nums[0]
        max_ = sum_
        for idx in xrange(1, length):
            num = nums[idx]
            new_sum = sum_ + num
            if new_sum < num:
                sum_ = num
            else:
                sum_ += num
            if sum_ > max_:
                max_ = sum_
        return max_
            
# @lc code=end


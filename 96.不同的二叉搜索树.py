#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#
# https://leetcode-cn.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (65.29%)
# Likes:    518
# Dislikes: 0
# Total Accepted:    43.9K
# Total Submissions: 66.9K
# Testcase Example:  '3'
#
# 给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？
#
# 示例:
#
# 输入: 3
# 输出: 5
# 解释:
# 给定 n = 3, 一共有 5 种不同结构的二叉搜索树:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        """
            首先 明确什么是二叉搜索树
            其次 找到问题对应的算法思想
            随后 运营对应的算法解决问题

            动态规划:
                当 n <= 2:
                    f(1) = 1
                    f(2) = 2 
                当 n >= 3:
                    f(n) = f(n-1)*f(n-1) + f(n-2)*f(2-1) \
                        + f(n-3)*f(3-1) + ... \
                        + f(n-n)*f(n-1)
        """
        if n <= 2:
            return n
        sum_ = 0
        # 令 f(0) = 1, 方便计算
        cache = [1, 1, 2]
        j = 3
        while True: 
            sum_ = 0
            for i in range(1, j+1):
                sum_ += cache[j-i] * cache[i-1]
            cache.append(sum_)
            # 满足输入，返回结果
            if j == n:
                return sum_
            j += 1
# @lc code=end


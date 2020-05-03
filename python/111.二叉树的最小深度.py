#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (42.21%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    71K
# Total Submissions: 168.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# 返回它的最小深度  2.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        """
            思路: 循环判断每个节点是否存在两个子节点，
                如果都不存在的话, 循环停止，这个节点即
                是最小深度的节点
        """
        if not root:
            return 0
        node_list = [root]
        depth = 0
        while node_list:
            tmp = []
            depth += 1
            for node in node_list:
                left_node = node.left
                right_node = node.right
                if (not left_node \
                    and not right_node):
                    return depth
                if left_node: # 满足非空
                    tmp.append(left_node)
                if right_node: # 满足非空
                    tmp.append(right_node)
            node_list = tmp
        # 一个子节点也没有的情况
        return depth

# @lc code=end


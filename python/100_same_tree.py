# coding: utf-8

# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#
# 思路： 这道题跟101题是同一个类型的题目，只不过一个是判断对称，
# 一个是判断完全相同，注意 「对称」 与 「相同」 的区别。
class Solution(object):

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            # 注意这个条件分支跟上一个条件分支的顺序不能互换
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

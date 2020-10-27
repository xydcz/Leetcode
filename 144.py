from binarytree import tree

# 递归
# class Solution:
#     def preorder(self, root):
#         self.nums = []
#
#         def pre(root):
#             if not root:
#                 return
#             self.nums.append(root.val)
#             pre(root.left)
#             pre(root.right)
#         pre(root)
#         return self.nums

# 迭代
class Solution:
    def preorder(self, root):
        tree = [root]
        nums = []
        while tree:
            n = tree.pop()
            nums.append(n.val)
            if n.right:
                tree.append(n.right)
            if n.left:
                tree.append(n.left)
        return nums


tree = Tree()
tree.add(1)
tree.add(None)
tree.add(2)
tree.add(None)
tree.add(None)
tree.add(3)
cs = Solution()
print(cs.preorder(tree.root))
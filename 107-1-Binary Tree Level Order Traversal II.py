# https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/


from collections import deque


class TreeNode(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


class Tree(object):
    def __init__(self):
        self.root = TreeNode()
        self.myQueue = []

    def add(self, val):
        node = TreeNode(val)

        # 如果树是空的，则对根节点赋值
        if self.root.val == -1:
            self.root = node
            self.myQueue.append(self.root)
            print(self.myQueue, self.root.val, 'top')

        # 如果有根节点
        else:
            treeNode = self.myQueue[0]  # 检查myQueue[0]的子树
            if treeNode.left == None:
                treeNode.left = node
                self.myQueue.append(treeNode.left)
                print(self.myQueue, self.root.val, 'left')
            else:
                treeNode.right = node
                self.myQueue.append(treeNode.right)
                self.myQueue.pop(0)  # myQueue[0]节点左右都有了，pop掉
                print(self.myQueue, self.root.val, 'right')

    def level_queue(self, root):
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print(node.val)
            if node.left != None:
                myQueue.append(node.left)
            if node.right != None:
                myQueue.append(node.right)


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []

        ans = [[root.val]]
        queue = deque([root])
        while queue:
            levelans = []
            for _ in range(len(queue)):
                root = queue.popleft()
                if root.left:
                    levelans.append(root.left.val)
                    queue.append(root.left)
                if root.right:
                    levelans.append(root.right.val)
                    queue.append(root.right)
            if levelans:
                ans.append(levelans)
        return ans[::-1]


vals1 = []
vals2 = [3, 9, 20, None, None, 15, 7]
tree = Tree()

for i in range(len(vals2)):
    tree.add(vals2[i])

# tree.level_queue(tree.root)  # root是最后建立出的树
print(Solution().levelOrderBottom(tree.root))

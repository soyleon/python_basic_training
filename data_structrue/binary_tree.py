# coding=utf-8


"""
二叉树实现
"""


class Node(object):
    """二叉树的节点类，树的节点有当前的元素，左节点与右节点"""
    def __init__(self, elem=None, lchid=None, rchild=None):
        self.elem = elem
        self.lchild = lchid
        self.rchild = rchild


class Tree(object):
    """树类，建立二叉树，并向树内添加元素"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树增加节点"""
        node = Node(elem)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild is None:
                    cur.lchild = node
                    return
                elif cur.rchild is None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def preorder(self,root):
        if root is None:
            return
        else:
            print(root.elem, end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self,root):
        if root is None:
            return
        else:
            self.inorder(root.lchild)
            print(root.elem, end=" ")
            self.inorder(root.rchild)

    def posorder(self,root):
        if root is None:
            return
        else:
            self.posorder(root.lchild)
            self.posorder(root.rchild)
            print(root.elem, end=" ")

    def deep_travel(self):
        root = self.root
        if root is None:
            return
        else:
            queue = [root]
            while queue:
                cur = queue.pop(0)
                print(cur.elem, end=" ")
                if cur.lchild is not None:
                    queue.append(cur.lchild)
                if cur.rchild is not None:
                    queue.append(cur.rchild)


if __name__ == "__main__":
    node = Node()
    fnode = Tree()
    fnode.add(3)
    fnode.add(5)
    fnode.add(6)
    fnode.add(1)
    fnode.add(8)
    fnode.add(9)
    fnode.add(2)
    fnode.add(7)
    fnode.add(0)
    #  fnode.preorder(fnode.root)
    fnode.deep_travel()

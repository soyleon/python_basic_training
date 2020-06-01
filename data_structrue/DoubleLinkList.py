# coding: utf-8


class Node(object):
    def __init__(self, item):
        self.prev = None
        self.elem = item
        self.next = None


class DoubleLinkList(object):
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head is None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部增加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        node.next.prev = node

    def append(self, item):
        """链表尾部增加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
            node.prev = cur

    def insert(self, pos, item):
        """制定位置添加元素
        : para : pos 从0开始
        """
        if pos < 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            node = Node(item)
            while count < pos-1:
                pre = pre.next
                count += 1
            node.next = pre.next
            node.prev = pre
            pre.next.prev = node
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return self
        else:
            pre = self.__head
            if pre.elem == item:
                if pre.next is None:
                    self.__head = None
                else:
                    self.__head = pre.next
                    pre.next.prev = None
            else:
                while pre.next is not None:
                    if pre.next.elem == item:
                        pre.next = pre.next.next
                        if pre.next is not None:
                            pre.next.prev = pre
                        else:
                            pre.next = None
                        break
                    else:
                        pre = pre.next

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while (cur is not None):
            if cur.elem == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    print(dll.is_empty())
    print(dll.length())

    dll.append(1)
    print(dll.is_empty())
    dll.remove(1)
    print(dll.length())

    dll.append(2)
    dll.add(8)
    dll.append(3)
    dll.append(4)

    dll.append(5)
    dll.append(6)
    dll.insert(-1, 9)
    dll.insert(-1, 9)
    dll.insert(3, 100)
    dll.insert(10, 200)
    dll.append(100)
    dll.append(100)
    dll.travel()
    dll.remove(9)
    dll.travel()
    dll.remove(100)
    dll.travel()

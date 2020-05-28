class Node(object):
    """单链表的结点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None
        pass


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部增加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部增加元素,尾插法"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

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
            pre.next = node

    def remove(self, item):
        """删除节点"""
        if self.is_empty():
            return self
        else:
            pre = self.__head
            if pre.elem == item:
                self.__head = pre.next
            else:
                while pre.next != None :
                    if pre.next.elem == item:
                        pre.next = pre.next.next
                    else:
                        pre = pre.next

    def search(self, item):
        """查找结点是否存在"""
        cur = self.__head
        while (cur != None):
            if cur.elem == item:
                return True
            cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.search(1))
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())

    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(-1, 9)
    ll.insert(3, 100)
    ll.insert(10, 200)
    ll.append(100)
    ll.append(100)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(100)
    ll.travel()

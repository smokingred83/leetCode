from __future__ import annotations
from utils.my_node import MyNode


class MyQueueNode(MyNode):
    def __init__(self, data):
        super().__init__(data)
        self._next: MyQueueNode = None

    @classmethod
    def copy(cls, node: MyQueueNode):
        n = MyQueueNode(node.data)
        n.adjacent = node.adjacent
        return n

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value
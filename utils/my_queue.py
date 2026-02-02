from utils.my_queue_node import MyQueueNode


class MyQueue:
    def __init__(self):
        self._first: MyQueueNode = None
        self._last: MyQueueNode = None

    def add(self, node: MyQueueNode):
        n = MyQueueNode.copy(node)
        if self._last is not None:
            self._last.next = n
        self._last = n
        if self._first is None:
            self._first = self._last

    def remove(self):
        if self._first is None:
            raise Exception()
        tmp = self._first
        self._first = self._first.next
        if self._first is None:
            self._last = None
        return tmp

    def peek(self):
        if self._first is None:
            raise Exception()
        return self._first.data

    def is_empty(self) -> bool:
        return self._first is None
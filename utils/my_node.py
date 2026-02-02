from __future__ import annotations
from utils.status import Status

class MyNode:
    def __init__(self, data):
        self.adjacent: [MyNode] = []
        self.status: Status = Status.Unvisited
        self.data = data

    def __repr__(self):
        return f"{self.data!r} --> {', '.join([n.data for n in self.adjacent])!r}"
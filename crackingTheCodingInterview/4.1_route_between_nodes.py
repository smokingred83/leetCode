from utils.my_graph import MyGraph
from utils.my_node import MyNode
from utils.my_queue import MyQueue
from utils.my_queue_node import MyQueueNode
from utils.status import Status


def search(graph: MyGraph, s: MyNode, e: MyNode) -> bool:
    start = search_node(graph.nodes[0], s, [Status.Unvisited], Status.Visiting)
    if start is None:
        return False
    end = search_node(start, e, [Status.Unvisited, Status.Visiting], Status.Visited)
    return end is not None


def search_node(root: MyQueueNode, n: MyQueueNode, statuses: [Status], new_status: Status):
    if root is not None:
        queue = MyQueue()
        queue.add(root)
        while not queue.is_empty():
            node = queue.remove()
            if node.data == n.data:
                return node
            for tmp in node.adjacent:
                if tmp.status in statuses:
                    tmp.status = new_status
                    queue.add(tmp)
            node.status = new_status
    return None


if __name__ == "__main__":
    graph = MyGraph()
    a = MyQueueNode("A")
    b = MyQueueNode("B")
    c = MyQueueNode("C")
    d = MyQueueNode("D")
    e = MyQueueNode("E")
    f = MyQueueNode("F")
    a.adjacent += [b, e, f]
    b.adjacent += [d, e]
    c.adjacent += [b]
    d.adjacent += [c, e]
    graph.nodes = [a, b, c, d, e, f]
    res = search(graph, c, e)
    res

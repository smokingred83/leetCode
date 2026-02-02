from utils.my_node import MyNode


class MyTreeNode(MyNode):
    def __init__(self, data):
        super().__init__(data)
        self.left: MyTreeNode = None
        self.right: MyTreeNode = None
        self.parent: MyTreeNode = None

    def __repr__(self):
        return (f"{self.parent.data if self.parent else ''}: "
                f"{self.left.data if self.left else ''} "
                f"<-- {self.data} --> "
                f"{self.right.data if self.right else ''}"
                f"")
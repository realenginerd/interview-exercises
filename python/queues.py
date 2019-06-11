class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def top(self):
        return self.items[-1]


class QueueStack:
    def __init__(self):
        pass

    def push(self, item):
        pass

    def pop(self):
        pass

    def is_empty(self):
        pass

    def top(self):
        pass


def test_queue_stack():
    stack = QueueStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    assert stack.top() == 4
    stack.pop()
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 2
    stack.push(3)
    assert stack.top() == 3
    stack.pop()
    assert stack.top() == 2


if __name__ == '__main__':
    test_queue_stack()

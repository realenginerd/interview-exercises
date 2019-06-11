# TODO: figure out how to test empty case
# TODO: write real unit tests
# TODO: factor out Queue


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
        return self.items[0]


class QueueStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        self.queue.enqueue(item)

    def pop(self):
        new_queue = Queue()
        result = self.queue.top()
        dequeue = self.queue.dequeue()
        while result != dequeue:
            new_queue.enqueue(dequeue)
            dequeue = self.queue.dequeue()
        self.queue = new_queue
        return result

    def is_empty(self):
        return self.queue.is_empty()

    def top(self):
        return self.queue.top()


def test_queue_stack():
    stack = QueueStack()
    stack.push(1)
    assert stack.top() == 1
    stack.pop()
    # assert stack.top() == False # TODO
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.top())
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

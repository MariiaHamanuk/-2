class MyQueue(object):

    def __init__(self):
        self.inn = []
        self.out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.inn.append(x)
        # self.out.append(x)
    def pop(self):
        """
        :rtype: int
        """
        if not self.out:
            while self.inn:
                self.out.append(self.inn.pop())
        return self.out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if not self.out:
            while self.inn:
                self.out.append(self.inn.pop())
        return self.out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.inn and not self.out

# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
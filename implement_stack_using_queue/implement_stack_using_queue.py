import collections

class MyStack(object):
    '''
    My stack class
    '''
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # self.queue2.append(x)
        # while self.queue1:
        #     self.queue2.append(self.queue1.popleft())
        # self.queue1, self.queue2 = self.queue2, self.queue1
        self.queue1.append(x)
    def pop(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        popp = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        # return self.queue1.popleft()
        return popp

    def top(self):
        """
        :rtype: int
        """
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft()) # just like in pop



        top = self.queue1.popleft()
        self.queue2.append(top)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top
        # return self.queue1[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.queue1

# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
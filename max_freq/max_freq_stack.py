'''
freq
'''
class FreqStack(object):
    '''
    freq
    '''
    def __init__(self):
        self.frequenc = {}
        self.group = {}
        self.max_freq = 0


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if val not in self.frequenc:
            self.frequenc[val] = 0
        self.frequenc[val] += 1

        fr = self.frequenc[val]

        if fr not in self.group:
            self.group[fr] = []

        self.group[fr].append(val)

        if fr > self.max_freq:
            self.max_freq = fr

    def pop(self):
        """
        :rtype: int
        """
        value = self.group[self.max_freq].pop() # not peek!!!!

        self.frequenc[value] -= 1
        if not self.group[self.max_freq]:


            del self.group[self.max_freq]
            self.max_freq -= 1
        return value

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
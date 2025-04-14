'''
freq
'''
class FreqStack(object):
    '''
    freq
    '''
    def __init__(self):
        self.freq = {}
        self.group = {}
        self.max_freq = 0


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val not in self.freq:
            self.freq[val] = 0
        self.freq[val] += 1
        f = self.freq[val]

        if f not in self.group:
            self.group[f] = []
        self.group[f].append(val)

        if f > self.max_freq:
            self.max_freq = f

    def pop(self):
        """
        :rtype: int
        """
        val = self.group[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.group[self.max_freq]:
            del self.group[self.max_freq]
            self.max_freq -= 1
        return val

class FirstN:
    def __init__(self, n):
        self.num = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.num < self.n:
            i = self.num
            self.num += 1
            return i
        else:
            raise StopIteration()

iterator = FirstN(100)

for item in iterator:
    print item

#x = iter([1, 2, 3])
#print x.next()
#print x.next()
#print x.next()


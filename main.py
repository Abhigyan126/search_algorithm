class SeqSer:
    def __init__(self):
        self.arr = None
        self.key = None
        self.temp = 0
        self.low = None
        self.high = None
        self.mid = None
        self.B = int()
        self.norm = None
        self.temp2 = None

    def linear_search(self, arr, key):
        self.temp = 0
        self.arr = arr
        self.key = key
        for self.temp in self.arr:
            print(self.temp)
            if self.arr[self.temp] == self.key:
                return self.temp

    def binary_search(self, arr, key, low, high, norm=True):
        self.arr = arr
        self.norm = norm
        self.key = key
        self.low = low
        self.high = high
        if self.norm:
            self.low = 0
            self.high = len(self.arr) - 1
        while self.low <= self.high:
            self.mid = self.low + (self.high - self.low) // 2
            if self.arr[self.mid] == self.key:
                return self.mid
            if self.arr[self.mid] < self.key:
                self.low = self.mid + 1
            else:
                self.high = self.mid - 1
        return -1

    def jump_search(self, arr, key):
        self.arr = arr
        self.key = key
        self.temp = 0
        self.B = 0
        while self.temp != len(self.arr) - 1 and self.arr[self.temp] < self.key:
            if self.arr[int(self.temp + (len(self.arr) ** (1 / 2)) - 1)] == self.key:
                return self.temp + (len(self.arr) ** (1 / 2)) - 1
            elif self.arr[int(self.temp + (len(self.arr) ** (1 / 2)) - 1)] > self.key:
                self.B = self.arr[self.temp: self.temp + (len(self.arr) ** (1 / 2)) - 1]
                return self.linear_search(self.B, self.key) + self.temp
            self.temp += 1
            self.temp2 = int(self.temp + (len(self.arr) ** (1 / 2)))
            self.B = self.arr[self.temp: self.temp2]
            print(self.B)
            return self.linear_search(self.B, self.key) + self.temp

    def interpolation_search(self, arr, key, low=0, high=0):
        self.arr = arr
        self.low = low
        self.high = high
        self.key = key
        self.low = 0
        self.high = 0
        if self.low <= self.high and self.arr[self.low] <= self.key <= self.arr[self.high]:
            self.temp = self.low + ((self.high - self.low) // (self.arr[self.high] - self.arr[self.low]) * (
                    self.key - self.arr[self.low]))
            if self.arr[self.temp] == self.key:
                return self.temp
            if self.arr[self.temp] < self.key:
                return self.interpolation_search(self.arr, self.key, self.low, self.temp + 1)
            if self.arr[self.temp] > self.key:
                return self.interpolation_search(self.arr, self.key, self.low, self.temp - 1)
        return -1

    def exponential_search(self, arr, key):
        self.arr = arr
        self.key = key
        self.temp = 0
        if not arr:
            return -1
        self.temp = 1
        while self.temp < len(self.arr) and self.arr[self.temp] < self.key:
            self.temp *= 2
        return self.binary_search(self.arr, self.key, self.temp // 2, min(self.temp, len(self.arr) - 1), norm=False)


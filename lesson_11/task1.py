class Triangle:
    def __init__(self, arr):
        self.arr = arr

    def is_possible(self):
        max_el = self.arr.pop(self.arr.index(max(self.arr)))
        for i in range(1):
            return (self.arr[i] + self.arr[i + 1]) > max_el


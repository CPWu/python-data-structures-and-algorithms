import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.make_array(self.capacity)

    def __len__(self):
        return self.n

    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!')
        return self.A[k]

    def append(self, element):
        if self.n == self.capacity:
            self._resize(2*self.capacity) # 2x if capacity is not enough
        
        self.A[self.n] = element
        self.n += 1

    def _resize(self, new_capacity):
        B = self.make_array(new_capacity)

        for k in range (self.n):
            B[k] = self.A[k]

        self.A = B
        self.capacity = new_capacity

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()



arr = DynamicArray()
arr.append(1)
print(arr[0])

arr.append(2)
print(arr[1])
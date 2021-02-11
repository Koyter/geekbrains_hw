class Road:
    def __init__(self, _length, _width, volume, depth):
        self._length = _length
        self._width = _width
        self.volume = volume
        self.depth = depth

    def mass(self):
        return self._length * self._width * self.volume * self.depth


class MassCount(Road):
    def __init__(self, _length, _width, volume, depth):
        super().__init__(_length, _width, volume, depth)


r = MassCount(30, 5000, 25, 5)
print(r.mass())
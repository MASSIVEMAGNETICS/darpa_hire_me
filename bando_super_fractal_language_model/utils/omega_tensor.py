import numpy as np

class OmegaTensor:
    """A simple tensor class for the Bando Super Fractal Language Model."""

    def __init__(self, data):
        self.data = np.array(data)

    def __repr__(self):
        return f"OmegaTensor({self.data})"

    def __add__(self, other):
        return OmegaTensor(self.data + other.data)

    def __sub__(self, other):
        return OmegaTensor(self.data - other.data)

    def __mul__(self, other):
        return OmegaTensor(self.data * other.data)

    def __truediv__(self, other):
        return OmegaTensor(self.data / other.data)

    @property
    def shape(self):
        return self.data.shape

    @property
    def T(self):
        return OmegaTensor(self.data.T)

    def dot(self, other):
        return OmegaTensor(self.data.dot(other.data))

    def sum(self, axis=None):
        return OmegaTensor(self.data.sum(axis=axis))

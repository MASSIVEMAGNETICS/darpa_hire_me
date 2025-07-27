import numpy as np
from .omega_tensor import OmegaTensor

class QuantumParameterState:
    """Represents a parameter as a probabilistic distribution."""

    def __init__(self, mean, std_dev):
        self.mean = OmegaTensor(mean)
        self.std_dev = OmegaTensor(std_dev)

    def sample(self):
        """Samples from the distribution to get a concrete value."""
        return OmegaTensor(np.random.normal(self.mean.data, self.std_dev.data))

class QuantumOmegaTensor(OmegaTensor):
    """An OmegaTensor with quantum properties."""

    def __init__(self, data):
        super().__init__(data)
        self.state = QuantumParameterState(data, np.ones_like(data) * 0.1)

    def __repr__(self):
        return f"QuantumOmegaTensor({self.state})"

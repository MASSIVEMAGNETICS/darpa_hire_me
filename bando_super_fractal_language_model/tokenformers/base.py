from abc import ABC, abstractmethod

class Tokenformer(ABC):
    """Abstract base class for all tokenformers."""

    @abstractmethod
    def process(self, input_data):
        """Processes the input data and returns a representation."""
        pass

from .base import Tokenformer

class SymbolicTokenformer(Tokenformer):
    """Processes structured, symbolic data."""

    def process(self, input_data):
        print("Processing with SymbolicTokenformer")
        return input_data

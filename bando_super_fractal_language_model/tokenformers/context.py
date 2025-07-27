from .base import Tokenformer

class ContextTokenformer(Tokenformer):
    """Interfaces directly with the BandoFractalMemory."""

    def process(self, input_data):
        print("Processing with ContextTokenformer")
        return input_data

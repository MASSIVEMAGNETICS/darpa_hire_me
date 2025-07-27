from .base import Tokenformer

class PredictiveTokenformer(Tokenformer):
    """Generates speculative predictions about future tokens."""

    def process(self, input_data):
        print("Processing with PredictiveTokenformer")
        return input_data

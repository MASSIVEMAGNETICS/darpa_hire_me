from .base import Tokenformer

class SemanticTokenformer(Tokenformer):
    """The primary language comprehender."""

    def process(self, input_data):
        print("Processing with SemanticTokenformer")
        return input_data

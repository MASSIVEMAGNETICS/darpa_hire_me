from .base import Tokenformer

class EmotionTokenformer(Tokenformer):
    """Identifies and quantifies emotional content."""

    def process(self, input_data):
        print("Processing with EmotionTokenformer")
        return input_data

from .semantic import SemanticTokenformer
from .emotion import EmotionTokenformer
from .symbolic import SymbolicTokenformer
from .predictive import PredictiveTokenformer
from .context import ContextTokenformer

class TokenformerManager:
    """Manages the tokenformer ecosystem."""

    def __init__(self):
        self.tokenformers = {
            "semantic": SemanticTokenformer(),
            "emotion": EmotionTokenformer(),
            "symbolic": SymbolicTokenformer(),
            "predictive": PredictiveTokenformer(),
            "context": ContextTokenformer(),
        }

    def process(self, input_data):
        """Processes input data with all tokenformers and fuses the outputs."""
        outputs = []
        for name, tokenformer in self.tokenformers.items():
            outputs.append(tokenformer.process(input_data))

        # For now, just return the list of outputs.
        # In the future, this will involve a more sophisticated fusion process.
        return outputs

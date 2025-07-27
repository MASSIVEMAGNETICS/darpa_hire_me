from .tokenformers.manager import TokenformerManager
from .core.flower_of_life import FractalFlowerOfLife

class BandoSuperFractalLanguageModel:
    """The main language model class."""

    def __init__(self):
        self.tokenformer_manager = TokenformerManager()
        self.fractal_core = FractalFlowerOfLife()

    def process(self, input_data):
        """The main processing loop of the model."""
        fused_output = self.tokenformer_manager.process(input_data)
        final_output = self.fractal_core.process(fused_output)
        return final_output

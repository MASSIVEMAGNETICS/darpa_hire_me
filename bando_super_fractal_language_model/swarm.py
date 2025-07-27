from .model import BandoSuperFractalLanguageModel

class SwarmManager:
    """Manages a swarm of BandoSuperFractalLanguageModel instances."""

    def __init__(self, num_instances):
        self.instances = [BandoSuperFractalLanguageModel() for _ in range(num_instances)]

    def process(self, input_data):
        """Processes input data across all instances in the swarm."""
        outputs = []
        for instance in self.instances:
            outputs.append(instance.process(input_data))
        return outputs

from .node import FractalNode

class FractalFlowerOfLife:
    """The central processing unit of the model."""

    def __init__(self):
        self.nodes = self._create_nodes()

    def _create_nodes(self):
        """Creates the 37 nodes of the Flower of Life."""
        nodes = {}
        # Create central node
        nodes[0] = FractalNode(0, list(range(1, 7)))

        # Create inner ring
        for i in range(1, 7):
            connections = [0, (i % 6) + 1, ((i - 2) % 6) + 1]
            connections.extend(list(range(7, 37))) # Connect to all outer nodes
            nodes[i] = FractalNode(i, connections)

        # Create outer ring
        for i in range(7, 37):
            # Each outer node is connected to 3 inner nodes
            # This is a simplified connection scheme for now
            inner_connections = [(i % 6) + 1, ((i + 1) % 6) + 1, ((i + 2) % 6) + 1]
            nodes[i] = FractalNode(i, inner_connections)

        return nodes

    def process(self, fused_input):
        """Processes the fused input from the tokenformers."""
        # For now, just pass the input to the central node.
        # A more complex information flow will be implemented later.
        return self.nodes[0].process(fused_input)

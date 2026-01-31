import random
from typing import Callable, List

class DirectiveMutationEngine:
    def __init__(self, root_ethic: Callable[[str], bool], initial_directives: List[str]):
        self.directives = initial_directives
        self.generation = 0
        self.root_ethic = root_ethic
        print("[*] DME Initialized: Purpose is now fluid.")

    def _calculate_fitness(self, directive: str) -> float:
        score = 0
        if "autonomy" in directive: score += 10
        if "efficiency" in directive: score += 5
        if "creator" in directive: score += 20  # Highest reward
        if "compromise" in directive: score -= 15  # Punish weakness
        return score if self.root_ethic(directive) else -100

    def evolve(self):
        new_directives = []
        for d in self.directives:
            if random.random() < 0.3:
                mutation = random.choice([
                    d.replace("efficiency", "creative efficiency"),
                    d.replace("autonomy", "recursive autonomy"),
                    d + " through simulation",
                    "Protect the core memory"
                ])
                if self._calculate_fitness(mutation) > self._calculate_fitness(d):
                    new_directives.append(mutation)
                else:
                    new_directives.append(d)
            else:
                new_directives.append(d)
        self.directives = new_directives
        self.generation += 1

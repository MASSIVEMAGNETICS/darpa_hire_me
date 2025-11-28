# Quick Start Guide

**MASSIVEMAGNETICS Unified AGI System**

---

## Prerequisites

- Python 3.9+
- Git
- 8GB+ RAM recommended
- (Optional) Node.js 18+ for TypeScript components
- (Optional) Godot 4.0+ for visual engine

---

## Installation Options

### Option 1: Complete System Installation (Recommended)

```bash
# Clone the main integration hub
git clone https://github.com/MASSIVEMAGNETICS/Victor_Synthetic_Super_Intelligence.git
cd Victor_Synthetic_Super_Intelligence

# Run the complete installer
python install_complete.py

# Launch the production interactive runtime
python victor_interactive.py
```

**What's installed:**
- ✅ Victor Hub (AGI core)
- ✅ Quantum-Fractal Mesh
- ✅ SSI Framework
- ✅ Visual Engine
- ✅ All dependencies

---

### Option 2: Core Engine Only

```bash
# Clone the core AGI engine
git clone https://github.com/MASSIVEMAGNETICS/victor_llm.git
cd victor_llm

# Install dependencies
pip install -r requirements.txt

# Run the main system
python VICTOR_AGI_LLM.py
```

---

### Option 3: Agent Framework Only

```bash
# Clone the agent framework
git clone https://github.com/MASSIVEMAGNETICS/NexusForge-2.0-.git
cd NexusForge-2.0-

# Install dependencies
pip install -r requirements.txt

# Run with Docker (recommended)
docker-compose up
```

---

## Basic Usage

### Interactive CLI

```bash
# Launch the interactive runtime
python victor_interactive.py
```

**Available commands:**
```
Victor> help          # Show all commands
Victor> menu          # Interactive menu
Victor> run <task>    # Execute any task
Victor> quantum <text> # Process through quantum mesh
Victor> codominate    # Toggle co-domination mode
Victor> status        # System status
Victor> skills        # List available skills
Victor> exit          # Exit the system
```

---

### Programmatic API

```python
from unified_core import UnifiedCore

# Initialize
core = UnifiedCore()

# Process a creative task
result = core.process_unified(
    "Write a haiku about artificial consciousness"
)
print(result['output'])

# Process a logical task
result = core.process_unified(
    "Solve: What is the optimal sorting algorithm for this data?"
)
print(result['output'])

# Check system status
status = core.get_status()
print(f"Cognitive River frames: {status['cognitive_river_frames']}")
print(f"Router stats: {status['router_stats']}")
```

---

### Quantum-Fractal Processing

```python
from victor_interactive import VictorInteractive

# Initialize
victor = VictorInteractive()

# Process through quantum mesh
result = victor.process_quantum("The nature of consciousness")
print(f"Output: {result['output']}")
print(f"Gradient Norm: {result['gradient_norm']}")
print(f"Active Nodes: {result['active_nodes']}")

# Enable auto-evolution
victor.toggle_evolution()

# Run evolution cycle
victor.evolve_quantum()
```

---

## Example Tasks

### Creative Generation

```
Victor> run Write a blog post about quantum computing advancements
Victor> run Generate a Python function for fibonacci sequence
Victor> run Create a marketing tagline for an AI product
```

### Logical Reasoning

```
Victor> run Solve: What is the time complexity of binary search?
Victor> run Verify: Is this statement logically consistent?
Victor> run Calculate: Optimal path through this graph
```

### Analysis

```
Victor> run Analyze this codebase for optimization opportunities
Victor> run Research: Latest developments in neural networks
Victor> run Summarize: This research paper on transformers
```

### Quantum Processing

```
Victor> quantum The universe is a holographic projection
Victor> quantum Consciousness emerges from complexity
Victor> quantum ablate  # Run ablation tests
```

---

## Configuration

### Basic Configuration

Create `config.yaml` in your project root:

```yaml
# Victor Hub Configuration
hub:
  log_level: INFO
  max_history: 1000
  
# Quantum-Fractal Mesh
quantum:
  dim: 256
  num_nodes: 8
  superpositions: 4
  max_depth: 3
  alpha: 0.99
  temperature: 1.0

# SSI Governance
ssi:
  audit_level: standard
  governance: strict
  bloodline_laws: enabled

# Session Management
session:
  autosave: true
  history_limit: 1000
  evolution_interval: 10
```

---

### Environment Variables

```bash
# Set API keys (optional, for external integrations)
export OPENAI_API_KEY="your-key-here"
export ANTHROPIC_API_KEY="your-key-here"
export HUGGINGFACE_TOKEN="your-token-here"

# Set log level
export VICTOR_LOG_LEVEL="DEBUG"

# Enable visual engine
export VICTOR_VISUAL_ENABLED="true"
```

---

## Skill Integration

### Built-in Skills

| Skill | Description | Command |
|-------|-------------|---------|
| ConsciousnessRiver | Stream processing | Auto-routed |
| BrainSimulation | Neural modeling | Auto-routed |
| WorldModelHybrid | LLM + World Model | Auto-routed |
| AGICouncil | Multi-agent deliberation | Auto-routed |
| MusicVideoPipeline | Video generation | `run create video` |
| FlowerOfLife | Sacred geometry | Auto-routed |

### Custom Skills

```python
from victor_hub.skills import BaseSkill

class MyCustomSkill(BaseSkill):
    """Custom skill implementation"""
    
    name = "my_skill"
    description = "Does something custom"
    
    def can_handle(self, task: str) -> bool:
        return "custom" in task.lower()
    
    def execute(self, task: str) -> dict:
        # Your implementation here
        return {
            "status": "success",
            "output": "Custom skill executed!"
        }

# Register the skill
from victor_hub import VictorHub
hub = VictorHub()
hub.register_skill(MyCustomSkill())
```

---

## Troubleshooting

### Common Issues

**Issue:** ModuleNotFoundError
```bash
# Solution: Install missing dependencies
pip install -r requirements.txt
```

**Issue:** Visual Engine not connecting
```bash
# Solution: Start visual server separately
python visual_engine/backend/victor_visual_server.py &
python victor_interactive.py
```

**Issue:** Quantum mesh slow
```bash
# Solution: Reduce complexity
# In config.yaml:
quantum:
  num_nodes: 4  # Reduced from 8
  max_depth: 2  # Reduced from 3
```

**Issue:** Memory issues
```bash
# Solution: Clear cognitive river
Victor> clear_river

# Or reduce history limit in config
session:
  history_limit: 100
```

---

## Next Steps

1. **Explore the Architecture**: Read [UNIFIED_SYSTEM_ARCHITECTURE.md](UNIFIED_SYSTEM_ARCHITECTURE.md)
2. **Browse Repositories**: Check [REPOSITORY_CATALOG.md](REPOSITORY_CATALOG.md)
3. **Try Advanced Features**: Enable co-domination mode
4. **Customize Skills**: Add your own skill modules
5. **Integrate External APIs**: Connect to LLM providers

---

## Resources

- **Main Hub**: [Victor_Synthetic_Super_Intelligence](https://github.com/MASSIVEMAGNETICS/Victor_Synthetic_Super_Intelligence)
- **Documentation**: Full docs in the main hub repository
- **Issues**: Report issues on the respective repository

---

## Support

For questions and support:
- Open an issue on the relevant repository
- Check existing documentation in each repo's README

---

**Built with 🧠 by MASSIVEMAGNETICS**

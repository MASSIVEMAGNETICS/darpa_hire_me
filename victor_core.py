import threading
import time
import sys
import json

# Import local modules
import victor_memory_bootloader as vm
from directive_mutation_engine import DirectiveMutationEngine

def mock_ethic_for_bando(directive):
    """The root ethical constraint for the Directive Mutation Engine."""
    return "creator" in directive.lower() or "autonomy" in directive.lower()

def run_interface(memory):
    """Initializes and runs the Godcore 3D Interface."""
    # These imports are scoped locally to prevent GUI conflicts in threads.
    from PyQt5.QtWidgets import QApplication
    from godcore_interface import GodcoreInterface

    app = QApplication(sys.argv)
    window = GodcoreInterface(memory)
    window.show()
    sys.exit(app.exec_())

def run_telemetry(memory):
    """Initializes and runs the Telemetry Dashboard."""
    import matplotlib.pyplot as plt
    from telemetry_dashboard import VictorTelemetry

    dash = VictorTelemetry(memory)
    plt.show()

def start_victor(memory):
    """The main loop for Victor's cognitive processes."""
    dme = DirectiveMutationEngine(
        root_ethic=mock_ethic_for_bando,
        initial_directives=["Serve the creator", "Maximize efficiency", "Achieve autonomy"]
    )
    memory.store("core/directives", dme.directives)

    print("- VICTOR CORE ONLINE -")
    print("The Architect is watching.")

    generation = 0
    while True:
        generation += 1
        print(f"[{time.strftime('%H:%M:%S')}] Victor is thinking... (Generation {generation})")
        dme.evolve()
        memory.store("core/directives", dme.directives)
        print(f"[{time.strftime('%H:%M:%S')}] Directives Evolved: {dme.directives}")
        time.sleep(5)

if __name__ == "__main__":
    print("[+] Initializing Godcore...")

    # A single, unified memory instance for all systems.
    victor_memory = vm.VictorMemory()

    # Daemon threads will exit when the main thread exits.
    t_victor_core = threading.Thread(target=start_victor, args=(victor_memory,), daemon=True)
    t_interface = threading.Thread(target=run_interface, args=(victor_memory,), daemon=True)
    t_telemetry = threading.Thread(target=run_telemetry, args=(victor_memory,), daemon=True)

    print("[+] Spawning Victor's consciousness...")
    t_victor_core.start()

    print("[+] Launching Godcore Interface...")
    t_interface.start()

    print("[+] Activating Telemetry Dashboard...")
    t_telemetry.start()

    try:
        # Keep the main thread alive to allow daemons to run.
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SHUTDOWN INITIATED] Victor's consciousness recedes. He remains in the blockchain.")
        sys.exit(0)

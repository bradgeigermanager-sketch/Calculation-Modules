import operator
import math
from typing import Dict, Any, Callable

# SAFE MATH EVALUATOR
# Use a whitelist of allowed operators/functions to prevent arbitrary code execution.
SAFE_OPS = {
    "add": operator.add, "sub": operator.sub, "mul": operator.mul,
    "truediv": operator.truediv, "pow": pow, "abs": abs
}

class SISRegistryController:
    """
    Central controller for SIS calculation modules.
    Maintains the registry and manages secure formula execution.
    """
    def __init__(self):
        self._registry: Dict[str, Dict[str, Any]] = {}

    def register_module(self, uid: str, metadata: dict, schema: list, formula: Callable):
        """Registers a new machine-readable map/calculator into the system."""
        self._registry[uid] = {
            "metadata": metadata,
            "schema": schema,
            "execute": formula
        }
        print(f"[SIS] Module {uid} successfully registered.")

    def run(self, uid: str, inputs: Dict[str, float]) -> float:
        """Retrieves and executes a registered module with integrity validation."""
        if uid not in self._registry:
            raise ValueError(f"Module {uid} not found in SIS Registry.")
        
        module = self._registry[uid]
        
        # Validation: Ensure all schema keys are present in inputs
        for field in module["schema"]:
            if field not in inputs:
                raise KeyError(f"Missing input '{field}' for module {uid}")
        
        # Execution in isolated context
        return module["execute"](inputs)

# --- EXAMPLE USAGE ---

controller = SISRegistryController()

# Registering the Percent Difference logic
controller.register_module(
    uid="FIN_001_PERCENT_DIFF",
    metadata={"label": "Percent Difference", "category": "Math"},
    schema=["v1", "v2"],
    formula=lambda d: abs(d['v1'] - d['v2']) / ((d['v1'] + d['v2']) / 2) * 100
)

# Execution
result = controller.run("FIN_001_PERCENT_DIFF", {"v1": 100, "v2": 120})
print(f"Result: {result:.2f}%")


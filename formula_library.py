"""
FILE: formula_library.py
PURPOSE: Pure logic registry for SIS modules.
NOTATION: All functions accept a dictionary of inputs and return a deterministic value.
"""
import math

# --- Math Domain ---
def fin_percent_difference(d: dict) -> float:
    """Calculates percent difference between two values."""
    return abs(d['v1'] - d['v2']) / ((d['v1'] + d['v2']) / 2) * 100

# --- Physics Domain ---
def phys_kinetic_energy(d: dict) -> float:
    """Calculates kinetic energy: 0.5 * m * v^2"""
    return 0.5 * d['mass'] * math.pow(d['velocity'], 2)

# --- Finance Domain ---
def fin_compound_interest(d: dict) -> float:
    """Calculates future value: P * (1 + r/n)^(nt)"""
    return d['principal'] * math.pow(
        (1 + (d['rate'] / d['compounds'])), 
        (d['compounds'] * d['time'])
    )

# --- Logic Registry Map ---
# This dictionary binds the manifest 'formula_ref' to the executable function
FORMULA_REGISTRY = {
    "FIN_001_LOGIC": fin_percent_difference,
    "PHYS_001_LOGIC": phys_kinetic_energy,
    "FIN_002_LOGIC": fin_compound_interest
}


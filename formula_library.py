"""
FILE: formula_library.py
PURPOSE: Pure logic registry with automated registration.
NOTATION: All functions accept a dictionary of inputs and return a deterministic value.


"""
import math
import statistics

# The core registry
FORMULA_REGISTRY = {}

def register_sis_formula(uid: str):
    """Decorator to automatically add functions to the SIS registry."""
    def decorator(func):
        FORMULA_REGISTRY[uid] = func
        return func
    return decorator

# --- AUTOMATED MODULE DEFINITIONS ---

@register_sis_formula("FIN_001_LOGIC")
def fin_percent_difference(d: dict) -> float:
    return abs(d['v1'] - d['v2']) / ((d['v1'] + d['v2']) / 2) * 100

@register_sis_formula("STAT_DESC_LOGIC")
def stats_descriptive(d: dict) -> dict:
    """Calculates descriptive stats from a list 'data'."""
    data = d['data']
    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "stdev": statistics.stdev(data) if len(data) > 1 else 0
    }

@register_sis_formula("STAT_OUTLIER_LOGIC")
def stats_outlier_detection(d: dict) -> dict:
    """Calculates fences for anomaly detection: Q1 - 1.5*IQR and Q3 + 1.5*IQR."""
    data = sorted(d['data'])
    q1, q3 = statistics.quantiles(data, n=4)[0], statistics.quantiles(data, n=4)[2]
    iqr = q3 - q1
    return {"lower_fence": q1 - 1.5 * iqr, "upper_fence": q3 + 1.5 * iqr}

@register_sis_formula("PHYS_KINETIC_LOGIC")
def phys_kinetic_energy(d: dict) -> float:
    """Calculates kinetic energy: 0.5 * m * v^2"""
    return 0.5 * d['mass'] * math.pow(d['velocity'], 2)

@register_sis_formula("FIN_COMPINT_LOGIC")
def fin_compound_interest(d: dict) -> float:
    """Calculates future value: P * (1 + r/n)^(nt)"""
    return d['principal'] * math.pow(
        (1 + (d['rate'] / d['compounds'])), 
        (d['compounds'] * d['time'])
    )

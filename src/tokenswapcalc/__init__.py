"""TokenSwapCalc: Estimates token swap rates and slippage for a given input amount."""

__version__ = "1.0.0"

from .core import run
from .cli import main

__all__ = ["main", "run", "__version__"]
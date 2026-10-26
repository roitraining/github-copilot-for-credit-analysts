import sys

import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import sklearn
import pytest

print(f"Python version: {sys.version.split()[0]}")
for name, module in [
    ("pandas", pd),
    ("numpy", np),
    ("matplotlib", matplotlib),
    ("seaborn", sns),
    ("sklearn", sklearn),
    ("pytest", pytest),
]:
    print(f"{name} version: {getattr(module, '__version__', 'unknown')}")

accounts = pd.DataFrame(
    {
        "account_id": [101, 102, 103],
        "balance": [1200.50, 2450.00, 980.75],
    }
)
print(f"Mean balance: {accounts['balance'].mean()}")
print("SUCCESS: Python environment is ready for the course labs!")

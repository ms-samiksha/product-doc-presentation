# 23f3001448@ds.study.iitm.ac.in
# Marimo Notebook: Interactive Data Analysis
# This notebook demonstrates variable dependencies and interactive widgets.

import marimo as mo

# --- Cell 1: Define dataset variable ---
# Data flows from here into dependent cells.
data = [10, 20, 30, 40, 50]


# --- Cell 2: Slider widget controlling scale ---
slider = mo.ui.slider(start=1, end=10, value=5)

# --- Cell 3: Derived variable depending on slider and data ---
scaled_data = [x * slider.value for x in data]


# --- Cell 4: Dynamic markdown showing slider + results ---
mo.md(
    f"""
### 📊 Interactive Scaling Demo  
Slider value: **{slider.value}**

Scaled data:  
**{scaled_data}**
"""
)

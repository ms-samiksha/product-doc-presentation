---
marp: true
title: Product Documentation Presentation
author: 23f3001448@ds.study.iitm.ac.in
theme: default
paginate: true
_paginate: true
---

<style>
/* === Custom Theme Styling === */
section {
  font-family: "Segoe UI", sans-serif;
  color: #222;
}

h1, h2, h3 {
  color: #0066cc;
}

strong {
  color: #cc0066;
}

footer {
  color: #777;
  font-size: 14px;
  text-align: right;
}
</style>

<!-- _header: **Product Documentation – Internal Use** -->
<!-- _footer: **23f3001448@ds.study.iitm.ac.in** -->

# 🧩 Product Documentation Overview

Welcome to the documentation ecosystem.  
Clear. Maintainable. Version-controlled.  
Built with **Marp** for maximum portability.

---

<!-- _class: lead -->
<!-- _backgroundColor: #eef6ff -->

# Why Marp?

- Write once → export to HTML, PDF, PPTX  
- Perfect for teams using Git & GitHub  
- Markdown-friendly for engineers  
- Customizable themes & components  

---

<!-- Slide with background image -->
![bg cover](images/background.jpg)

# Platform Architecture  
*This slide uses a full-cover background image.*

Documentation powered by:  
- Markdown  
- Marp CLI  
- Version control workflows  

---

# Custom Styling Example

<!-- _backgroundColor: #ffffff -->
<!-- _color: #003366 -->
<!-- _class: section-style -->

This slide demonstrates how Marp directives  
can change **color**, **layout**, and **tone**.

---

# Algorithmic Complexity

Inline math:  
The time complexity of binary search is  
$O(\log n)$.

Block math:  

$$
T(n) = T\left(\frac{n}{2}\right) + O(1)
$$

Which solves to:  
$$
T(n) = O(\log n)
$$

---

# Example Code Block

```python
def search(arr, key):
    for i, val in enumerate(arr):
        if val == key:
            return i
    return -1

# -*- coding: utf-8 -*-
r"""
Seaborn example
===============

This example demonstrates a Seaborn plot. Figures produced Matplotlib **and**
by any package that is based on Matplotlib (e.g., Seaborn), will be
"""
# Author: Michael Waskom & Lucy Liu
# License: BSD 3 clause

import pyvista as pv


p = pv.Plotter()
arrow = pv.Arrow()
p.add_mesh(arrow)
p.show()

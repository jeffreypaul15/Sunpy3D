import functools

import numpy as np
import pyvista as pv

from astropy.constants import R_sun

from sunpy.coordinates import HeliocentricInertial
from sunpy.map.maputils import all_corner_coords_from_map
from dq import draw_quadrangle, draw_rectangles
import quadrangle


__all__ = ['PyVistaPlotter']


class PyVistaPlotter:
    """
    A plotter for 3D data.
    Since pyvista is not coordinate aware, all coordinates are converted to
    a specific frame (`~sunpy.coordinates.HeliocentricInertial` by default),
    and distance units are such that :math:`R_{sun} = 1`.
    Parameters
    ----------
    coordinate_frame : astropy.coordinates.BaseFrame
        Coordinate frame of the plot. The x, y, z axes of the pyvista plotter
        will be the x, y, z axes in this coordinate system.
    """
    def __init__(self, coordinate_frame=None):
        self._plotter = pv.Plotter()
        self.draw = Draw(coordinate_frame)

    @property
    def plotter(self):
        """
        `pyvista.Plotter`.
        """
        return self._plotter

    @functools.wraps(pv.Plotter.show)
    def show(self, *args, **kwargs):
        """
        Show the plot.
        """
        self.plotter.show(*args, **kwargs)

    def _pyvista_mesh(self, m):
        """
        Create a mesh from a map.
        Parameters
        ----------
        m : sunpy.map.Map
        Returns
        -------
        pyvista.StructuredGrid
        """
        nodes = self.draw.create_map(m)
        grid = pv.StructuredGrid()
        grid.points = nodes
        print(grid.points)
        grid.dimensions = [m.data.shape[0] + 1,
                           m.data.shape[1] + 1,
                           1]
        data = m.data.T.reshape(-1)
        grid['data'] = m.plot_settings['norm'](data)
        return grid

    def plot_map(self, m, **kwargs):
        """
        Plot a map.
        Parameters
        ----------
        m : sunpy.map.Map
            Map to be plotted.
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        """
        cmap = kwargs.pop('cmap', m.cmap)
        mesh = self._pyvista_mesh(m)
        self.plotter.add_mesh(mesh, cmap=cmap, **kwargs)
        return mesh

    def plot_quadrangle(self, m, **kwargs):
        """
        Plot a quadrangle on the map from the given map
        """
        bottom_left = SkyCoord(40*u.deg, -45*u.deg, frame='heliographic_stonyhurst', obstime=m.date)
        coords = self.draw.draw_quadrangle(m, bottom_left, width=10*u.deg, height=90*u.deg)
        coords -= 0.001
        mesh = pv.StructuredGrid(coords[:, 0], coords[:, 1], coords[:, 2])
        self.plotter.add_mesh(mesh, color='lightblue', line_width=2.0)
        return mesh

    def plot_line(self, coords, **kwargs):
        """
        Plot a line from a set of coordinates.
        Parameters
        ----------
        coords : astropy.coordinates.SkyCoord
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        Notes
        -----
        This plots a `pyvista.Spline` object.
        """
        points = self._coords_to_xyz(coords)
        spline = pv.Spline(points)
        self.plotter.add_mesh(spline, **kwargs)
        return spline

    def plot_solar_axis(self, length=2.5, arrow_kwargs={}, **kwargs):
        """
        Plot the solar rotation axis as an arrow.
        Parameters
        ----------
        length : float
            Length of the arrow in multiples of solar radii.
        arrow_kwargs : dict
            Keyword arguments to be handed to `pyvista.Arrow`.
            ``start``, ``direction``, and ``scale`` cannot be manually
            specified, as they are automatically set.
        **kwargs :
            Keyword arguments are handed to `pyvista.Plotter.add_mesh`.
        """
        defaults = {'shaft_radius': 0.01,
                    'tip_length': 0.05,
                    'tip_radius': 0.02}
        defaults.update(arrow_kwargs)
        arrow = pv.Arrow(start=(0, 0, -length / 2),
                         direction=(0, 0, length),
                         scale='auto',
                         **defaults)
        self.plotter.add_mesh(arrow, **kwargs)
        return arrow
        
        
"""
=======================
Three dimensional plots
=======================
sunpy can interface with the `pyvista` package to produce interactive 3D plots.
"""
###############################################################################
# Start by importing the required modules
import astropy.constants as const
import astropy.units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
from sunpy.data.sample import AIA_193_IMAGE
from sunpy.map import Map
from quadrangle import Draw

m = Map(AIA_193_IMAGE)
m.plot()
plotter = PyVistaPlotter()
map_mesh = plotter.plot_map(m)
line_mesh = plotter.plot_solar_axis()
quad_mesh = plotter.plot_quadrangle(m)
# combined_mesh = map_mesh + quad_mesh

blocks = pv.MultiBlock([line_mesh])
merged = blocks.combine()
# merged
pv.save_meshio('/home/jeffrey/jupy/tmp.vtk', merged)
plotter = pv.Plotter()
plotter.add_mesh(merged)
plotter.show()
# plotter.show(cpos=(-100,0,0), screenshot="quad.png")

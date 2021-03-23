from datetime import datetime
import os

import astropy.constants as const
import astropy.units as u
from astropy.coordinates import SkyCoord
import matplotlib.pyplot as plt
import numpy as np
import sunpy.map
import sunpy.io.fits

import pfsspy
import pfsspy.tracing as tracing
from pfsspy.sample_data import get_gong_map

import functools

import numpy as np
import pyvista as pv

from astropy.constants import R_sun

from sunpy.coordinates import HeliocentricInertial
from sunpy.map.maputils import all_corner_coords_from_map




class Pfss3D:
    def __init__(self, nrho, rss, gong_map = sunpy.map.Map(get_gong_map())):
        self._nrho = nrho
        self._rss = rss
        self.gong_map = gong_map
        self.input = pfsspy.Input(self.gong_map, self.nrho, self.rss)
        self._output = pfsspy.pfss(self.input)
        self.tracer = tracing.PythonTracer()
    
    @property
    def nrho(self):
        return self._nrho
    
    @property
    def rss(self):
        return self._rss

    @property
    def output(self):
        return self._output

    def calculate_lon_lat(self):
        r = 1.2 * const.R_sun
        lat = np.linspace(-np.pi / 2, np.pi / 2, 8, endpoint=False)
        lon = np.linspace(0, 2 * np.pi, 8, endpoint=False)
        lat, lon = np.meshgrid(lat, lon, indexing='ij')
        lat, lon = lat.ravel() * u.rad, lon.ravel() * u.rad
        return lat, lon, r

    def create_field_lines(self, lat, lon, r):
        seeds = SkyCoord(lon, lat, r, frame=self.output.coordinate_frame)
        field_lines = self.tracer.trace(seeds, self.output)
        return field_lines
    
    def get_colors(self, field_line):
        color = {0: 'black', -1: 'lightblue', 1: 'red'}.get(field_line.polarity)
        return color
    
    def plot(self, field_lines):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for field_line in field_lines:
            coords = field_line.coords
            coords.representation_type = 'cartesian'
            ax.plot(coords.x / const.R_sun,
                        coords.y / const.R_sun,
                        coords.z / const.R_sun,
                        color=color, linewidth=1)

        ax.set_title('PFSS solution')
        plt.show()


        



# nrho = 35
# rss = 2.5





# tracer = tracing.PythonTracer()


# r = 1.2 * const.R_sun
# lat = np.linspace(-np.pi / 2, np.pi / 2, 8, endpoint=False)
# lon = np.linspace(0, 2 * np.pi, 8, endpoint=False)
# lat, lon = np.meshgrid(lat, lon, indexing='ij')
# lat, lon = lat.ravel() * u.rad, lon.ravel() * u.rad

# seeds = SkyCoord(lon, lat, r, frame=output.coordinate_frame)

# field_lines = tracer.trace(seeds, output)

# for field_line in field_lines:
    
#     coords = field_line.coords
#     coords.representation_type = 'cartesian'
#     ax.plot(coords.x / const.R_sun,
#             coords.y / const.R_sun,
#             coords.z / const.R_sun,
#             color=color, linewidth=1)

# ax.set_title('PFSS solution')
# plt.show()
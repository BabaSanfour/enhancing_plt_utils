"""
color_maps.py

Author: Hamza Abdelhedi

Last Updated: December 2023

Tested on:
- Python 3.10.12
- Matplotlib 3.8.1

## Contents:

- `get_color_map()`: Returns a list of colors for a given color map name.
- `continuous_color_map()`: Returns a continuous color map for a given color map name.

---

This utility script provides convenient function for getting color maps.
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

spring = ['#0d0887', '#0000ff', '#0055d4', '#0080bf', '#00aaaa', '#00d495', '#7ff240', '#b6ff32', '#ffffff']

autumn = ['#ffffff', '#fff6cb', '#ffe0b2', '#ff8932', '#ff6532', '#df5050', '#d80404', '#bb0202', '#990000']

pink_floyd = spring + autumn
pink_floyd.remove("#ffffff")

green_bull = [
    '#004529',
    '#0c713b',
    '#379e54',
    '#5da04b',
    '#7ecb6e',
    '#a6d96a',
    '#b2df8a',
    '#bfe5a0',
    '#e0f3b2',
    '#f7fcbe',
    '#ffffcc',
    '#ffffff',
]

grey =  ['#f7f7f7', "#dddddd", '#999999']

the_blues = [
    '#00205b',
    '#003480',
    '#00489e',
    '#005fbf',
    '#0077e3',
    '#3498db',
    '#5fa3e3',
    '#85b8f2',
    '#aad3ff',
    '#d6e7ff',
    '#e6f2ff',
    '#ffffff',
]

oppenheimer = [
    '#9c179e',
    '#b01eaa',
    '#c025b6',
    '#d12cc2',
    '#e377c2',
    '#f781bf',
    '#ffaaaa',
    '#ffc0cb',  
    '#ffcccc',  
    '#ffd9e6',  
    '#fff5f0',
    '#ffffff',
    
]

pink_ocean = the_blues + list(reversed(oppenheimer))
pink_floyd.remove("#ffffff")

one_piece = [
    '#0000ff', # Blue
    '#00aaaa', # Cyan
    '#d80404', # Red
    '#ff8932', # Orange
    '#aad3ff', # Light blue
    '#df2179', # Pink
    '#ffccd3', # Light pink
    '#ffd700',  # Gold
    '#ffff00',  # Yellow
    '#8a2be2',  # Blue Violet
    '#ff00ff',  # Fuchsia
    '#8B4513',  # Saddle Brown
    '#006400',  # Dark Green
    '#FF00FF',  # Magenta
    '#D2691E',  # Chocolate
]

color_maps = {
    'spring': spring,
    'autumn': autumn,
    'pink_floyd': pink_floyd,
    'green_bull': green_bull,
    'grey': grey,
    'the_blues': the_blues,
    'oppenheimer': oppenheimer,
    'pink_ocean': pink_ocean,
    'one_piece': one_piece,
}

def get_color_map(name):
    """
    Returns a list of colors for a given color map name.

    Args:
        - name (str): Name of the color map.

    Returns:
        - list: List of colors in the specified color map.
    """
    return color_maps[name]

def continuous_color_map(name, vmin=-1, vmax=1):
    """
    Returns a continuous color map for a given color map name.

    Args:
        - name (str): Name of the color map.
        - vmin (float): Minimum value of the color map. Default: -1
        - vmax (float): Maximum value of the color map. Default: 1

    Returns:
        - LinearSegmentedColormap: Continuous color map.
    """
    color_map = color_maps[name]
    if name in ["oppenheimer", "the_blues", "green_bull", "spring"]:
        color_map = list(reversed(color_map))
    
    new_cmap = np.array([plt.cm.colors.hex2color(color) for color in color_map])
    
    new_cmap = LinearSegmentedColormap.from_list(name, new_cmap)
    
    norm = plt.Normalize(vmin=vmin, vmax=vmax)
    
    new_cmap = plt.cm.ScalarMappable(cmap=new_cmap, norm=norm)
    
    return new_cmap
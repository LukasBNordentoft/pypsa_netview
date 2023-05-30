# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:12:47 2023

@author: lukas
"""

def circle_points(r, n):
    # From https://stackoverflow.com/questions/33510979/generator-of-evenly-spaced-points-in-a-circle-in-python
    import numpy as np
    
    circle_points = []
    for r, n in zip(r, n):
        t = np.linspace(0, 2*np.pi, n, endpoint=False)
        x = r * np.cos(t)
        y = r * np.sin(t)
        circle_points.append(np.c_[x, y])

    return circle_points


def set_positions(pos, n, spacing):
    import pandas as pd
    
    # ----- Set positions -----
    if pos == None or len(pos) != len(n.buses.index):
        #Determine if automatic position is used, or if positions are provided
        print('\nWARNING: draw_network():  No position given, or not sufficienct positions for the buses. Using automatic circular layout. \n')
        
        n_buses = len(n.buses.index)
        T = [n_buses]
        R = [n_buses * spacing]
    
        # Create positions in a circle
        pos = circle_points(R, T)
        s = pd.DataFrame(pos[0], columns = ['x', 'y'])
        s.index = n.buses.index
        
    else:
        print('\nINFO: draw_network(): bus positions given. spacing parameter has no effects. \n')
        s = pd.DataFrame(pos, columns = ['x', 'y'])
        s.index = n.buses.index
        
    return s
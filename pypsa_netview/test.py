# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:50:56 2023

@author: lukas
"""

import pypsa
from pypsa_netview import draw_network

#%% Set up pypsa network

# Create a new network
n = pypsa.Network('v_2030_base0_opt.nc')

n.links.p_min_pu['Island_to_Denmark'] = -1

#%% Draw pypsa network

draw_network(n, show_capacities = True)
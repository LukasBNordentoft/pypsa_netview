# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:04:54 2023

@author: lukas
"""

import pypsa
from pypsa_netview.pypsa_netview import draw_network

# Create an empty network
n = pypsa.Network()

# Add buses
n.add("Bus", "Bus0")
n.add("Bus", "Bus1")

# Add links
n.add("Link", "Link0", bus0="Bus0", bus1="Bus1", p_nom=20, p_min_pu=-1, p_max_pu=1)

# Set the load for Bus0
n.add("Load", "Load0", bus="Bus0", p_set=10)

# Set the generator for Bus1
n.add("Generator", "Generator0", bus="Bus1", p_nom=20, control="P")

# Set the snapshots
n.set_snapshots(range(5))

# Solve the network
# n.lopf()
# 
from pypsa_netview import draw_network

draw_network(n, show_capacities = True)


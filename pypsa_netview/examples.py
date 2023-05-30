# -*- coding: utf-8 -*-
"""
Created on Mon May 29 20:04:54 2023

@author: lukas
"""

import pypsa
from pypsa_netview import draw_network

#%% Two-bus network -----------------------------------------------------------

n = pypsa.Network()

# Add buses
n.madd('Bus',  ['Bus0', 'Bus1'])

# Add bidirectional link
n.add("Link", "Link0", bus0="Bus0", bus1="Bus1", p_nom=20, p_min_pu=-1,)

# Set the load for Bus0
n.add("Load", "Load0", bus="Bus0", p_set=10)

# Set the generator for Bus1
n.add("Generator", "Generator1", bus="Bus1", p_nom=20)

# Solve the network or not
n.lopf()

draw_network(n, 
             # filename = 'two_bus_example.pdf'
             )

#%% four bus network ----------------------------------------------------------
# Example case with four buses connected with unidirectional links

n = pypsa.Network()

# Add four buses
n.madd('Bus', 
       ['Bus0', 'Bus1', 'Bus2', 'Bus3'])

# Connect buses with links in a square
n.madd('Link',
       names = ['Link0', 'Link1', 'Link2', 'Link3'],
       bus0  = ['Bus0',  'Bus1',  'Bus2',  'Bus3'],
       bus1  = ['Bus3',  'Bus0',  'Bus1',  'Bus2'],
       p_nom_extendable = True,
       )

# Add generators to
n.madd('Generator',
       names = ['Bus0 Gen', 'Bus1 Gen'],
       bus   = ['Bus0',     'Bus1'],
       p_nom = 10,
       )

n.add('Load',
      'Bus2 load',
      bus = 'Bus2',
      p_set = 20)

n.lopf()

draw_network(n, spacing = 1, 
             show_capacities = True,
             filename = 'four_bus_exmaple.pdf')


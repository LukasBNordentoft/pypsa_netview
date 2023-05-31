import pypsa
from pypsa_netview.draw import draw_network

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
             filename = 'four_bus_example.pdf')
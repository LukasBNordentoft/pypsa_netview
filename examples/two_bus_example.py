import pypsa
from pypsa_netview.draw import draw_network

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
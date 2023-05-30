# PyPSA NetView - Visualize PyPSA networks
PyPSA NetView automatically creates a visual representation of a given PyPSA network, showing buses, components on buses and links between buses. This is intended to help understand the network that is being worked on. PyPSA NetView is not at all done, but feel free to look around anyways.

The files required to use PyPSA NetView are located in the pypsa_netview directory, and are
```python
pypsa_netview.py
helper_functions.py
custom_elements.py
```

PyPSA NetView is built on the ![Schemdraw package](https://github.com/RonSheely/schemdraw). By default, PyPSA NetView will create a circular layout with each bus being a point on a circle.  

Input parameters
------------
The following parameters can be passed to draw_network:

- ```show_capcities = True```: If the network has been solved, show capacities for bus components and links

- ```filename = 'yourdrawing.pdf' ```: A drawing can be saved as pdf by passing a filename.
 
- ```spacing ```: Increase or decrease distance betwene buses for automatically generated bus positions
  
Code example
------------

The following code produces the example drawing with two buses:
```python
import pypsa
from pypsa_netview import draw_network

n = pypsa.Network()

# Add buses, a bidirectional link, a load and a generator
n.madd('Bus',  ['Bus0', 'Bus1'])
n.add("Link", 'Link0', bus0 = 'Bus0', bus1 = 'Bus1', p_nom = 20, p_min_pu = -1,)
n.add("Load", 'Load0', bus = 'Bus0', p_set = 10)
n.add("Generator", 'Generator1', bus = 'Bus1', p_nom = 20)

# Solve the network (or not) and create visualization
n.lopf()
draw_network(n)
```

Dependencies
------------
- PyPSA 

- Schemdraw 

- Pandas 

- NumPy

Example drawings
------------
An exmaple of an unsolved two-bus network:

<img src="extra/two_bus_example.png" alt="Two bus network example" width="600">

An example of a solved four-bus network:

<img src="extra/four_bus_example.png" alt="Image Description" width="500">

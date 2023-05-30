# PyPSA NetView - Visualize PyPSA networks
PyPSA NetView automatically creates a visual representation of a given PyPSA network, showing buses, components on buses and links between buses. This is intended to help understand the network that is being worked on. 

The files required to use PyPSA NetView are located in the pypsa_netview directory, and are
```python
pypsa_netview.py
helper_functions.py
custom_elements.py
```

PyPSA NetView is built on the ![Schemdraw package][https://github.com/RonSheely/schemdraw]. A drawing of the network can be created such as:
```python
pypsa_netview.py
helper_functions.py
custom_elements.py
```

Dependencies
------------
- PyPSA 

- Schemdraw 

- Pandas 

## Exmaples
An exmaple of an unsolved two-bus network:

<img src="extra/two_bus_example.png" alt="Two bus network example" width="600">

An example of a solved four-bus network:

<img src="extra/four_bus_example.png" alt="Image Description" width="500">

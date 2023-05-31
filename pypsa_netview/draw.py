
from .helper_functions import set_positions
from .custom_elements import PyPSA_Gen, PyPSA_Load, PyPSA_Store
import schemdraw.elements as elm

def draw_component_on_bus(d, n, bus_components,
                          line_length = 1.5,
                          link_line_length = 0.75,
                          fontsize = 8,
                          bus_color = 'steelblue',
                          show_capacities = False,
                          ):
    # bus_components must be a dataframe from PyPSA, such as n.generators.
    
    # Determine type
    component_type = bus_components.index.name
    
    for component in bus_components.index:
        # Loop through component type on this bus, and add new line segment
        # and icon. Add label to icon.
        
        # Start
        d += elm.Line().color(bus_color).length(line_length) #Add line piece
        d.push() # Save position
        
        # Add labels if activated
        if show_capacities:
            
            # If component is generator, get p_nom_opt
            if component_type == 'Generator':
                value_string = f'\n \n p: {round(n.generators.loc[component].p_nom_opt, 2)}'
           
            # If component is store, get e_nom_opt
            elif component_type == 'Store':
                value_string = f'\n \n e: {round(n.stores.loc[component].e_nom_opt, 2)}'
            
            # If component is load, get mean load value
            elif component_type == 'Load':
                value_string = f'\n \n mean: {round(n.loads_t.p[component].mean(), 2)}'
            
            
        # Add capacities to label if show_capacities is True
        label_addition = value_string if show_capacities else ''
            
        # Create label
        label = (component.replace(' ', ' \n') 
                  + label_addition
                 )
        
        # Add icon with label depending on component type
        if component_type == 'Generator':
            d += PyPSA_Gen().up().label(label, loc='right', fontsize = fontsize)
        
        elif component_type == 'Store':
            d += PyPSA_Store().up().label(label, loc = 'right', fontsize = fontsize)
            
        elif component_type == 'Load':
            d += PyPSA_Load().right().label(label, loc='top', fontsize = fontsize)
        
        d.pop()  # Return to saved position
        
        return n

def draw_network(n, spacing = 2, 
                 line_length = 1.5, link_line_length = 0.75, 
                 headwidth = 0.45, headlength = 0.75,
                 fontsize = 8, title_fontsize = 12,
                 bus_color = 'steelblue', 
                 component_color = 'black',
                 link_color = 'darkorange', 
                 arrow_color = 'darkorange',
                 theme = 'default',
                 link_style = 'N',
                 pos = None, filename = None, index1 = None,
                 show_country_values = False,
                 show_capacities = False,
                 ):
    import pandas as pd
    pd.options.mode.chained_assignment = None #Disable warning (For line 218)
    import numpy as np
    import schemdraw
    
    # ------ INITIAL CHECKS ---------------------------------------------------
    
    # Check if model is solved by checking if an objective value exists
    if not hasattr(n, 'objective'):
        show_capacities = False
        print('\n WARNING: PyPSA NetView: \n "show_capacities" is True, but network is not solved. Setting "show_capacities = False". \n' )
    
    
    # ------ INITIAL SETUP ----------------------------------------------------
    # Set theme
    schemdraw.theme(theme)
    
    # Copy network to avoid changing network
    n = n.copy()
    
    if index1 is not None:
        n.links = n.links.reindex(index1)
        
    # Get positions for buses
    s = set_positions(pos, n, spacing)
            
    # ------ DRAW NETWORK -----------------------------------------------------
    with schemdraw.Drawing() as d:
    
        # Add columns with start and end cooridnates for links
        n.links['start'] = np.nan
        n.links['end']   = np.nan
        
        # ----- ADD BUS COMPONENTS -------------------
        for bus in n.buses.index:
            d += (elm.Dot()
                  .color(bus_color)
                  .label(bus, fontsize = title_fontsize)
                  .at(( s['x'][bus], s['y'][bus] )))
            
            # ----- Get elements on this bus from network -----
            gens   = n.generators[n.generators['bus'] == bus] #Get all generators on bus
            loads  = n.loads[n.loads['bus'] == bus]
            stores = n.stores[n.stores['bus'] == bus]
            
            # ----- Links from bus ----- 
            for link in n.links.index:
                # Loop through 
                
                if n.links['bus0'][link] == bus:
                    
                    d += elm.Line().color(bus_color).length(link_line_length) #Add line piece
                    d += (C := elm.Dot().color(link_color))
                    
                    # Set start point for this link to be the current bus
                    n.links['start'][link] = C
            
            # ----- Draw components on bus ----- 
            draw_component_on_bus(d, n, gens,
                                  show_capacities = show_capacities)
            
            draw_component_on_bus(d, n, loads,
                                  show_capacities = show_capacities)
            
            draw_component_on_bus(d, n, stores,
                                  show_capacities = show_capacities)
            
            # ----- Links to bus ----- 
            for link in n.links.index:
                
                if n.links['bus1'][link] == bus:
                    
                    d += elm.Line().color(bus_color).length(link_line_length) #Add line piece
                    d += (C := elm.Dot().color(link_color)) # Add dot for link
                    
                    # Set end point for link to be current bus
                    n.links['end'][link] = C
            
            # ----- End bus with dot with bus_color -----  
            d += elm.Line(arrow = '-o').color(bus_color).length(link_line_length)
        
        
        # ----- ADD LINKS BETWEEN BUSES -------------------
        for link in n.links.index:
            # Loop through all links, and create lines with arrows.
            
            n.links.reindex(index1)
            
            # Set link width
            link_width = ( (n.links.p_nom_opt[link]/n.links.p_nom_opt.max()) )*4 + 0.1 if show_capacities else 2
            
            # Set link style
            style = link_style
            
            # Set link label depending
            label = str(round(n.links.p_nom_opt[link])) + ' MW' if show_capacities else link
            
            # Draw link from link start to link end
            d += ( elm.Wire(style, k = 1)
                  .color(link_color)
                  .at(n.links['start'][link].center)
                  .to(n.links['end'][link].center)
                  .label(label, 
                         fontsize = title_fontsize,
                         color = bus_color)
                  .zorder(0.1)
                  .linewidth(link_width)
                  )
            
            # Add arrowhead to link end
            d += elm.Arrowhead(headwidth = headwidth, headlength = headlength).color(arrow_color)
            
            
            if n.links.p_min_pu[link] < 0:
                # if link is bidirectional, add an additional arrow head at 
                # link start.
                
                # Draw wire going from end to start, to get arrow direction
                d += ( elm.Wire(style, k = 1)
                      .color(link_color)
                      .at(n.links['end'][link].center)
                      .to(n.links['start'][link].center)
                      .zorder(0)
                      .linewidth(0)
                      )
                
                # Add arrow
                d += elm.Arrowhead(headwidth = headwidth, headlength = headlength).color(arrow_color)
            
            
    # Save drawing if filename is given  
    if filename is not None:
        if '.pdf' not in filename:
            filename += '.pdf'
        d.save(filename)
            
    fig = d.draw()
    
    return fig

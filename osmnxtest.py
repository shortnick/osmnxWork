import osmnx
import matplotlib.image as Image
import matplotlib.pyplot as plt 

osmnx.utils.config(log_file=True, log_console=True, use_cache=True)

prefix = 'Seattle'
placeS = ['Westlake', 'Pike St & Broadway', '1st Ave S & S Lander St', '23rd & Jackson', 'High Point']

pointS = [(47.611073, -122.337092), (47.614059, -122.320783), (47.579838, -122.334012), (47.599284, -122.302223), (47.542859, -122.376483)] 

img_folder = 'pictures'
dpi = 600
extension = 'png'

def osmnx_Graph_Pull(point, fileName):
	print("Beginning OSM query")
	#takes a lat/long point and file name, then queries OSM for nearby network, returns networkx multidigraph
	osmnxGraph = osmnx.core.graph_from_point(point, distance=1000, distance_type='bbox', network_type='all_private', simplify=True, 
		retain_all=False, truncate_by_edge=True, name=fileName, timeout=180, memory=None, max_query_area_size=2500000000, clean_periphery=True)
	print("OSM-->networkx Graph Pulled",/n,"++++++++++++++++++++++++++",/n)
	return osmnxGraph

def osm_City_Graph_Plot(netxGraph, fileName):
	#takes networkx multidigraph and filename, saves a configured image of the network snapshot
	print("Plotting City Grid",/n,"++++++++++++++++++++++++++",/n)
	cityPlot = osmnx.plot.plot_figure_ground(G=netxGraph, dist=1000, network_type='all', street_widths={'footway' : 0.5,
		'steps' : 0.5,
		'pedestrian' : 0.5,
		'path' : 0.5,
		'track' : 0.5,
		'service' : 2,
		'residential' : 3,
		'primary' : 5,
		'motorway' : 6}, default_width=4, fig_length=10, edge_color='w', bgcolor='#333333', 
		smooth_joints=True, filename=fileName, file_format=extension, show=False, save=True, close=True, dpi=300)
	print("City Plot saved",/n,"++++++++++++++++++++++++++",/n)
	return cityPlot


"""
def simple_graph(prefix, place, point, img_folder, dpi, extension):
	fig, ax = ox.plot_figure_ground(point=point, filename=(prefix+"_"+place), dpi=dpi)
	Image('{}/{}.{}'.format(img_folder, place , extension), height = 400, width = 400)
	print("Simple city graph saved")
"""

def netx_graph_work(latitude, longitude, fileName):
	#take a lat/long & name, then create a networkx multidigraph from OSM data:
	tempGraph = osmnx_Graph_Pull((latitude, longitude), fileName)

	#diversion point for saving a networkx multidigraph for analysis

	#taking in the graph and the place/filename, returns the good looking city graph

	osm_City_Graph_Plot(tempGraph, fileName)



assert len(placeS) == len(pointS)

for x, item in enumerate(placeS):
	fileName = prefix+item
	place = placeS[x]
	lat, leung = pointS[x]
	netx_graph_work(lat, leung, fileName)


	
"""
# you can also create a network with a buffer distance (meters) around the place
G = ox.graph_from_place('Piedmont, California, USA', network_type='walk', buffer_dist=200)
fig, ax = ox.plot_graph(ox.project_graph(G))

osmnx.buildings.buildings_from_point(point, distance, retain_invalid=False)

 osmnx.buildings.plot_buildings(gdf, fig=None, ax=None, figsize=None, color='#333333', bgcolor='w', set_bounds=True, bbox=None, save=False, show=True, close=False, filename='image', file_format='png', dpi=600)

    Plot a GeoDataFrame of building footprints.
    Parameters:	

        gdf (GeoDataFrame) – building footprints
        fig (figure) –
        ax (axis) –
        figsize (tuple) –
        color (string) – the color of the building footprints
        bgcolor (string) – the background color of the plot
        set_bounds (bool) – if True, set bounds from either passed-in bbox or the spatial extent of the gdf
        bbox (tuple) – if True and if set_bounds is True, set the display bounds to this bbox
        save (bool) – whether to save the figure to disk or not
        show (bool) – whether to display the figure or not
        close (bool) – close the figure (only if show equals False) to prevent display
        filename (string) – the name of the file to save
        file_format (string) – the format of the file to save (e.g., ‘jpg’, ‘png’, ‘svg’)
        dpi (int) – the resolution of the image file if saving

 osmnx.core.create_graph(response_jsons, name='unnamed', retain_all=False, network_type='all_private')

    Create a networkx graph from OSM data.
    Parameters:	

        response_jsons (list) – list of dicts of JSON responses from from the Overpass API
        name (string) – the name of the graph
        retain_all (bool) – if True, return the entire graph even if it is not connected
        network_type (string) – what type of network to create

    Returns:	

    Return type:	

    networkx multidigraph

 osmnx.core.graph_from_bbox(north, south, east, west, network_type='all_private', simplify=True, retain_all=False, truncate_by_edge=False, name='unnamed', timeout=180, memory=None, max_query_area_size=2500000000, clean_periphery=True)

Create a networkx graph from OSM data within some bounding box.
Parameters:	

    north (float) – northern latitude of bounding box
    south (float) – southern latitude of bounding box
    east (float) – eastern longitude of bounding box
    west (float) – western longitude of bounding box
    network_type (string) – what type of street network to get
    simplify (bool) – if true, simplify the graph topology
    retain_all (bool) – if True, return the entire graph even if it is not connected
    truncate_by_edge (bool) – if True retain node if it’s outside bbox but at least one of node’s neighbors are within bbox
    name (string) – the name of the graph
    timeout (int) – the timeout interval for requests and to pass to API
    memory (int) – server memory allocation size for the query, in bytes. If none, server will use its default allocation size
    max_query_area_size (float) – max size for any part of the geometry, in square degrees: any polygon bigger will get divided up for multiple queries to API
    clean_periphery (bool) – if True (and simplify=True), buffer 0.5km to get a graph larger than requested, then simplify, then truncate it to requested spatial extent

Returns:	

Return type:	

networkx multidigraph


osmnx.core.graph_from_point(center_point, distance=1000, distance_type='bbox', network_type='all_private', simplify=True, retain_all=False, truncate_by_edge=False, name='unnamed', timeout=180, memory=None, max_query_area_size=2500000000, clean_periphery=True)
osmnx.core.graph_from_point(center_point, distance=1000, distance_type='bbox', network_type='all_private', simplify=True, 
	retain_all=False, truncate_by_edge=True, name='unnamed', timeout=180, memory=None, max_query_area_size=2500000000, clean_periphery=True)


Create a networkx graph from OSM data within some distance of some (lat, lon) center point.
Parameters:	

    center_point (tuple) – the (lat, lon) central point around which to construct the graph
    distance (int) – retain only those nodes within this many meters of the center of the graph
    distance_type (string) – {‘network’, ‘bbox’} if ‘bbox’, retain only those nodes within a bounding box of the distance parameter. if ‘network’, retain only those nodes within some network distance from the center-most node.
    network_type (string) – what type of street network to get
    simplify (bool) – if true, simplify the graph topology
    retain_all (bool) – if True, return the entire graph even if it is not connected
    truncate_by_edge (bool) – if True retain node if it’s outside bbox but at least one of node’s neighbors are within bbox
    name (string) – the name of the graph
    timeout (int) – the timeout interval for requests and to pass to API
    memory (int) – server memory allocation size for the query, in bytes. If none, server will use its default allocation size
    max_query_area_size (float) – max size for any part of the geometry, in square degrees: any polygon bigger will get divided up for multiple queries to API
    clean_periphery (bool,) – if True (and simplify=True), buffer 0.5km to get a graph larger than requested, then simplify, then truncate it to requested spatial extent

Returns:	

Return type:	

networkx multidigraph

osmnx.plot.plot_figure_ground(G=None, address=None, point=None, dist=805, network_type='drive_service', street_widths=None, default_width=4, fig_length=8, edge_color='w', bgcolor='#333333', smooth_joints=True, filename=None, file_format='png', show=False, save=True, close=True, dpi=300)
osmnx.plot.plot_figure_ground(G=**None, dist=1000, network_type='all', street_widths={'footway' : 0.5,
                 'steps' : 0.5,
                 'pedestrian' : 0.5,
                 'path' : 0.5,
                 'track' : 0.5,
                 'service' : 2,
                 'residential' : 3,
                 'primary' : 5,
                 'motorway' : 6}, default_width=4, fig_length=10, edge_color='w', bgcolor='#333333', 
                 smooth_joints=True, filename=**None, file_format='png', show=False, save=True, close=True, dpi=300)

Plot a figure-ground diagram of a street network, defaulting to one square mile.
Parameters:	

    G (networkx multidigraph) –
    address (string) – the address to geocode as the center point if G is not passed in
    point (tuple) – the center point if address and G are not passed in
    dist (numeric) – how many meters to extend north, south, east, and west from the center point
    network_type (string) – what type of network to get
    street_widths (dict) – where keys are street types and values are widths to plot in pixels
    default_width (numeric) – the default street width in pixels for any street type not found in street_widths dict
    fig_length (numeric) – the height and width of this square diagram
    edge_color (string) – the color of the streets
    bgcolor (string) – the color of the background
    smooth_joints (bool) – if True, plot nodes same width as streets to smooth line joints and prevent cracks between them from showing
    filename (string) – filename to save the image as
    file_format (string) – the format of the file to save (e.g., ‘jpg’, ‘png’, ‘svg’)
    show (bool) – if True, show the figure
    save (bool) – if True, save the figure as an image file to disk
    close (bool) – close the figure (only if show equals False) to prevent display
    dpi (int) – the resolution of the image file if saving

Returns:	

fig, ax
Return type:	

tuple

"""
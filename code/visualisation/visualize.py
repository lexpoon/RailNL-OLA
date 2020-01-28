import plotly.graph_objects as go

from csv import reader
from functions.import_data import RailNL


def visualisation(map, routes):
    """ Visualize stations and routes in scattermapbox."""

    # Add stations to visualisation
    fig = visualize_stations(map)

    # Add all possible connections to visualisation
    fig = visualize_all_connections(map, fig)

    # Add routes to visualisation
    fig = visualize_routes(routes, fig)

    # Center and zoom figure to Holland
    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 4.900277615, 'lat': 52.37888718},
            'style': "carto-positron",
            'zoom': 7})

    fig.show()


def visualize_stations(map):
    """Add a marker to scattermapbox for each station in map."""

    # Read station longitudes and latitudes from csv into lists
    with open(f"data/Stations{map}.csv", "r") as f:
        csv_reader = reader(f)
        station = []
        lat = []
        lon = []
        for line in csv_reader:
            station.append(line[0])
            lat.append(line[1])
            lon.append(line[2])

    # Add marker for each station in list
    fig = go.Figure(go.Scattermapbox(
        mode = "markers",
        lon = lon,
        lat = lat,
        text = station,
        marker = {'size': 10}))

    return fig

def visualize_all_connections(map, fig):
    """Add a grey line for each possible connection to scattermapbox."""

    data = RailNL(map).data

    # Retrieve coordinates for connections in map
    with open(f'data/Connecties{map}.csv', "r") as f:
        csv_reader = reader(f)
        for connection in csv_reader:
            lon = []
            lat = []
            lat.append(data[connection[0]].coordinates["long"])
            lon.append(data[connection[0]].coordinates["lat"])
            lat.append(data[connection[1]].coordinates["long"])
            lon.append(data[connection[1]].coordinates["lat"])

            # Add grey trace for each connection
            fig.add_trace(go.Scattermapbox(
                mode = "lines",
                lon = lon,
                lat = lat,
                marker = { 'size': 10, 'color': 'rgb(204, 204, 204)' },
                showlegend = False
            ))

    return fig

def visualize_routes(routes, fig):
    """Add a coloured line to scattermapbox for each route."""

    # Visualize every route with a coloured line
    for route in routes:
        lon = []
        lat = []

        for station in route.route:
            lon.append(station.coordinates["lat"])
            lat.append(station.coordinates["long"])

        fig.add_trace(go.Scattermapbox(
            mode = "lines",
            lon = lon,
            lat = lat,
            marker = { 'size': 10 }))

    return fig

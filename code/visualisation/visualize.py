import csv
import plotly.graph_objects as go
from functions.import_data import RailNL

def visualisation(routes_list, map):
    """ Visualize stations and routes in scattermapbox. """

    # Read station longitudes and latitudes from csv into lists
    with open(f"data/Stations{map}.csv", "r") as f:
        csv_reader = csv.reader(f)
        station = []
        lat = []
        lon = []
        for line in csv_reader:
            station.append(line[0])
            lat.append(line[1])
            lon.append(line[2])

    # Add dot to figure for each station
    fig = go.Figure(go.Scattermapbox(
        mode = "markers",
        lon = lon,
        lat = lat,
        text = station,
        marker = {'size': 10}))

    # Visualize all possible connections in grey
    data = RailNL(map).data
    with open(f'data/Connecties{map}.csv', "r") as f:
        csv_reader = csv.reader(f)
        for connection in csv_reader:
            lon = []
            lat = []
            lat.append(data[connection[0]].coordinates["long"])
            lon.append(data[connection[0]].coordinates["lat"])
            lat.append(data[connection[1]].coordinates["long"])
            lon.append(data[connection[1]].coordinates["lat"])

            # Add route lines to figure
            fig.add_trace(go.Scattermapbox(
                mode = "lines",
                lon = lon,
                lat = lat,
                marker = { 'size': 10, 'color': 'rgb(90, 90, 90)' },
                showlegend = False
            ))

    # Visualize route for every route
    for route in routes_list:
        lon = []
        lat = []

        # Create two lists of longitutes and latitudes for stations in routes
        for station in route.route:
            lon.append(station.coordinates["lat"])
            lat.append(station.coordinates["long"])

        # Add route lines to figure
        fig.add_trace(go.Scattermapbox(
            mode = "lines",
            lon = lon,
            lat = lat,
            marker = { 'size': 10 }))

    # Center and zoom figure to Holland
    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 4.900277615, 'lat': 52.37888718},
            'style': "carto-positron",
            'zoom': 7})

    fig.show()

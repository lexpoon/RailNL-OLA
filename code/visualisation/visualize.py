import os, sys, csv
import plotly.graph_objects as go

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))
sys.path.append(os.path.join(directory, "code", "functions"))
sys.path.append(os.path.join(directory, "code", "visualisation"))

from import_data import RailNL

def visualisation(routes):
    """ Visualize stations and routes in scattermapbox. """

    filename = "data/StationsHolland.csv"

    # Read station longitudes and latitudes from csv into lists
    with open(filename, "r") as f:
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

    for k,v in routes.items():
        lon = []
        lat = []
        data = RailNL()

        # Create two lists of longitutes and latitudes for stations in routes
        for station in v:
            lon.append(data.data[station].coordinates['long'])
            lat.append(data.data[station].coordinates['lat'])

        # Add route lines to figure
        fig.add_trace(go.Scattermapbox(
            mode = "lines",
            lon = lon,
            lat = lat,
            marker = {'size': 10}))

    # Center and zoom figure to Holland
    fig.update_layout(
        margin ={'l':0,'t':0,'b':0,'r':0},
        mapbox = {
            'center': {'lon': 4.900277615, 'lat': 52.37888718},
            'style': "carto-positron", 
            'zoom': 7})

    fig.show()

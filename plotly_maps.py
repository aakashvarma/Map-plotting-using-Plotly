import plotly.plotly as py
from plotly.graph_objs import *
import plotly
from plotly.offline import plot
plotly.tools.set_credentials_file(username='aakashvarma18', api_key='tFCB65mxaAx9tFel2hDf')

mapbox_access_token = 'pk.eyJ1IjoiYWFrYXNoMTgiLCJhIjoiY2pka21xMzdzMDI1cTMzczN5MG9ic3c0eCJ9.-Jf_342u6cWFfCCAfWMJjQ'

lats=[12.9718,12.9718,12.9718]
lons=[79.1589,79.1590,79.1591]

plots=[]
for i,j in zip(lats,lons):
    data = Data([
        Scattermapbox(
            lat=[str(i)],
            lon=[str(j)],
            mode='markers',
            marker=Marker(
                size=14
            ),
            text=['VIT Vellore1','road2','road3'],
        )
    ])

    layout = Layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=13,
                lon=79
            ),
            pitch=0,
            zoom=5
        ),
    )
    fig = dict(data=data, layout=layout)
    plots.append(fig)
    print (fig)
plot(fig,"plot.html")
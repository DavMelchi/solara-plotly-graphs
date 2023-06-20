import solara
from utils import SharedSidebar
from bar import BarPlot
from line import LinePlot
from scatter import ScatterPlot
from pie import PieChart
from histogram import Histograms
from boxs import Boxs
from violin import Violins
from density_heatmap import DensityHeatmap
from treed_plot import TreeD
from maps import Maps
from other_plot import OtherPlots
from animated_plot import AnimatedPlots


@solara.component
def line():
    with solara.Sidebar():
        SharedSidebar()
    LinePlot()

@solara.component
def bar():
    with solara.Sidebar():
        SharedSidebar()
    BarPlot()
    

@solara.component
def scatter():
    with solara.Sidebar():
        SharedSidebar()
    ScatterPlot()

@solara.component
def pie_chart():
    with solara.Sidebar():
        SharedSidebar()
    PieChart()

@solara.component
def histogram():
    with solara.Sidebar():
        SharedSidebar()
    Histograms()

@solara.component
def Box():
    with solara.Sidebar():
        SharedSidebar()
    Boxs()

@solara.component
def violin():
    with solara.Sidebar():
        SharedSidebar()
    Violins()

@solara.component
def density():
    with solara.Sidebar():
        SharedSidebar()
    DensityHeatmap()

@solara.component
def treeD_plot():
    with solara.Sidebar():
        SharedSidebar()
    TreeD()

@solara.component
def map_plot():
    with solara.Sidebar():
        SharedSidebar()
    Maps()

@solara.component
def other():
    with solara.Sidebar():
        SharedSidebar()
    OtherPlots()
    

@solara.component
def animate():
    with solara.Sidebar():
        SharedSidebar()
    AnimatedPlots()

routes = [
    solara.Route(path="/", component=line, label="Line"),
    solara.Route(path="bar", component=bar, label="Bar"),
    solara.Route(path="scatter", component=scatter, label="Scatter"),
    solara.Route(path="pie", component=pie_chart, label="Pie"),
    solara.Route(path="histogram", component=histogram, label="Histogram"),
    solara.Route(path="box", component=Box, label="Box"),
    solara.Route(path="violin", component=violin, label="Violin"),
    solara.Route(path="density-heatmap", component=density, label="Density-Heatmap"),
    solara.Route(path="Plot_3D", component=treeD_plot, label="3D-Plot"),
    solara.Route(path="map", component=map_plot, label="Maps"),
    solara.Route(path="other", component=other, label="Other_Plot"),
    solara.Route(path="animated", component=animate, label="Animated_Plot"),

]

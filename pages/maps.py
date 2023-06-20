import solara
import pandas as pd
import plotly.express as px
from utils import selected_template

# You can color complex maps like we do here representing unemployment data

# Allows us to grab data from a supplied URL
from urllib.request import urlopen
# Used to decode JSON data
import json
# Grab US county geometry data
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

# Grab unemployment data based on each counties Federal Information Processing number
df2 = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                dtype={"fips": str})



@solara.component
def Maps():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#Map Scatter Plots")

        # There are many interesting ways of working with maps
        # plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html
        df = px.data.gapminder().query("year == 2007")
        fig1 = px.scatter_geo(df, locations="iso_alpha",
                            color="continent", # which column to use to set the color of markers
                            hover_name="country", # column added to hover information
                            size="pop", # size of markers
                            projection="orthographic",
                            template=selected_template.value
                            )


        # solara.Markdown(f"#### Use Box plot to compare different variables ")
        solara.Markdown("""
                        ```python
                            # There are many interesting ways of working with maps
                            # plotly.com/python-api-reference/generated/plotly.express.scatter_geo.html
                            df = px.data.gapminder().query("year == 2007")
                            fig = px.scatter_geo(df, locations="iso_alpha",
                                                color="continent", # which column to use to set the color of markers
                                                hover_name="country", # column added to hover information
                                                size="pop", # size of markers
                                                projection="orthographic")
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)

        # Draw map using the county JSON data, color using unemployment values on a range of 12
        fig2 = px.choropleth(df2, geojson=counties, locations='fips', color='unemp',
                                color_continuous_scale="Viridis",
                                range_color=(0, 12),
                                scope="usa",
                                labels={'unemp':'unemployment rate'},
                                template=selected_template.value
                                )

        solara.Markdown(f"####Choropleth Maps")
        solara.Markdown("""
                        ```python
                            # You can color complex maps like we do here representing unemployment data

                            # Allows us to grab data from a supplied URL
                            from urllib.request import urlopen
                            # Used to decode JSON data
                            import json
                            # Grab US county geometry data
                            with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
                                counties = json.load(response)

                            # Grab unemployment data based on each counties Federal Information Processing number
                            df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                                            dtype={"fips": str})

                            # Draw map using the county JSON data, color using unemployment values on a range of 12
                            fig2 = px.choropleth(df, geojson=counties, locations='fips', color='unemp',
                                                    color_continuous_scale="Viridis",
                                                    range_color=(0, 12),
                                                    scope="usa",
                                                    labels={'unemp':'unemployment rate'}
                                                    )

                        ```
                        """
                        )
        solara.FigurePlotly(fig2)

    return main

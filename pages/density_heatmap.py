import solara
import seaborn as sns
import plotly.express as px
from utils import selected_template


@solara.component
def DensityHeatmap():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#Density Heatmap")
        # Create a heatmap using Seaborn data
        flights = sns.load_dataset("flights")
        flights

        # You can set bins with nbinsx and nbinsy
        fig1 = px.density_heatmap(flights, x='year', y='month', z='passengers', 
                                color_continuous_scale="Viridis",
                                template=selected_template.value)

        solara.Markdown(f"####Create a heatmap using Seaborn data")
        
        solara.Markdown("""
                        ```python
                            # Create a heatmap using Seaborn data
                            flights = sns.load_dataset("flights")
                            flights

                            # You can set bins with nbinsx and nbinsy
                            fig1 = px.density_heatmap(flights, x='year', y='month', z='passengers', 
                                                    color_continuous_scale="Viridis")
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)



        # You can add histograms
        fig2 = px.density_heatmap(flights, x='year', y='month', z='passengers', 
                                marginal_x="histogram", marginal_y="histogram",
                                template=selected_template.value)

        solara.Markdown(f"####Add histograms")
        solara.Markdown("""
                        ```python
                            # You can add histograms
                            fig2 = px.density_heatmap(flights, x='year', y='month', z='passengers', 
                                                    marginal_x="histogram", marginal_y="histogram")
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)

    return main

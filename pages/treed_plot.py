import solara
import seaborn as sns
import plotly.express as px
from utils import selected_template

@solara.component
def TreeD():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#3D Scatter Plots")

        flights = sns.load_dataset("flights")
        # Create a 3D scatter plot using flight data
        fig1 = px.scatter_3d(flights, x='year', y='month', z='passengers', color='year',
                        opacity=0.7, 
                        width=800, height=400,
                        template=selected_template.value)


        # solara.Markdown(f"#### Use Box plot to compare different variables ")
        solara.Markdown("""
                        ```python
                            flights = sns.load_dataset("flights")
                            # Create a 3D scatter plot using flight data
                            fig1 = px.scatter_3d(flights, x='year', y='month', z='passengers', color='year',
                                            opacity=0.7, width=800, height=400)
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)


        # With a scatter matrix we can compare changes when comparing column data
        fig2 = px.line_3d(flights, x='year', y='month', z='passengers', color='year',template=selected_template.value)

        solara.Markdown(f"#3D Line Plots")
        solara.Markdown("""
                        ```python
                            # With a scatter matrix we can compare changes when comparing column data
                            fig2 = px.line_3d(flights, x='year', y='month', z='passengers', color='year')

                        ```
                        """
                        )
        solara.FigurePlotly(fig2)

    return main

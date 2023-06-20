import solara
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from utils import selected_template


@solara.component
def ScatterPlot():
    with solara.Row(justify='space-around') as main:
        with solara.Column(gap="10px",align="stretch"):
            with solara.Card():
                with solara.Row():
                    with solara.Column():
                        selection_data, set_selection_data = solara.use_state(None)
                        click_data, set_click_data = solara.use_state(None)
                        hover_data, set_hover_data = solara.use_state(None)
                        unhover_data, set_unhover_data = solara.use_state(None)
                        deselect_data, set_deselect_data = solara.use_state(None)
                        
                        
                        solara.Markdown(f"#SCATTER PLOTS")
                        # Use included Iris data set
                        df_iris = px.data.iris()
                        # Create a scatter plot by defining x, y, different color for count of provided
                        # column, size based on supplied column and additional data to display on hover
                        fig1= px.scatter(df_iris, x="sepal_width", y="sepal_length", color="species", template=selected_template.value,
                                        size='petal_length', hover_data=['petal_width'])

                        solara.Markdown(f"###Create a scatter plot by defining x, y, different color for count of provided")
                        solara.Markdown("""
                                        ```python
                                            fig1= px.scatter(df_iris, x="sepal_width", y="sepal_length", color="species",
                                            size='petal_length', hover_data=['petal_width'])
                                        ```
                                        """
                                        )
                        solara.FigurePlotly(fig1, on_selection=set_selection_data, 
                                            on_click=set_click_data, on_hover=set_hover_data, 
                                            on_unhover=set_unhover_data, on_deselect=set_deselect_data)

                    with solara.Columns():
                            solara.Markdown(
                                                        f"""
                                            # Events data
                                            ## selection
                                            ```
                                            {selection_data}
                                            ```

                                            ## click
                                            ```
                                            {click_data}
                                            ```

                                            ## hover
                                            ```
                                            {hover_data}
                                            ```

                                            ## unhover
                                            ```
                                            {unhover_data}
                                            ```

                                            ## deselect
                                            ```
                                            {deselect_data}
                                            ```
                                            """
                                                    )

            with solara.Column(gap="10px",align="stretch"):
                # Create a customized scatter with black marker edges with line width 2, opaque
                # and colored based on width. Also show a scale on the right
                fig2 = go.Figure()
                fig2.add_trace(go.Scatter(
                    x=df_iris.sepal_width, y=df_iris.sepal_length,
                    mode='markers',
                    marker_color=df_iris.sepal_width,
                    text=df_iris.species,
                    marker=dict(showscale=True)
                ))
                fig2.update_traces(marker_line_width=2, marker_size=10)
                fig2.update_layout(template= selected_template.value)
                solara.Markdown(f"##Create a customized scatter with black marker edges with line width 2, opaque and colored based on width. Also show a scale on the right")
                solara.Markdown("""
                                ```python
                                    fig2 = go.Figure()
                                    fig2.add_trace(go.Scatter(
                                        x=df_iris.sepal_width, y=df_iris.sepal_length,
                                        mode='markers',
                                        marker_color=df_iris.sepal_width,
                                        text=df_iris.species,
                                        marker=dict(showscale=True)
                                    ))
                                    fig2.update_traces(marker_line_width=2, marker_size=10)
                                ```
                                """
                                )
                solara.FigurePlotly(fig2)

                    # Working with a lot of data use Scattergl
                fig3 = go.Figure(data=go.Scattergl(
                    x = np.random.randn(10000),
                    y = np.random.randn(10000),
                    mode='markers',
                    marker=dict(
                        color=np.random.randn(10000),
                        colorscale='Viridis',
                        line_width=1
                    )
                ))
                fig3.update_layout(template= selected_template.value)

                solara.Markdown(f"#Working with a lot of data use *Scattergl*")
                solara.Markdown("""
                                ```python
                                    fig3 = go.Figure(data=go.Scattergl(
                                        x = np.random.randn(10000),
                                        y = np.random.randn(10000),
                                        mode='markers',
                                        marker=dict(
                                            color=np.random.randn(10000),
                                            colorscale='Viridis',
                                            line_width=1
                                        )
                                    ))
                                ```
                                """
                                )
                solara.FigurePlotly(fig3)




                # With a scatter matrix we can compare changes when comparing column data
                flights = sns.load_dataset("flights")
                
                fig4 = px.scatter_matrix(flights, color='month',template=selected_template.value,)


                solara.Markdown(f"##Scatter Matrix")
                solara.Markdown("""
                                ```python
                                    # With a scatter matrix we can compare changes when comparing column data
                                    flights = sns.load_dataset("flights")                            
                                    fig3 = px.scatter_matrix(flights, color='month')
                                ```
                                """
                                )
                solara.FigurePlotly(fig4)

        return main

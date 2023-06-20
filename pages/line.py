import solara
import plotly.express as px
import plotly.graph_objects as go
from utils import selected_template

@solara.component
def LinePlot():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#LINE PLOTS")
        
        df_stocks = px.data.stocks()
        fig1 = px.line(df_stocks, x='date', y='GOOG', labels={'x':'Date', 'y':'Price'},
                    template=selected_template.value
                    )
        solara.Markdown(f"###Use included Google price data to make one plot")
        
        solara.Markdown("""
                        ```python
                        fig1 = px.line(df_stocks, x='date', y='GOOG', labels={'x':'Date', 'y':'Price'},
                        template=selection_data.value)
                        ```
                        """
                        )
                        
                        

        solara.FigurePlotly(fig1)
        
        all_stocks =df_stocks.columns.values.tolist()
        del all_stocks[0]
        stocks,set_stocks = solara.use_state ([all_stocks[0],all_stocks[1]])

        fig2 = px.line(df_stocks, x='date', y=stocks, labels={'x':'Date', 'y':'Price'},
            title=" VS ".join(stocks),
            template=selected_template.value)

        with solara.Card():
            solara.Markdown(f"###Make multiple line plots")
            
            solara.Markdown("""
                            ```python
                            fig2 = px.line(df_stocks, x='date', y=['GOOG','AAPL'], labels={'x':'Date', 'y':'Price'},
                                title='Apple Vs. Google',template=selection_data.value)
                            ```
                            """
                            )
            
            solara.FigurePlotly(fig2)
            solara.SelectMultiple("Stocks", values= stocks, all_values= all_stocks, on_value =set_stocks)


        # Create a figure to which I'll add plots
        fig3 = go.Figure()
        # You can pull individual columns of data from the dataset and use markers or not
        fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL, 
                                mode='lines', name='Apple'))
        fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN, 
                                mode='lines+markers', name='Amazon'))
        # You can create custom lines (Dashes : dash, dot, dashdot)
        fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG, 
                                mode='lines+markers', name='Google',
                                line=dict(color='firebrick', width=2, dash='dashdot')))
        fig3.update_layout(template= selected_template.value)

        solara.Markdown(f"###Create a figure to which I'll add plots")
        
        solara.Markdown("""
                        ```python
                            fig3 = go.Figure()
                            # You can pull individual columns of data from the dataset and use markers or not
                            fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL, 
                                                    mode='lines', name='Apple'))
                            fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN, 
                                                    mode='lines+markers', name='Amazon'))
                            # You can create custom lines (Dashes : dash, dot, dashdot)
                            fig3.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG, 
                                                    mode='lines+markers', name='Google',
                                                    line=dict(color='firebrick', width=2, dash='dashdot')))
                        ```
                        """
                        )
        
        solara.FigurePlotly(fig3)


        solara.Markdown(f"###Go crazy styling the figure")

        fig4 =  go.Figure()
        # You can pull individual columns of data from the dataset and use markers or not
        fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL, 
                                mode='lines', name='Apple'))
        fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN, 
                                mode='lines+markers', name='Amazon'))
        # You can create custom lines (Dashes : dash, dot, dashdot)
        fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG, 
                                mode='lines+markers', name='Google',
                                line=dict(color='firebrick', width=2, dash='dashdot')))
        fig4.update_layout(template= selected_template.value)
        fig4.update_layout(
            # Shows gray line without grid, styling fonts, linewidths and more
                xaxis=dict(
                    showline=True,
                    showgrid=False,
                    showticklabels=True,
                    linecolor='rgb(204, 204, 204)',
                    linewidth=2,
                    ticks='outside',
                    tickfont=dict(
                        family='Arial',
                        size=12,
                        color='rgb(82, 82, 82)',
                    ),
                ),
                # Turn off everything on y axis
                yaxis=dict(
                    showgrid=False,
                    zeroline=False,
                    showline=False,
                    showticklabels=False,
                ),
                # autosize=False,
                margin=dict(
                    autoexpand=False,
                    l=100,
                    r=20,
                    t=110,
                ),
                showlegend=False,
                plot_bgcolor='white'
            )
        
        solara.Markdown("""
                ```python
                    fig4 =  go.Figure()
                            # You can pull individual columns of data from the dataset and use markers or not
                            fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AAPL, 
                                                    mode='lines', name='Apple'))
                            fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.AMZN, 
                                                    mode='lines+markers', name='Amazon'))
                            # You can create custom lines (Dashes : dash, dot, dashdot)
                            fig4.add_trace(go.Scatter(x=df_stocks.date, y=df_stocks.GOOG, 
                                                    mode='lines+markers', name='Google',
                                                    line=dict(color='firebrick', width=2, dash='dashdot')))
                            fig4.update_layout(template= selection_data.value)
                            fig4.update_layout(
                                # Shows gray line without grid, styling fonts, linewidths and more
                                    xaxis=dict(
                                        showline=True,
                                        showgrid=False,
                                        showticklabels=True,
                                        linecolor='rgb(204, 204, 204)',
                                        linewidth=2,
                                        ticks='outside',
                                        tickfont=dict(
                                            family='Arial',
                                            size=12,
                                            color='rgb(82, 82, 82)',
                                        ),
                                    ),
                                    # Turn off everything on y axis
                                    yaxis=dict(
                                        showgrid=False,
                                        zeroline=False,
                                        showline=False,
                                        showticklabels=False,
                                    ),
                                    # autosize=False,
                                    margin=dict(
                                        autoexpand=False,
                                        l=100,
                                        r=20,
                                        t=110,
                                    ),
                                    showlegend=False,
                                    plot_bgcolor='white'
                                )
                ```
                """
                )
        solara.FigurePlotly(fig4)
    
    return main
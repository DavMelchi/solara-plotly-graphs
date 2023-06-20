import solara
import plotly.express as px
import plotly.graph_objects as go
from utils import selected_template



@solara.component
def Boxs():
    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#BOX PLOTS")

        # A box plot allows you to compare different variables
        # The box shows the quartiles of the data. The bar in the middle is the median 
        # The whiskers extend to all the other data aside from the points that are considered
        # to be outliers
        df_tips = px.data.tips()
        # We can see which sex tips the most, points displays all the data points
        fig1= px.box(df_tips, x='sex', y='tip', points='all', template= selected_template.value)
        
        
        # Display tip sex data by day
        fig2=px.box(df_tips, x='day', y='tip', color='sex', template= selected_template.value)

        # Adding standard deviation and mean
        fig3 = go.Figure()
        fig3.add_trace(go.Box(x=df_tips.sex, y=df_tips.tip, marker_color='blue',
                            boxmean='sd'))
        fig3.update_layout(template= selected_template.value)

        solara.Markdown(f"#### Use Box plot to compare different variables ")
        solara.Markdown("""
                        ```python
                            # A box plot allows you to compare different variables
                            # The box shows the quartiles of the data. The bar in the middle is the median 
                            # The whiskers extend to all the other data aside from the points that are considered
                            # to be outliers
                            df_tips = px.data.tips()
                            # We can see which sex tips the most, points displays all the data points
                            px.box(df_tips, x='sex', y='tip', points='all')

                            # Display tip sex data by day
                            px.box(df_tips, x='day', y='tip', color='sex')

                            # Adding standard deviation and mean
                            fig1 = go.Figure()
                            fig1.add_trace(go.Box(x=df_tips.sex, y=df_tips.tip, marker_color='blue',
                                                boxmean='sd'))
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)
        solara.FigurePlotly(fig2)
        solara.FigurePlotly(fig3)


        # Complex Styling
        df_stocks = px.data.stocks()
        fig4 = go.Figure()
        # Show all points, spread them so they don't overlap and change whisker width
        fig4.add_trace(go.Box(y=df_stocks.GOOG, boxpoints='all', name='Google',
                            fillcolor='blue', jitter=0.5, whiskerwidth=0.2))
        fig4.add_trace(go.Box(y=df_stocks.AAPL, boxpoints='all', name='Apple',
                            fillcolor='red', jitter=0.5, whiskerwidth=0.2))
        # Change background / grid colors
        fig4.update_layout(title='Google vs. Apple', 
                        yaxis=dict(gridcolor='rgb(255, 255, 255)',
                        gridwidth=3),template= selected_template.value,
                        paper_bgcolor='rgb(243, 243, 243)',
                        plot_bgcolor='rgb(243, 243, 243)'
                        )

        # fig4.update_layout(template= selected_template.value)
        solara.Markdown(f"####Complex Styling")
        solara.Markdown("""
                        ```python
                            # Complex Styling
                            df_stocks = px.data.stocks()
                            fig2 = go.Figure()
                            # Show all points, spread them so they don't overlap and change whisker width
                            fig2.add_trace(go.Box(y=df_stocks.GOOG, boxpoints='all', name='Google',
                                                fillcolor='blue', jitter=0.5, whiskerwidth=0.2))
                            fig2.add_trace(go.Box(y=df_stocks.AAPL, boxpoints='all', name='Apple',
                                                fillcolor='red', jitter=0.5, whiskerwidth=0.2))
                            # Change background / grid colors
                            fig2.update_layout(title='Google vs. Apple', 
                                            yaxis=dict(gridcolor='rgb(255, 255, 255)',
                                            gridwidth=3),
                                            paper_bgcolor='rgb(243, 243, 243)',
                                            plot_bgcolor='rgb(243, 243, 243)')
                        ```
                        """
                        )
        solara.FigurePlotly(fig4)

    return main

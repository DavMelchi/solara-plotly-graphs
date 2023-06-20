import solara
import plotly.express as px
from utils import selected_template


@solara.component
def BarPlot():
    with solara.Column(gap="10px",align="stretch" ) as main:
        solara.Markdown(f"#BAR PLOTS")
        # Get population change in US by querying for US data
        df_us = px.data.gapminder().query("country == 'United States'")
        fig1 = px.bar(df_us, x='year', y='pop',template=selected_template.value)
        solara.FigurePlotly(fig1)

        # Create a stacked bar with more customization
        df_tips = px.data.tips()
        fig2 = px.bar(df_tips, x='day', y='tip', color='sex', title='Tips by Sex on Each Day',template=selected_template.value,
            labels={'tip': 'Tip Amount', 'day': 'Day of the Week'})
        solara.Markdown(f"###Create a stacked bar with more customization")
        solara.Markdown("""
                        ```python
                        fig2 = px.bar(df_tips, x='day', y='tip', color='sex', title='Tips by Sex on Each Day',
                            labels={'tip': 'Tip Amount', 'day': 'Day of the Week'})
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)

        # Place bars next to each other
        fig3 = px.bar(df_tips, x="sex", y="total_bill",template=selected_template.value,
                    color='smoker', barmode='group')
        solara.Markdown(f"###Place bars next to each other")
        solara.Markdown("""
                        ```python
                            fig3 = px.bar(df_tips, x="sex", y="total_bill",
                                        color='smoker', barmode='group')
                        ```
                        """
                        )
        solara.FigurePlotly(fig3)

        # Display pop data for countries in Europe in 2007 greater than 2000000
        df_europe = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
        fig4 = px.bar(df_europe, y='pop', x='country', text='pop', color='country',template=selected_template.value)
        # Put bar total value above bars with 2 values of precision
        fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        # Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
        fig4.update_layout(uniformtext_minsize=8)
        # Rotate labels 45 degrees
        fig4.update_layout(xaxis_tickangle=-45)

        solara.Markdown(f"###Display pop data for countries in Europe in 2007 greater than 2000000")
        solara.Markdown("""
                        ```python
                            df_europe = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
                            fig4 = px.bar(df_europe, y='pop', x='country', text='pop', color='country')
                            # Put bar total value above bars with 2 values of precision
                            fig4.update_traces(texttemplate='%{text:.2s}', textposition='outside')
                            # Set fontsize and uniformtext_mode='hide' says to hide the text if it won't fit
                            fig4.update_layout(uniformtext_minsize=8)
                            # Rotate labels 45 degrees
                            fig4.update_layout(xaxis_tickangle=-45)
                        ```
                        """
                        )



        solara.FigurePlotly(fig4)

    return main



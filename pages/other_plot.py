import solara
import seaborn as sns
import plotly.express as px
from utils import selected_template


@solara.component
def OtherPlots():

        
    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#Polar Chart")
        
        # Polar charts display data radially 
        # Let's plot wind data based on direction and frequency
        # You can change size and auto-generate different symbols as well
        df_wind = px.data.wind()
        px.scatter_polar(df_wind, r="frequency", theta="direction", color="strength",
                        size="frequency", symbol="strength",
                        template=selected_template.value)

        # Data can also be plotted using lines radially
        # A template makes the data easier to see
        fig1 = px.line_polar(df_wind, r="frequency", theta="direction", color="strength",
                line_close=True, template="plotly_dark", width=800, height=400)
        
        solara.Markdown("""
                        ```python
                            # Polar charts display data radially 
                            # Let's plot wind data based on direction and frequency
                            # You can change size and auto-generate different symbols as well
                            df_wind = px.data.wind()
                            px.scatter_polar(df_wind, r="frequency", theta="direction", color="strength",
                                            size="frequency", symbol="strength")

                            # Data can also be plotted using lines radially
                            # A template makes the data easier to see
                            fig1 = px.line_polar(df_wind, r="frequency", theta="direction", color="strength",
                                    line_close=True, template="plotly_dark", width=800, height=400)
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)


        # Used to represent ratios of 3 variables
        df_exp = px.data.experiment()
        fig2 = px.scatter_ternary(df_exp, a="experiment_1", b="experiment_2", 
                        c='experiment_3', hover_name="group", color="gender",template=selected_template.value)

        solara.Markdown(f"#Ternary Plot")
        solara.Markdown("""
                        ```python
                        # Used to represent ratios of 3 variables
                        df_exp = px.data.experiment()
                        px.scatter_ternary(df_exp, a="experiment_1", b="experiment_2", 
                                        c='experiment_3', hover_name="group", color="gender")
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)



        # You can create numerous subplots
        df_tips = px.data.tips()
        fig3= px.scatter(df_tips, x="total_bill", y="tip", color="smoker", facet_col="sex",
                         template=selected_template.value)

        # We can line up data in rows and columns
        fig4 = px.histogram(df_tips, x="total_bill", y="tip", color="sex", facet_row="time", facet_col="day",template=selected_template.value,
            category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})

        # This dataframe provides scores for different students based on the level
        # of attention they could provide during testing
        att_df = sns.load_dataset("attention")
        fig5 = px.line(att_df, x='solutions', y='score', facet_col='subject',
                    facet_col_wrap=5, title='Scores Based on Attention',
                    template=selected_template.value)

        solara.Markdown(f"#Facets")
        solara.Markdown("""
                        ```python
                            # You can create numerous subplots
                            df_tips = px.data.tips()
                            px.scatter(df_tips, x="total_bill", y="tip", color="smoker", facet_col="sex")

                            # We can line up data in rows and columns
                            fig3 = px.histogram(df_tips, x="total_bill", y="tip", color="sex", facet_row="time", facet_col="day",
                                category_orders={"day": ["Thur", "Fri", "Sat", "Sun"], "time": ["Lunch", "Dinner"]})

                            # This dataframe provides scores for different students based on the level
                            # of attention they could provide during testing
                            att_df = sns.load_dataset("attention")
                            fig4 = fig = px.line(att_df, x='solutions', y='score', facet_col='subject',
                                        facet_col_wrap=5, title='Scores Based on Attention')
                        ```
                        """
                        )
        solara.FigurePlotly(fig3)
        solara.FigurePlotly(fig4)
        solara.FigurePlotly(fig5)

    return main

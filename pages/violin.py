import solara
import plotly.express as px
import plotly.graph_objects as go
from utils import selected_template

@solara.component
def Violins():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#VIOLIN PLOTS")

        # Violin Plot is a combination of the boxplot and KDE
        # While a box plot corresponds to data points, the violin plot uses the KDE estimation
        # of the data points
        df_tips = px.data.tips()
        fig1= px.violin(df_tips, y="total_bill", box=True, points='all',template=selected_template.value)


        # solara.Markdown(f"#### Use Box plot to compare different variables ")
        solara.Markdown("""
                        ```python
                            # Violin Plot is a combination of the boxplot and KDE
                            # While a box plot corresponds to data points, the violin plot uses the KDE estimation
                            # of the data points
                            df_tips = px.data.tips()
                            px.violin(df_tips, y="total_bill", box=True, points='all')
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)


        # Multiple plots
        fig2 = px.violin(df_tips, y="tip", x="smoker", color="sex", box=True, points="all",
                hover_data=df_tips.columns,template=selected_template.value)

        solara.Markdown(f"####Multiple plots")
        solara.Markdown("""
                        ```python
                            # Multiple plots
                            px.violin(df_tips, y="tip", x="smoker", color="sex", box=True, points="all",
                                    hover_data=df_tips.columns)
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)



        # Morph left and right sides based on if the customer smokes
        fig3 = go.Figure()
        fig3.add_trace(go.Violin(x=df_tips['day'][ df_tips['smoker'] == 'Yes' ],
                                y=df_tips['total_bill'][ df_tips['smoker'] == 'Yes' ],
                                legendgroup='Yes', scalegroup='Yes', name='Yes',
                                side='negative',
                                line_color='blue'))
        fig3.add_trace(go.Violin(x=df_tips['day'][ df_tips['smoker'] == 'No' ],
                                y=df_tips['total_bill'][ df_tips['smoker'] == 'No' ],
                                legendgroup='Yes', scalegroup='Yes', name='No',
                                side='positive',
                                line_color='red'))
        fig3.update_layout(template= selected_template.value)
        
        solara.Markdown(f"####MMorph left and right sides based on if the customer smokes")
        solara.Markdown("""
                        ```python
                            # Morph left and right sides based on if the customer smokes
                            fig3 = go.Figure()
                            fig3.add_trace(go.Violin(x=df_tips['day'][ df_tips['smoker'] == 'Yes' ],
                                                    y=df_tips['total_bill'][ df_tips['smoker'] == 'Yes' ],
                                                    legendgroup='Yes', scalegroup='Yes', name='Yes',
                                                    side='negative',
                                                    line_color='blue'))
                            fig3.add_trace(go.Violin(x=df_tips['day'][ df_tips['smoker'] == 'No' ],
                                                    y=df_tips['total_bill'][ df_tips['smoker'] == 'No' ],
                                                    legendgroup='Yes', scalegroup='Yes', name='No',
                                                    side='positive',
                                                    line_color='red'))
                        ```
                        """
                        )
        solara.FigurePlotly(fig3)
    return main

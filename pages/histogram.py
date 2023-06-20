import solara
import numpy as np
import plotly.express as px
from utils import selected_template


@solara.component
def Histograms():

    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#HISTOGRAMS")

        # Plot histogram based on rolling 2 dice
        dice_1 = np.random.randint(1,7,5000)
        dice_2 = np.random.randint(1,7,5000)
        dice_sum = dice_1 + dice_2
        # bins represent the number of bars to make
        # Can define x label, color, title
        # marginal creates another plot (violin, box, rug)
        fig1 = px.histogram(dice_sum, nbins=11, labels={'value':'Dice Roll'},
                    title='5000 Dice Roll Histogram', marginal='violin',
                    color_discrete_sequence=['green'])

        fig1.update_layout(
            xaxis_title_text='Dice Roll',
            yaxis_title_text='Dice Sum',
            bargap=0.2, showlegend=False,
            template=selected_template.value
        )

        solara.Markdown(f"#### Plot histogram based on rolling 2 dice ")
        solara.Markdown("""
                        ```python
                            dice_1 = np.random.randint(1,7,5000)
                            dice_2 = np.random.randint(1,7,5000)
                            dice_sum = dice_1 + dice_2
                            # bins represent the number of bars to make
                            # Can define x label, color, title
                            # marginal creates another plot (violin, box, rug)
                            fig1 = px.histogram(dice_sum, nbins=11, labels={'value':'Dice Roll'},
                                        title='5000 Dice Roll Histogram', marginal='violin',
                                        color_discrete_sequence=['green'])

                            fig1.update_layout(
                                xaxis_title_text='Dice Roll',
                                yaxis_title_text='Dice Sum',
                                bargap=0.2, showlegend=False
                            )
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)



        # Stack histograms based on different column data
        df_tips = px.data.tips()
        fig2= px.histogram(df_tips, x="total_bill", color="sex",template=selected_template.value)


        solara.Markdown(f"####Stack histograms based on different column data")
        solara.Markdown("""
                        ```python
                            df_tips = px.data.tips()
                            px.histogram(df_tips, x="total_bill", color="sex")
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)
        
    return main

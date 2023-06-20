import solara
import plotly.express as px
from utils import selected_template



@solara.component
def AnimatedPlots():
        
    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#Animated Plots")
        # Create an animated plot that you can use to cycle through continent
        # GDP & life expectancy changes
        df_cnt = px.data.gapminder()
        fig1= px.scatter(df_cnt, x="gdpPercap", y="lifeExp", animation_frame="year", 
                animation_group="country",
                template=selected_template.value,
                size="pop", color="continent", hover_name="country",
                log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

        # Watch as bars chart population changes
        fig2 =px.bar(df_cnt, x="continent", y="pop", color="continent",template=selected_template.value,
        animation_frame="year", animation_group="country", range_y=[0,4000000000])

        solara.Markdown("""
                        ```python
                            # Create an animated plot that you can use to cycle through continent
                            # GDP & life expectancy changes
                            df_cnt = px.data.gapminder()
                            px.scatter(df_cnt, x="gdpPercap", y="lifeExp", animation_frame="year", 
                                    animation_group="country",
                                    size="pop", color="continent", hover_name="country",
                                    log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])

                            # Watch as bars chart population changes
                            px.bar(df_cnt, x="continent", y="pop", color="continent",
                            animation_frame="year", animation_group="country", range_y=[0,4000000000])
                        ```
                        """
                        )
        solara.display(fig1)
        solara.display(fig2)

    return main

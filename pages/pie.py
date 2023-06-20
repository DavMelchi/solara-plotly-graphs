import solara
import plotly.express as px
import plotly.graph_objects as go
from utils import selected_template

@solara.component
def PieChart():
    
    with solara.Column(gap="20px", align = "stretch") as main:
        
        solara.Markdown(f"#PIE CHARTS")
        # Use included Iris data set
        df_samer = px.data.gapminder().query("year == 2007").query("continent == 'Asia'")
        
        fig1= px.pie(df_samer, values='pop', names='country', height= 700,
            title='Population of Asian continent',template= selected_template.value,
            color_discrete_sequence=px.colors.sequential.RdBu)

        solara.Markdown(f"#### Create Pie chart of the largest nations in Asia ")
        solara.Markdown("[Color maps here](https://plotly.com/python/builtin-colorscales)")
        solara.Markdown("""
                        ```python
                            # Use included Iris data set
                            df_samer = px.data.gapminder().query("year == 2007").query("continent == 'Asia'")
                            fig1= px.pie(df_samer, values='pop', names='country', 
                                title='Population of Asian continent', 
                                color_discrete_sequence=px.colors.sequential.RdBu)
                        ```
                        """
                        )
        solara.FigurePlotly(fig1)



        # Customize pie chart
        colors = ['blue', 'green', 'black', 'purple', 'red', 'brown']
        fig2 = go.Figure(data=[go.Pie(labels=['Water','Grass','Normal','Psychic', 'Fire', 'Ground'], 
                            values=[110,90,80,80,70,60])])
        # Define hover info, text size, pull amount for each pie slice, and stroke
        fig2.update_traces(hoverinfo='label+percent', textfont_size=15,
                        textinfo='label+percent', pull=[0.1, 0, 0.2, 0, 0, 0],
                        marker=dict(colors=colors, line=dict(color='yellow', width=2)))
        fig2.update_layout(template= selected_template.value)


        solara.Markdown(f"#### Customize pie chart")
        solara.Markdown("""
                        ```python
                            # Customize pie chart
                            colors = ['blue', 'green', 'black', 'purple', 'red', 'brown']
                            fig2 = go.Figure(data=[go.Pie(labels=['Water','Grass','Normal','Psychic', 'Fire', 'Ground'], 
                                                values=[110,90,80,80,70,60])])
                            # Define hover info, text size, pull amount for each pie slice, and stroke
                            fig2.update_traces(hoverinfo='label+percent', textfont_size=15,
                                            textinfo='label+percent', pull=[0.1, 0, 0.2, 0, 0, 0],
                                            marker=dict(colors=colors, line=dict(color='yellow', width=2)))
                        ```
                        """
                        )
        solara.FigurePlotly(fig2)
    return main

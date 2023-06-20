import solara

selected_template = solara.reactive("plotly")
def change_theme(e):
    print (selected_template.value)
templates =["plotly", "plotly_white", "plotly_dark", "ggplot2", "seaborn", "simple_white", "none"]


@solara.component
def SharedSidebar():
    with solara.Card("Solara + Plotly Graphs", style={"max-width": "500px"}):
        solara.Markdown(
            f"""
            ###This project utilizes the Solara Framework to create interactive graphs using Plotly.
            *The code and examples in this project are based on the Plotly tutorial by Derek Banas.* 
            *Please refer to his repository for the original tutorial [here](https://github.com/derekbanas/plotly-tutorial/blob/master/Plotly%20Tut.ipynb)*
            """
        )
    with solara.Card(style={"max-width": "500px"}):
        solara.Select(label="Themes", value=selected_template, values=templates, on_value=change_theme)

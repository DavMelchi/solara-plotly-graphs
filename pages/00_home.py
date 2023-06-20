from typing import Optional, cast
import pandas as pd
import os
import solara
from solara.components.file_drop import FileDrop
from lat_lon_parser import parse,to_str_deg_min_sec


class State:
    options = ["Decimal", "Deg_Min_Sec"]
    option = solara.reactive("")
    df = solara.reactive(cast(Optional[pd.DataFrame], None))
    dff = solara.reactive(cast(Optional[pd.DataFrame], None))
    latitude = solara.reactive(cast(Optional[str],""))
    longitude = solara.reactive(cast(Optional[str],""))
    extension_check = solara.reactive(True)
    error_message = solara.reactive("")

    @staticmethod
    def load_from_file(file):
        file_name, file_extension = os.path.splitext(file["name"])
        if file_extension == ".csv":
            df = pd.read_csv(file["file_obj"], encoding='latin-1')
            State.df.value = df
            State.extension_check.value = True
            State.reset_vars()
        else:
            State.extension_check.value = False
            State.df.value = None
            State.reset_vars()

    def reset_vars():
        State.latitude.value = str("")
        State.longitude.value = str("")
        State.option.value = str("")
        State.error_message.value =str("")

    @staticmethod
    def convert ():
        State.error_message.value =""
        try :        
            df = State.df.value
            df['converted_latitude'] = df.loc[:, str(State.latitude.value)]
            df['converted_longitude'] = df.loc[:, str(State.longitude.value)]
            if State.option.value =="Decimal":
                df['converted_longitude'] =df['converted_longitude'].str.replace('O','W')
                df["converted_latitude"] =df["converted_latitude"].apply(parse)
                df["converted_longitude"] =df["converted_longitude"].apply(parse)
            elif State.option.value =="Deg_Min_Sec":
                df["converted_latitude"] =df["converted_latitude"].apply(to_str_deg_min_sec)
                df["converted_longitude"] =df["converted_longitude"].apply(to_str_deg_min_sec)
                df["converted_latitude"] =df["converted_latitude"].apply(lambda x: x.replace("-", "") + "S" if "-" in x else x + "N")
                df["converted_longitude"] =df["converted_longitude"].apply(lambda x: x.replace("-", "") + "W" if "-" in x else x + "E")
        except Exception as es:
            State.error_message.value = f"An error occurred. Please check your latitude and longitude format and ensure the correct conversion format ({es})"
        else :
            State.df.value = None
            State.df.value = df
            State.dff.value  = State.df.value
            
@solara.component
def Page():
    df = State.df.value
    
    solara.Title("GPS Coordinates Converter")
    
    with solara.Sidebar():
        with solara.Column():
            FileDrop(on_file=State.load_from_file, on_total_progress=lambda *args: None, label="Drag your file CSV here")
            
            if State.extension_check.value is not True :
                solara.Warning("Only CSV file are allowed")
            else :
                if df is not None:
                    columns = list(map(str, df.columns))
                    solara.Select("Latitude", values=columns, value=State.latitude)
                    solara.Select("Longitude", values=columns, value=State.longitude)
                    solara.Select("Convert To", values=State.options, value=State.option)
                    
                    if State.longitude.value =="" or State.latitude.value == "" or State.option.value == "":
                        solara.Info("Select Coordinates Columns and Ouput Format")
                    else :
                        solara.Button("Convert", color="primary", text=True, outlined=True, on_click=State.convert)
                        if State.dff.value is not None:
                            def get_data():
                                return State.dff.value.to_csv(index=False)
                            solara.FileDownload(get_data, label=f"Download {len(State.dff.value):,} converted coordinates", filename="converted.csv",)


    if State.df.value is not None:
        with solara.Column():
            solara.DataFrame(State.df.value)
            if State.error_message.value != "":
                solara.Warning(State.error_message.value)
    else:
        solara.Info("Waiting for Data, Please upload a file.")

@solara.component
def Layout(children):
    route, routes = solara.use_route()
    return solara.AppLayout(children=children)
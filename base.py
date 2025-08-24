import streamlit as st
st.set_page_config(page_title="stressforecast",page_icon="logo-removebg-preview.png",layout="centered")
from streamlit_option_menu import option_menu
import stressprediction,stresslevels,heartstatistics,about,contact
class Sidebar:
    def __init__(self):
        self.apps=[]
    def add_app(self,title,function):
        self.apps.append({
            "title":title,
            "function":function
        })
    def run():
        with st.sidebar:
            app=option_menu(
                menu_title="Health Statistics",
                options=["Home","Stress Levels","Statistics","About","Contact"],
                default_index=0,
            )
        if(app=="Home"):
            stressprediction.app()
        if(app=="Stress Levels"):
            stresslevels.app()
        if(app=="Statistics"):
            heartstatistics.app1()
        if(app=="About"):
            about.app()
        if(app=="Contact"):
            contact.app()
    run()

            


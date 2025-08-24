import streamlit as st
import numpy as np 
import pandas as pd
def app():
    col1,col2=st.columns(2)
    #Low
    h1="""<b><p style='text-align:center'>Low level Stress Range Chart</p><b>"""
    col1.markdown(h1,unsafe_allow_html=True)
    #col1.write("Low level Stress Range Chart")
    data1={"name":["Snoring","Respiration","Temperature","Limb Movement","Oxygen","Eye Movement","Sleeping","Heart"],"Range":[45,17,97,5,96,70,8,53]}
    data1=pd.DataFrame(data1)
    data1=data1.set_index("name")
    col1.bar_chart(data1,color="#FF0000")
    #Medium low
    h2="""<b><p style='text-align:center'>Medium Low level Stress Range Chart</p></b>"""
    col2.markdown(h2,unsafe_allow_html=True)
    #col2.write("Medium Low level Stress Range Chart")
    data2={"name":["Snoring","Respiration","Temperature","Limb Movement","Oxygen","Eye Movement","Sleeping","Heart"],"Range":[55,19,95,9,93,83,6,57]}
    data2=pd.DataFrame(data2)
    data2=data2.set_index("name")
    col2.bar_chart(data2,color="#00FF00")
    #Medium
    col3,col4=st.columns(2)
    h3="""<b><p style='text-align:center'>Medium level Stress Range Chart</p></b>"""
    col3.markdown(h3,unsafe_allow_html=True)
    #col3.write("Medium Level Stress Range Chart")
    data3={"name":["Snoring","Respiration","Temperature","Limb Movement","Oxygen","Eye Movement","Sleeping","Heart"],"Range":[70,21,93,11,91,90,1,70]}
    data3=pd.DataFrame(data3)
    data3=data3.set_index("name")
    col3.bar_chart(data3,color="#0000FF")
    #Medium High
    h4="""<b><p style='text-align:center'>Medium High level Stress Range Chart</p></b>"""
    col4.markdown(h4,unsafe_allow_html=True)
    #col4.write("Medium High level Stress Range Chart")
    data4={"name":["Snoring","Respiration","Temperature","Limb Movement","Oxygen","Eye Movement","Sleeping","Heart"],"Range":[85,23,91,15,89,99,1,70]}
    data4=pd.DataFrame(data4)
    data4=data4.set_index("name")
    col4.bar_chart(data2,color="#800080")


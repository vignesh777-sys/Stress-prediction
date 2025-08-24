import streamlit as st
import pandas as pd
import stresslevels as stress
import altair as alt
gsr=grr=gbt=glm=gbo=gem=gsh=ghr=0;
glabel="";
def app(predicted_stress_label,sr,rr,bt,lm,bo,em,sh,hr):
    global gsr;
    gsr=sr;
    global grr;
    grr=rr;
    global gbt;
    gbt=bt;
    global glm;
    glm=lm;
    global gbo;
    gbo=bo;
    global gem;
    gem=em;
    global gsh;
    gsh=sh;
    global ghr;
    ghr=hr;
    global glabel;
    glabel=predicted_stress_label
    
def app1():
    habits=["Continue a balanced diet, regular exercise, and sufficient sleep to keep stress levels low.","Simple deep breathing exercises can help manage mild stress. Focus on slow, deep breaths to calm the mind."," Incorporate mindfulness practices or meditation into your daily routine to help manage moderate stress.","More intense physical activity, such as running or cycling, can help burn off stress hormones and improve mood.","Consider seeking help from a therapist or counselor if stress becomes overwhelming and starts to interfere with daily life​."]
    diet=["Maintain a diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats.","Maintain a diet rich in fruits, vegetables, whole grains, lean proteins, and healthy fats.","Include berries, dark chocolate, and green tea to help combat oxidative stress.","Ensure adequate protein intake with foods like chicken, tofu, beans, and eggs to support energy levels and muscle repair.","Focus on nutrient-dense foods like leafy greens, nuts, seeds, and lean proteins to support overall health and resilience."]
    # levels=[gsr,grr,gbt,glm,gbo,gem,gsh,ghr]
    h1="""<b><p style='text-align:center'>Stress Statistics</p><b>"""
    st.markdown(h1,unsafe_allow_html=True)
    data={"name":["Snoring","Respiration","Temperature","Limb Movement","Oxygen","Eye Movement","Sleeping","Heart"],"Range":[gsr,grr,gbt,glm,gbo,gem,gsh,ghr]}
    data=pd.DataFrame(data)
    data=data.set_index("name")
    st.bar_chart(data,color="#00FF00")
    st.markdown("""<h1 style='text-align:center;color:yellow'>Remarks</h1>""",unsafe_allow_html=True)
    if(glabel=="Low/Normal"):
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><li>{habits[0]}</li><li>{diet[0]}</li><p>visit for more info: <a href="https://www.verywellmind.com/tips-to-reduce-stress-3145195">Verywell Mind</a></p></div>""",unsafe_allow_html=True)
    elif(glabel=="Medium Low"):
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><li>{habits[1]}</li><li>{diet[1]}</li><p>visit for more info: <a href="https://www.mayoclinic.org/healthy-lifestyle/stress-management/basics/stress-relief/hlv-20049495">Mayo Clinic</a></p></div>""",unsafe_allow_html=True)
    elif(glabel=="Medium"):
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><li>{habits[2]}/</li><li>{diet[2]}</li><p>visit for more info: <a href="https://health.clevelandclinic.org/how-to-relieve-stress">Cleveland Clinic</a></p></div>""",unsafe_allow_html=True)
    elif(glabel=="Medium High"):
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><li>{habits[3]}</li><li>{diet[3]}</li><p>visit for more info: <a href="https://www.verywellmind.com/tips-to-reduce-stress-3145195">https://www.mayoclinic.org/healthy-lifestyle/stress-management/in-depth/stress-relievers/art-20047257</a></p></div>""",unsafe_allow_html=True)
    elif(glabel=="High"):
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><li>{habits[4]}</li><li>{diet[4]}</li><p>visit for more info: <a href="https://health.clevelandclinic.org/how-to-relieve-stress">Cleveland Clinic</a></p></div>""",unsafe_allow_html=True)
    else:
        st.markdown(f"""<div style='padding:5px;width:90%;border:5px solid brown;margin:auto'><p>No Data Entered</p></div>""",unsafe_allow_html=True)
    
    # f=st.bar_chart(data,color="#00FF00")
    # """Generate a download link for a given chart."""
    # filename = "chart.png"
    # f.save(filename)
    # with open(filename, 'rb') as f:
    #     data = f.read()
    # href = f'<a href="data:image/png;base64,{data.decode()}" download="{filename}">Download Chart</a>'
    # res=b'stress.app()'
    # st.download_button(label="Download File",data=res,file_name="file.csv")
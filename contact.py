import streamlit as st
def app():
    st.markdown("""<h2 style='text-align:center;color:brown;'>Write Us</h2>""",unsafe_allow_html=True)
    form=st.form("form1")
    form.text_input("Name",key="1")
    form.text_input("Email",key="2")
    form.number_input("Mobile Number",key="3")
    form.text_area("Comments",key="4")
    form.form_submit_button("Submit")

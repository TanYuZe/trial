import streamlit as st
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from PIL import Image

wj_img = Image.open('wj.jpg')
ey_img = Image.open('ey.jpg')
xo_img = Image.open('xo.jpg')
zw_img = Image.open('zw.jpg')
st.markdown("",unsafe_allow_html=True)
def app():


    original_title = '<p style="font-family:Arial; font-size: 17px;"> Final Year Project - CSIT321-S4-G16 -  Web Service for Stock Market Prediction'
    st.markdown(original_title, unsafe_allow_html=True)

    original_title = '<p style="font-family:Arial; font-size: 17px;"> Supervisor: Mr Tan KT'
    st.markdown(original_title, unsafe_allow_html=True)

    original_title = '<p style="font-family:Arial; font-size: 17px;"> Assessor: Mr Tian SH'
    st.markdown(original_title, unsafe_allow_html=True)
    st.text("")


    original_title = '<p style="font-family:Arial; font-size: 20px; text-align: center;"> Meet the Team'
    st.markdown(original_title, unsafe_allow_html=True)
    st.text("")
    col1,col2 = st.columns(2)
    with col1:
        st.image(xo_img,width=100)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Name: Xavier Oh'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Course: Bachelor of Business Information System, Full Time'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Contact: xjhkoh002@mymail.sim.edu.sg'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Role: Project Manager'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Responsibilities: Testing, Documentation'
        st.markdown(original_title, unsafe_allow_html=True)
    with col2:
        st.image(wj_img,width = 100)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Name: Yao Wenjie'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Course: Bachelor of Computer Science (Big Data), Full Time'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Contact: wyao003@mymail.sim.edu.sg'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Role: Technical Team Lead'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Responsibilities: Application Development , Documentation'
        st.markdown(original_title, unsafe_allow_html=True)
    with col1:
        st.image(zw_img,width = 100)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Name: T. Zhen Wen'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Course: Bachelor of Computer Science (Cyber Security), Full Time'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Contact: zwtan016@mymail.sim.edu.sg'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Role: Design Team Lead'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Responsibilities: UI and UX Design, Documentation'
        st.markdown(original_title, unsafe_allow_html=True)
    with col2:
        st.image(ey_img,width = 100)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Name: Yap Guo Hui, Eric'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Course: Bachelor of Computer Science (Cyber Security), Full Time'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Contact: gheyeap001@mymail.sim.edu.sg'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Role: Quality Assurance Team Lead'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style="font-family:Arial; font-size: 17px;"> Responsibilities: Program Design, Documentation'
        st.markdown(original_title, unsafe_allow_html=True)

import streamlit as st
from PIL import Image
img = Image.open('icon.jpg')
st.set_page_config(page_title='SIMAISTOCK', page_icon=img)
from multiapp import MultiApp
from apps import about_us, stock_prediction, live_stock # import your app modules here
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
app = MultiApp()

st.markdown("""
# SIMAISTOCK
""")

# Add all your application here
app.add_app("Live Stock Data", live_stock.app)
app.add_app("Stock Prediction", stock_prediction.app)
app.add_app("About us", about_us.app)
# The main app
app.run()

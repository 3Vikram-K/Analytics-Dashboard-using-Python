import streamlit as st
from multiapp import MultiApp
from apps import builder, home, sales # import your app modules here

app = MultiApp()

#st.set_page_config(layout='wide',initial_sidebar_state='auto')
st.markdown("""
# Analytics Dashboard

A python Dashboard with inbuilt ML model builder.

""")

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Model Builder", builder.app)
app.add_app("Sales Dashboard",sales.app)
# The main app
app.run()

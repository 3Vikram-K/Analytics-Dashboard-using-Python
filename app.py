import streamlit as st
from multiapp import MultiApp
from apps import builder, dashboard # import your app modules here

app = MultiApp()



st.markdown("""
# Analytics Dashboard

A python Dashboard with inbuilt ML model builder.

""")

# Add all your application here
app.add_app("Dashboard", dashboard.app)
app.add_app("Model Builder", builder.app)
# The main app
app.run()

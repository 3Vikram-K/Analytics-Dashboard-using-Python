import streamlit as st
import pandas as pd
import plost

def app():
    #st.set_page_config(layout='wide', initial_sidebar_state='expanded')

    with open('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
    st.sidebar.header('NHCE')

    st.sidebar.subheader('Heat map parameter')
    time_hist_color = st.sidebar.selectbox('Color by', ('temp_min', 'temp_max')) 

    st.sidebar.subheader('Donut chart parameter')
    donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

    st.sidebar.subheader('Line chart parameters')
    plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
    plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)

    st.title(':house: Home')
    st.markdown('\n Home page of this dashboard.\n')
    st.markdown('---')
    # Row A
    st.markdown('### Metrics')
    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")
    st.markdown("##")

    # Row B
    seattle_weather = pd.read_csv('C:/3Vikram/Data/CODE/PROJECTS/Python/Mini_Project_4/Data/seattle.csv', parse_dates=['date'])
    stocks = pd.read_csv('C:/3Vikram/Data/CODE/PROJECTS/Python/Mini_Project_4/Data/stock.csv')

    c1, c2 = st.columns((7,3))
    st.markdown('##')
    with c1:
        st.markdown('### Heatmap')
        plost.time_hist(
        data=seattle_weather,
        date='date',
        x_unit='week',
        y_unit='day',
        color=time_hist_color,
        aggregate='median',
        legend=None,
        height=345,
        use_container_width=True)
    with c2:
        st.markdown('### Donut chart')
        plost.donut_chart(
            data=stocks,
            theta=donut_theta,
            color='company',
            legend='right', 
            use_container_width=False)

    # Row C
    st.markdown('### Line chart')
    st.line_chart(seattle_weather, x = 'date', y = plot_data, height = plot_height)
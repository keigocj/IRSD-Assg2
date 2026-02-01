import os
import streamlit as st #to input data into a local host, working directly on the browser
import pandas as pd  #pandas manipulates data as tables
import plotly.express as px  #plotly to manipulate the data in the tables
from apis import apod_generator

#in the terminal run: streamlit run dashboard.py
#if prompts you to enter email just press enter
#if streamlit not recognize run:
# python -m streamlit run dashboard.py
#API can be private - company; public - everyone has limited access; lincesed by subscription.


st.title("Water Quality  and NASA's APOD Dashboard")
st.header("Internship Ready Software Development")
st.write(
    "This Streamlit dashboard visualizes Biscayne Bay water quality data using Plotly charts "
    "and also demonstrates API integration by displaying NASA’s APOD."
)
#st.subheader("CS Cesar Calzadilla")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")


#this is a method that expect a list of labels
tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2D plots",
     "3D plots",
     "NASA's APOD"]
)

with tab1:
    #st.info("Working on this!")
    st.header("Biscayne Water Quality")
    st.write(
        "This section shows the raw Biscayne Bay dataset and summary statistics "
        "to help you understand the overall range, average, and variability of each measurement."
    )
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")


with tab2:
    #st.info("Be patient!")
    # fig1 = px.line(df,
    #                x= "Time",
    #                y= "Temperature (c)")
    # st.plotly_chart(fig1)
    #
    # fig2 = px.scatter(df,
    #                   x="ODO mg/L",
    #                   y="Temperature (c)",
    #                   color = "pH")
    # st.plotly_chart(fig2)


    st.header("2D Visualizations")
    st.write("Select which chart you want to view: ")

    st.write(
        "Use the dropdown to switch between two 2D visualizations. "
        "These plots help explore how temperature changes over time and how dissolved oxygen relates to temperature."
    )
    chart_type = st.selectbox(
        "Choose a chart",
        ["Temperature Over Time", "Oxygen vs. Temperature"]
    )

    if chart_type == "Temperature Over Time":
        fig1 = px.line(
            df,
            x= "Time",
            y= "Temperature (c)",
            title = "Water Temperature Over Time",
            labels={
                "Time" : "Time",
                "Temperature (c)": "Temperature (C)"
            }
        )

        st.plotly_chart(fig1)

    elif chart_type == "Oxygen vs. Temperature":

        fig2 = px.scatter(
            df,
            x= "ODO mg/L",
            y= "Temperature (c)",
            color = "pH",
            title = "Dissolved Oxygen vs. Temperature",
            labels={
                "ODO mg/L": "Dissolved Oxygen mg/L",
                "Temperature (c)" : "Temperature (C)",
                "pH" : "pH Level"
            }
        )

        st.plotly_chart(fig2)

with tab3:
    #st.info("It's worth the wait!")
    st.write(
        "This 3D plot maps location (latitude/longitude) against water column depth, "
        "with color showing temperature. Rotate/zoom to explore patterns across the bay."
    )
    fig3 = px.scatter_3d(
        df,
        x="Longitude",
        y="Latitude",
        z="Total Water Column (m)",
        color="Temperature (c)",
        title="3D View: Water Column Depth by Location",
        labels={
            "Longitude": "Longitude",
            "Latitude": "Latitude",
            "Total Water Column (m)": "Total Water Column (m)",
            "Temperature (c)": "Temperature (°C)"
        }
    )
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)



with tab4:
    st.header("NASA's Astronomy Picture of the Day")
    st.write(
        "This section pulls NASA’s Astronomy Picture of the Day (APOD) from a public API "
        "and displays key metadata and the media content."
    )

    #TODO: call a function that generates the APOD
    response = apod_generator("https://api.nasa.gov/planetary/apod?api_key=", os.getenv("NASA_API_KEY"))

    #TODO: using the streamlit methods
    # display the APOD image and title and other features

    st.subheader("Features")
    st.dataframe(response)
    st.caption("APOD's Image:")
    st.image(response["url"])






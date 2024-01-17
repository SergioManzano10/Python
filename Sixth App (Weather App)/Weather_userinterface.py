import streamlit as st
import plotly.express as px # To import the module express of plotly
from Weather_backend import get_data


# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")

place = st.text_input("City: ")
days = st.slider("Forecast Days", min_value = 1, max_value = 5, help = "Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")

if place: # It allows to execute the function pnly if a place is entered, avoiding the first error

    # Get the temperature/sky data
    try: 
        filtered_data = get_data(place, days)


        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data] # / 10 to show the temperature in a correct format (Celsius)
            dates = [dict["dt_txt"] for dict in filtered_data]
            # Create a temperature plot (for temperature)
            figure = px.line(x = dates , y = temperatures, labels = {"x": "Date", "y": "Temperature (Celsius)"}) # To plot a line in the graph
            st.plotly_chart(figure)

        if option == "Sky":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data] # We have to add [0] because weather is a list that contains a dictionary inside
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png", "Snow": "images/snow.png"} # Create a dictionary with the routes depending on the weather
            image_paths = [images[condition] for condition in sky_conditions]
            # Create a image set (for sky)
            st.image(image_paths, width=115)

    except KeyError:
        st.write("This place does not exist.")
# Water Quality and NASA APOD Dashboard

## Overview
This project is an interactive Streamlit web application developed for the
Internship Ready Software Development (IRSD) course.

The dashboard visualizes Biscayne Bay water quality data using Plotly charts and
demonstrates API integration by displaying NASA’s Astronomy Picture of the Day (APOD).

## Features
- Displays raw water quality data and descriptive statistics
- Interactive 2D and 3D visualizations using Plotly
- Dropdown menu to switch between charts
- Integration with NASA APOD public API
- Organized interface using Streamlit tabs

## Dataset
The application uses a CSV file containing Biscayne Bay water quality measurements,
including:
- Latitude and longitude
- Temperature
- Dissolved oxygen
- pH level
- Water column depth
- GPS data

Source file: `biscayneBay_waterquality.csv`

## Technologies Used
- Python
- Streamlit
- Pandas
- Plotly
- Requests
- Python-dotenv

## Installation and Setup

### 1. Clone the Repository
git clone https://github.com/keigocj/IRSD.git
cd IRSD

### 2. Install the dependencies
pip install -r requirements.txt

### 3. Set up a NASA API key
create a .env file and add
NASA_API_KEY = your_api_key

### 4. RUN THE APP!


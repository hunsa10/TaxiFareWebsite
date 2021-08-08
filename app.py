import streamlit as st
import datetime
import requests

'''
# TaxiFareModel
Creates a simple streamlit website to predict taxi fare from pickup and dropoff
input. (Prediction model code from TaxiFareModel)
'''

st.markdown('''
Predict your taxi fare!
''')


# Pickup datetime
pickup_date = st.date_input('What date is your trip?',
                            datetime.date(2021, 1, 1))

pickup_time = st.time_input('What time is your trip?',
                            datetime.time(9, 0, 0))

pickup_datetime = f'{pickup_date} {pickup_time}'

# Pickup long and lat
pickup_longitude = st.number_input('Pickup longitude', 0)

pickup_latitude = st.number_input('Pickup longitude', 1)

# Dropoff long and lat
dropoff_longitude = st.number_input('Dropoff longitude', 0)

dropoff_latitude = st.number_input('Dropoff longitude', 1)

# Passenger count
passenger_count = st.number_input('Passenger_count', 1)


# Call API to retrieve the price prediction

url = 'https://taxifare.lewagon.ai/predict'

params = {'pickup_datetime': pickup_datetime,
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count
          }

response = requests.get(url, params)

prediction = response.json()['prediction']

st.write(f'Your fare is: ${round(prediction, 2)}')

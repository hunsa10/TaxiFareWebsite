import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Predict your taxi fare!
''')

# Here we would like to add some controllers in order to ask the user to
# select the parameters of the ride
# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count


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


# Once we have these, let's call our API in order to retrieve a prediction
# See ? No need to load a `model.joblib` file in this app, we do not even need
# to know anything about Data Science in order to retrieve a prediction...
# 🤔 How could we call our API ? Off course... The `requests` package 💡


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

# 2. Let's build a dictionary containing the parameters for our API...
# 3. Let's call our API using the `requests` package...
# 4. Let's retrieve the prediction from the **JSON** returned by the API...
# Finally, we can display the prediction to the user

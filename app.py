import streamlit as st
import datetime
import requests


# Title
st.markdown("""# greenlima Taxifare4u""")

# Panel
d = st.date_input("Date",
                  datetime.date(2016, 7, 6))
st.write('Date:', d)

pickup_long = st.text_input('Pick-up longitude', '-73.950655')
st.write('Pickup longitude:', pickup_long)

pickup_lat = st.text_input('Pick-up latitude', '40.783282')
st.write('Pickup latitude:', pickup_lat)

dropoff_long = st.text_input('Drop-off longitude', '-73.950655')
st.write('Drop-off longitude:', dropoff_long)

dropoff_lat = st.text_input('Drop-off latitude', '40.783282')
st.write('Drop-off latitude:', dropoff_lat)

pass_count = st.number_input('Passenger count')
st.write('Passenger count ', pass_count)

# API endpoint
url = 'https://taxifare-qlahvylymq-ew.a.run.app/predict'
params = {'pickup_datetime': d,
          'pickup_longitude': pickup_long,
          'pickup_latitude': pickup_lat,
          'dropoff_longitude': dropoff_long,
          'dropoff_latitude': dropoff_lat,
          'passenger_count': pass_count}

# Button
if st.button('Calculate Fare'):
    # print is visible in the server output, not in the page
    print('button clicked!')
    ## Finally, we can display the prediction to the user
    response = requests.get(url, params).json()
    fare = round(response['fare_amount'], 2)
    st.metric("Fare", f'${fare}')
else:
    st.write('I was not clicked 😞')

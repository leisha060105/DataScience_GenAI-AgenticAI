import streamlit as st
import numpy as np
import pandas as pd

# App title and description
st.title("My First Streamlit App")
st.write("This is a simple app to demonstrate Streamlit's capabilities.")

#Interactive Widegets in sidebar
st.sidebar.header("User Input Features")

#Text input
user_name = st.sidebar.text_input("What is your name?", "Leisha Vishwanath")

#Slider input
age = st.sidebar.slider("Select your age", 0, 100, 25)

#Selectbox input
favorite_color = st.sidebar.selectbox("Select your favorite color", ["Red", "Green", "Blue", "Yellow"])

#Main Page Content
st.header(f"Welcome, {user_name}!")
st.write(f"Your age is {age} and your favorite color is {favorite_color}.")

#Displaying data
st.subheader("Here is some random data:")

#Create a random dataframe
data = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

st.dataframe(data)

#Checkbox to show/hide data
if st.checkbox("Show raw data"):
    st.subheader("Raw Data")
    st.write(data)

#Button to trigger an action
if st.button("Say hello"):
    st.write("Hello there!")
else:
    st.write("Goodbye!")
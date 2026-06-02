#import the streamlit library
import streamlit as st

#Add a title to the app
st.title("My First Streamlit App created by Leisha Vishwanath")

#Add some text
st.write("Welcome! This app calculates the square of a number.")

# Create an interacting slider
st.header("Select the number")
number = st.slider("Choose a number", 0, 50, 3) #min, max, default

#Calculate and display the result
st.subheader("Result")
squared_number = number * number
st.write(f"The square of {number} is {squared_number}.")

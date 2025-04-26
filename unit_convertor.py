import streamlit as st       # streamlit  is a Liabrary for building web apps

# function to convert units based on predefined conversion factors or formulas
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams ": 1000
    }

    key = f"{unit_from}_{unit_to}"

    #Logic to convert units
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported" # return a message if the conversion is not supported

# 👇 Streamlit UI code (outside the function)
st.title("Unit Converter")  #set the title of the web apps

# user input: numerical value to convert
value = st.number_input("Enter the value:", min_value=1.0,step=1.0)

#dropdown to select unit to convert from
unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])

#dropdown to select unit to convert from
unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

#button to trigger the conversion
if st.button("Convert"):

    # call the conversion function
    result = convert_units(value, unit_from, unit_to)

    #display the result
    st.write(f"Converted value: {result}")

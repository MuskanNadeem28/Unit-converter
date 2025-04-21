import streamlit as st

def convert_units(value, unit_from, unit_to):
    # Conversion rates between units
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
    }

    # Create the key to match the conversion
    key = f"{unit_from}_{unit_to}"

    # Check if the conversion is in the dictionary
    if key in conversions:
        conversion = conversions[key]
        return value * conversion
    else:
        return "Conversion not supported"

# Streamlit interface
st.title("Unit Converter")

# Input for the value
value = st.number_input("Enter the value:")

# Dropdown for unit selection
unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

# Button to trigger conversion
if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.write(f"Converted value: {result}")

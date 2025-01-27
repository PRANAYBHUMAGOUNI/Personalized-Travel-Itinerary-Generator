import streamlit as st
import openai

# Setting OpenAI API key here
openai.api_key = 'provide API Key here'
# Function to generate itinerary based on user inputs
def generate_itinerary(budget, duration, destination, purpose, preferences):
    # Constructing the prompt for OpenAI's GPT model
    prompt = f"""
    You are an AI travel planner. Generate a detailed travel itinerary for the following user preferences:

    - Budget: {budget}
    - Duration: {duration} days
    - Destination: {destination}
    - Purpose of Trip: {purpose}
    - Preferences: {preferences}

    Please provide a day-by-day itinerary including activities, dining options, and accommodations.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("Personalized Travel Itinerary Generator")

# User Inputs
budget = st.text_input("What is your budget for the trip?")
duration = st.text_input("How many days do you plan to travel?")
destination = st.text_input("Where would you like to go?")
purpose = st.text_input("What is the main purpose of your trip (e.g., leisure, business)?")
preferences = st.text_area("Do you have any specific interests or preferences for activities?")

# Generating Itinerary Button
if st.button("Generate Itinerary"):
    if budget and duration and destination and purpose:
        itinerary = generate_itinerary(budget, duration, destination, purpose, preferences)
        st.subheader("Your Travel Itinerary:")
        st.write(itinerary)
    else:
        st.error("Please fill in all fields.")


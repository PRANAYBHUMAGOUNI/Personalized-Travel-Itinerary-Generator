# Personalized-Travel-Itinerary-Generator

## Overview

The Personalized Travel Itinerary Generator is a web application designed to create customized travel itineraries using OpenAI's GPT model. The application uses Streamlit for an intuitive and interactive user interface, allowing users to enter their travel preferences and receive detailed itineraries based on their inputs.

## Features

- Collects user inputs including budget, trip duration, destination, trip purpose, and specific preferences.
- Utilizes OpenAI's GPT to generate a personalized, day-by-day travel itinerary.
- Presents the generated itinerary in a clear and user-friendly format via Streamlit.

## Requirements

- **Python**: Version 3.7 or later.
- **OpenAI API Key**: Obtain a key from [OpenAI](https://beta.openai.com/signup/).

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/PRANAYBHUMAGOUNI/Personalized-Travel-Itinerary-Generator
    cd travel_itinerary_app.py
    ```

2. **Install Dependencies**:
    ```bash
    pip install streamlit openai
    ```

3. **Set Up OpenAI API Key**:
   Replace `'your-openai-api-key'` in the script with your actual OpenAI API key. You can add this in a configuration file or directly in the code as needed.

4. **Run the Application**:
    ```bash
    streamlit run travel_itinerary_app.py
    ```

## Usage

1. After running the application, open the given local URL in your web browser.
2. Enter the required travel details in the provided input fields:
   - Budget
   - Duration
   - Destination
   - Purpose of the trip
   - Preferences
3. Click "Generate Itinerary" to create your personalized travel plan.
4. The application will display a detailed itinerary based on your inputs.

   ![image](https://github.com/user-attachments/assets/8fc3b5c6-8020-430b-b301-afe1911b02ba)


## Development Approach

- **User-Friendly Interface**: Streamlit was chosen for its simplicity and ease of use in creating web applications.
- **Effective AI Integration**: The application uses carefully crafted prompts to interact with OpenAI's model for generating relevant outputs.
- **Flexibility**: Designed to handle various travel scenarios, making it adaptable for different user needs.

## Limitations

- The effectiveness of the generated itinerary is dependent on the input quality and detail provided by users.
- Usage of the OpenAI API is subject to token limits; ensure that your key has sufficient quota.


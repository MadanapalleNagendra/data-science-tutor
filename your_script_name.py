import streamlit as st
import google.generativeai as ai
import os

# Step 1: Configure the Google Generative AI API
# Replace "GEMINI_API_KEY with your actual API key
api_key = os.getenv("GEMINI_API_KEY") or "GEMINI_API_KEY"
ai.configure(api_key=api_key)

# Step 2: Define the system prompt for the AI model
sys_prompt = """
You are a helpful AI Tutor for Data Science. 
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible. 
Make sure to take examples while explaining a concept.
In case if a student asks any question outside the data science scope, 
politely decline and tell them to ask the question from the data science domain only.
Always include a helpful statement.
"""

# Step 3: Initialize the Gemini model
gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

# Step 4: Streamlit app layout
st.title("Data Science/AI TUTOR")

# User input area
user_input = st.text_area(label="Enter your query/issue", placeholder="Explain the concept of for loops")

# Button to submit the query
btn_click = st.button("Get Answer")

# Step 5: Process the query when the button is clicked
if btn_click and user_input.strip():
    with st.spinner("Generating response..."):
        try:
            # Generate a response using the Gemini model
            response = gemini_model.generate_content(user_input)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
elif btn_click and not user_input.strip():
    st.warning("Please enter a query before clicking the button.")

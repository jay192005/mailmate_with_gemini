import streamlit as st
import google.generativeai as genai

# Configure the Gemini API with the secret key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

def generate_email_response(email_text, tone):
    # Initialize the Gemini model. 
    # 'gemini-1.5-flash' is the latest fast and efficient model.
    model = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f"""
You are an AI assistant. Write a reply to the following email using a {tone.lower()} tone:

Email:
{email_text}

Reply:
"""
    # Generate content using the new API
    response = model.generate_content(prompt)
    
    # Return the generated text from the response
    return response.text
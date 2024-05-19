import streamlit as st
import subprocess
import os
from pathlib import Path
from streamlit_lottie import st_lottie
import sys
# Utility function to load Lottie animations from URL
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load an animation for the header
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

# Set page configuration
st.set_page_config(page_title="Autopy", page_icon=":sparkles:", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: grey;
        font-family: 'Arial', sans-serif;
        padding: 2rem;
    }
    h1 {
        color: #6c63ff;
        text-align: center;
        font-weight: bold;
    }
    .description {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 2rem;
    }
    .button-container {
        display: flex;
        justify-content: center;
        margin-top: 2rem;
    }
    .button-container button {
        background-color: #6c63ff;
        color: white;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .button-container button:hover {
        background-color: #574bff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1>Python to Executable Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='description'>Convert your Python scripts (.py) to standalone executables (.exe) with ease using auto-py-to-exe. Developed by SKAV TECH, A company focuses on Building Practial AI projects</p>", unsafe_allow_html=True)

# Instructions for users
st.markdown("""
1. Click the button below to install `auto-py-to-exe`.
2. Follow the instructions in the auto-py-to-exe GUI to complete your conversion.
3. Once the conversion is done, download your executable from the `dist` directory.
""")

# Button to start the installation and open auto-py-to-exe
if st.button("Start Conversion Process"):
    with st.spinner("Setting up the environment..."):
        # Install auto-py-to-exe
        subprocess.run([sys.executable, "-m", "pip", "install", "auto-py-to-exe"], capture_output=True, text=True)
        st.success("auto-py-to-exe installed successfully!")

        # Provide instructions to the user
        st.write("The `auto-py-to-exe` GUI will open automatically. Follow these steps:")
        st.write("1. In the `Script Location` field, select the Python file you want to convert.")
        st.write("2. Customize the settings as needed.")
        st.write("3. Click on `Convert .py to .exe` to start the conversion.")
        st.write("4. Once the conversion is done, download your executable from the `dist` directory.")

        # Open auto-py-to-exe GUI
        subprocess.Popen(["auto-py-to-exe"], shell=True)

# Clean up temporary files (optional)
if st.button("Clean up temporary files"):
    temp_dir = "temp"
    if os.path.exists(temp_dir):
        for file_name in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(temp_dir)
        st.success("Temporary files cleaned up successfully.")
    else:
        st.info("No temporary files to clean up.")

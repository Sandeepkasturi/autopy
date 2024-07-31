import streamlit as st
import subprocess
import sys
import os
import zipfile
import tempfile

# Utility function to load Lottie animations from URL
def load_lottieurl(url: str):
    import requests
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Function to save uploaded files to a temporary directory
def save_uploaded_files(uploaded_file):
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return file_path

# Function to extract a zip file
def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

# Function to run auto-py-to-exe
def run_auto_py_to_exe(executable_path):
    # Attempt to run auto-py-to-exe
    result = subprocess.run([sys.executable, executable_path], shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        st.success("auto-py-to-exe executed successfully!")
        st.write("Follow the instructions in the auto-py-to-exe GUI to complete your conversion.")
    else:
        st.error("Failed to execute auto-py-to-exe.")
        st.error(result.stderr)

# Set page configuration
st.set_page_config(page_title="Autopy", page_icon=":sparkles:", layout="centered")

# Load an animation for the header
lottie_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Arial', sans-serif;
        padding: 2rem;
    }
    h1 {
        color: #bb86fc;
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
        background-color: #bb86fc;
        color: #121212;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .button-container button:hover {
        background-color: #a03dbe;
    }
    .output {
        margin-top: 2rem;
        background-color: #1f1f1f;
        color: #e0e0e0;
        padding: 1rem;
        border-radius: 5px;
    }
    .error {
        color: #cf6679;
    }
    .info {
        color: #03dac6;
    }
    .warning {
        color: #ffab00;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.markdown("<h1>Python to Executable Converter</h1>", unsafe_allow_html=True)
st.markdown("Developed by SKAV TECH a Company focused on Building Practical AI Projects.")
st.markdown("<p class='description'>Convert your Python scripts (.py) to standalone executables (.exe) with ease using auto-py-to-exe. Developed by SKAV TECH, A company focuses on Building Practical AI projects</p>", unsafe_allow_html=True)

# Instructions for users
st.markdown("""
1. Install `auto-py-to-exe` on your local machine.
2. Upload the necessary files using the file uploader below.
3. Type `auto-py-to-exe` in the command shell and execute.
""")

# File uploader for user to upload auto-py-to-exe files
uploaded_file = st.file_uploader("Upload auto-py-to-exe zip file", type=["zip"])

if uploaded_file is not None:
    # Save and extract the uploaded zip file
    zip_path = save_uploaded_files(uploaded_file)
    extract_to_dir = tempfile.mkdtemp()
    extract_zip(zip_path, extract_to_dir)

    st.success("Files uploaded and extracted successfully!")

    # Provide the path to the auto-py-to-exe executable
    auto_py_to_exe_path = os.path.join(extract_to_dir, 'auto-py-to-exe', 'auto_py_to_exe.py')  # Update this path as needed

    # Shell command input and execution
    st.markdown("<h2>Command Shell</h2>", unsafe_allow_html=True)
    command = st.text_input("Enter a shell command:")

    if st.button("Execute"):
        if command.strip().lower() == "auto-py-to-exe":
            run_auto_py_to_exe(auto_py_to_exe_path)
        else:
            st.warning("Please enter a valid command to execute.")
else:
    st.info("Please upload the `auto-py-to-exe` package to proceed.")

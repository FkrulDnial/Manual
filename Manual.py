import streamlit as st

st.set_page_config(page_title="Smart Access System Guide", page_icon="🔐", layout="centered")

st.title("🔐 Smart Access Control System")
st.subheader("📘 Setup & User Instructions")

# 📚 User Guide
with st.expander("📚 Guide"):
    st.markdown("""
    ### 📸 Register
    1. Enter full name & student ID.
    2. Take a clear photo with good lighting.
    3. Click **Register**.

    ### 🔐 Access
    1. Take a photo.
    2. Face will be recognized automatically.

    ---
    ⚠️ **Important Tips**
    - Only one face per photo.
    - Good lighting is crucial.
    """)

# 🛠️ Installation Guide
with st.expander("🛠️ Installation Guide"):
    st.markdown("""
    ### 💻 Local Setup

    #### Prerequisites
    - Python 3.8 or newer  
    - A webcam/camera  
    - Internet connection for Google Sheets  

    #### Step-by-Step Installation

    1. **Clone or download** this project to your computer

    2. **Create virtual environment:**
    ```bash
    python -m venv venv
    ```

    3. **Activate the virtual environment:**
    - **Windows:**
        ```bash
        venv\\Scripts\\activate
        ```
    - **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

    4. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

    5. **Set up Google Sheets credentials:**
    - Go to [Google Cloud Console](https://console.cloud.google.com/)
    - Create a new project or select existing one  
    - Enable Google Sheets API  
    - Create Service Account credentials  
    - Download the JSON file as `drive_credentials.json`  
    - Place it in your project root folder  

    6. **Update ESP32 IP address** in the code (line 365):
    ```python
    ESP32_URL = "http://YOUR_ESP32_IP/unlock"
    ```

    7. **Run the application:**
    ```bash
    streamlit run app.py
    ```

    ### 📋 requirements.txt Contents
    ```
    streamlit>=1.28.0
    face-recognition>=1.3.0
    numpy>=1.21.0
    requests>=2.28.0
    gspread>=5.7.0
    google-auth>=2.16.0
    pandas>=1.5.0
    Pillow>=9.0.0
    ```

    ### ⚠️ Important Notes
    - **Camera Access:** Ensure your browser allows camera access  
    - **Face Recognition:** Use clear, well-lit photos with only one face  
    - **Google Sheets:** Make sure your spreadsheet is shared with the service account email  
    - **ESP32 Connection:** Update the IP address to match your ESP32 device  
    - **Firewall:** Ensure your firewall allows the application to access the camera and network  

    ### 🔧 Troubleshooting
    - **Camera not working:** Check browser permissions and try refreshing  
    - **Google Sheets error:** Verify credentials file and API permissions  
    - **Face not detected:** Improve lighting and ensure face is clearly visible  
    - **ESP32 connection failed:** Check IP address and network connectivity  
    """)

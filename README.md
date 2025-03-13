Streamlit File Manager App
Streamlit
Python

This is a Streamlit-based File Manager App that allows users to:

Create and manage folders.

Upload images (PNG, JPG, JPEG, WEBP).

Automatically convert non-JPG images (e.g., PNG, WEBP) to JPG format.

Rename files using a customizable pattern.

View files in a selected folder with serial numbers.

The app is designed to be simple and user-friendly, with a sidebar interface for folder management and file uploads.

Features
Folder Management:

Create new folders.

Select existing folders to view or manage files.

File Upload:

Upload multiple images at once.

Supported formats: PNG, JPG, JPEG, WEBP.

File Conversion:

Automatically converts PNG and WEBP images to JPG format.

File Renaming:

Customizable renaming pattern (e.g., image_TIMESTAMP).

File Listing:

View files in the selected folder with serial numbers.

Prerequisites
Before running the app, ensure you have the following installed:

Python 3.7 or higher: Download and install Python from python.org.

Streamlit: Install Streamlit using pip:

bash
Copy
pip install streamlit
Pillow: Install Pillow for image processing:

bash
Copy
pip install Pillow
How to Run the App Locally
Clone the Repository:

bash
Copy
git clone https://github.com/your-username/streamlit-file-manager.git
cd streamlit-file-manager
Install Dependencies:
Ensure all dependencies are installed by running:

bash
Copy
pip install -r requirements.txt
Run the Streamlit App:
Start the app by running:

bash
Copy
streamlit run app.st12.py
Access the App:
Open your browser and go to the provided URL (e.g., http://localhost:8501).

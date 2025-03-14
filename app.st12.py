import os
import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime

# Set Correct Base Directory
#BASE_DIR = Path("DataSet")  # Ensure correct folder name
#BASE_DIR.mkdir(exist_ok=True)  # Create if it doesn't exist
# Use environment variable for dataset directory
BASE_DIR = Path(os.getenv("DATASET_DIR", "DataSet"))  # Fallback to "DataSet" if env variable is missing
BASE_DIR.mkdir(exist_ok=True)
# Streamlit UI
st.set_page_config(page_title="File Manager", layout="wide")

# Sidebar - Display Folder Structure
st.sidebar.header("📂 File Explorer")

def list_files(directory):
    """ List files in a directory. """
    if not directory.exists():
        return []
    return [item.name for item in directory.iterdir() if item.is_file()]

# Get folder list inside BASE_DIR
folder_list = [folder.name for folder in BASE_DIR.iterdir() if folder.is_dir()]
selected_folder = st.sidebar.selectbox("Select Folder", ["DataSet"] + folder_list)

# Create a new folder
new_folder = st.sidebar.text_input("📁 New Folder Name")
if st.sidebar.button("Create Folder"):
    new_folder_path = BASE_DIR / new_folder
    if not new_folder_path.exists():
        new_folder_path.mkdir()
        st.sidebar.success(f"Folder '{new_folder}' created!")
    else:
        st.sidebar.error("Folder already exists!")

# Upload Files
st.sidebar.header("📤 Upload Images")
uploaded_files = st.sidebar.file_uploader(
    "Drag and Drop Files Here", accept_multiple_files=True, type=["png", "jpg", "jpeg", "webp"]
)

# ✅ Ensure correct folder selection
selected_path = BASE_DIR if selected_folder == "DataSet" else BASE_DIR / selected_folder
selected_path.mkdir(exist_ok=True)  # Ensure folder exists

# Renaming Pattern
if "rename_pattern" not in st.session_state:
    st.session_state.rename_pattern = "image"

rename_pattern = st.sidebar.text_input("Set Rename Pattern", st.session_state.rename_pattern)
if st.sidebar.button("Apply Rename Pattern"):
    st.session_state.rename_pattern = rename_pattern
    st.sidebar.success(f"Pattern set to '{rename_pattern}_TIMESTAMP'")

# Convert Image to JPG
def convert_to_jpg(image_path):
    """ Convert PNG/WEBP images to JPG """
    img = Image.open(image_path)
    rgb_img = img.convert("RGB")  # Convert to RGB mode (JPG doesn't support transparency)
    new_path = image_path.with_suffix(".jpg")  # Change extension to .jpg
    rgb_img.save(new_path, format="JPEG", quality=90)
    return new_path.name  # Return new file name

# Save Uploaded Files & Convert
if uploaded_files:
    for file in uploaded_files:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{st.session_state.rename_pattern}_{timestamp}{Path(file.name).suffix}"
        file_path = selected_path / new_file_name

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Convert non-JPG files to JPG
        if file.name.lower().endswith(("png", "webp")):
            new_jpg_name = convert_to_jpg(file_path)
            os.remove(file_path)  # Remove original file
            st.sidebar.success(f"Converted {file.name} to {new_jpg_name}")

    st.sidebar.success("Files uploaded & renamed successfully!")

# ✅ File Listing
# ✅ File Listing with Serial Numbers
if selected_path.exists():
    st.subheader(f"📂 Viewing: {selected_folder}")
    files = list_files(selected_path)

    for idx, file in enumerate(files, start=1):
        st.write(f"**{idx}. {file}**")  # Display files with serial numbers
else:
    st.error(f"🚨 Folder '{selected_folder}' does not exist. Try creating it first.")

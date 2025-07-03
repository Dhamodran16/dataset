import os
import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime

# ✅ Set Base Directory in C:\ Drive (LOCAL ONLY)
BASE_DIR = Path("C:/") / "DataSet"
BASE_DIR.mkdir(parents=True, exist_ok=True)

# ✅ Streamlit UI
st.set_page_config(page_title="File Manager", layout="wide")
st.sidebar.header("📂 File Explorer")

# ✅ List files in a folder
def list_files(directory):
    return [item.name for item in directory.iterdir() if item.is_file()] if directory.exists() else []

# ✅ Get all folders inside BASE_DIR
folder_list = [folder.name for folder in BASE_DIR.iterdir() if folder.is_dir()]
selected_folder = st.sidebar.selectbox("Select Folder", ["DataSet"] + folder_list)

# ✅ Folder creation
new_folder = st.sidebar.text_input("📁 New Folder Name")
if st.sidebar.button("Create Folder"):
    new_folder_path = BASE_DIR / new_folder
    if not new_folder_path.exists():
        new_folder_path.mkdir(parents=True)
        st.sidebar.success(f"Folder '{new_folder}' created!")
    else:
        st.sidebar.error("Folder already exists!")

# ✅ File upload
st.sidebar.header("📤 Upload Images")
uploaded_files = st.sidebar.file_uploader(
    "Drag and Drop Files Here", accept_multiple_files=True, type=["png", "jpg", "jpeg", "webp"]
)

# ✅ Target path
selected_path = BASE_DIR if selected_folder == "DataSet" else BASE_DIR / selected_folder
selected_path.mkdir(parents=True, exist_ok=True)

# ✅ Rename pattern
if "rename_pattern" not in st.session_state:
    st.session_state.rename_pattern = "image"

rename_pattern = st.sidebar.text_input("Set Rename Pattern", st.session_state.rename_pattern)
if st.sidebar.button("Apply Rename Pattern"):
    st.session_state.rename_pattern = rename_pattern
    st.sidebar.success(f"Pattern set to '{rename_pattern}_TIMESTAMP'")

# ✅ Image conversion
def convert_to_jpg(image_path):
    img = Image.open(image_path).convert("RGB")
    new_path = image_path.with_suffix(".jpg")
    img.save(new_path, format="JPEG", quality=90)
    return new_path.name

# ✅ Save uploaded files
if uploaded_files:
    for file in uploaded_files:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{st.session_state.rename_pattern}_{timestamp}{Path(file.name).suffix}"
        file_path = selected_path / new_file_name

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        if file.name.lower().endswith(("png", "webp")):
            new_jpg_name = convert_to_jpg(file_path)
            os.remove(file_path)
            st.sidebar.success(f"Converted {file.name} to {new_jpg_name}")

    st.sidebar.success(f"✅ Files saved to: {selected_path}")

# ✅ File list view
if selected_path.exists():
    st.subheader(f"📂 Viewing: {selected_folder} (C:/DataSet/{selected_folder})")
    files = list_files(selected_path)
    for idx, file in enumerate(files, start=1):
        st.write(f"**{idx}. {file}**")
else:
    st.error("Folder does not exist.")

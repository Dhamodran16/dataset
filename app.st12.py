import os
import streamlit as st
from pathlib import Path
from PIL import Image
from datetime import datetime
import tempfile
import zipfile
from io import BytesIO

# ✅ Set Safe Base Directory (compatible with both local & Render)
if "RENDER" in os.environ:  # Render.com sets this env var
    BASE_DIR = Path(tempfile.gettempdir()) / "DataSet"
else:
    BASE_DIR = Path("DataSet")

BASE_DIR.mkdir(parents=True, exist_ok=True)  # Create if not exists

# ✅ Streamlit UI Config
st.set_page_config(page_title="File Manager", layout="wide")
st.sidebar.header("📂 File Explorer")

# ✅ Function to list files
def list_files(directory):
    return [item.name for item in directory.iterdir() if item.is_file()] if directory.exists() else []

# ✅ Folder selection
folder_list = [folder.name for folder in BASE_DIR.iterdir() if folder.is_dir()]
selected_folder = st.sidebar.selectbox("Select Folder", ["DataSet"] + folder_list)

# ✅ Folder creation
new_folder = st.sidebar.text_input("📁 New Folder Name")
if st.sidebar.button("Create Folder"):
    new_folder_path = BASE_DIR / new_folder
    if not new_folder_path.exists():
        new_folder_path.mkdir()
        st.sidebar.success(f"Folder '{new_folder}' created!")
    else:
        st.sidebar.error("Folder already exists!")

# ✅ File uploader
st.sidebar.header("📤 Upload Images")
uploaded_files = st.sidebar.file_uploader(
    "Drag and Drop Files Here", accept_multiple_files=True, type=["png", "jpg", "jpeg", "webp"]
)

# ✅ Ensure selected folder exists
selected_path = BASE_DIR if selected_folder == "DataSet" else BASE_DIR / selected_folder
selected_path.mkdir(parents=True, exist_ok=True)

# ✅ Renaming pattern
if "rename_pattern" not in st.session_state:
    st.session_state.rename_pattern = "image"

rename_pattern = st.sidebar.text_input("Set Rename Pattern", st.session_state.rename_pattern)
if st.sidebar.button("Apply Rename Pattern"):
    st.session_state.rename_pattern = rename_pattern
    st.sidebar.success(f"Pattern set to '{rename_pattern}_TIMESTAMP'")

# ✅ Image conversion to JPG
def convert_to_jpg(image_path):
    img = Image.open(image_path).convert("RGB")
    new_path = image_path.with_suffix(".jpg")
    img.save(new_path, format="JPEG", quality=90)
    return new_path.name

# ✅ File saving & conversion
if uploaded_files:
    for file in uploaded_files:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"{st.session_state.rename_pattern}_{timestamp}{Path(file.name).suffix}"
        file_path = selected_path / new_file_name

        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        # Convert to JPG if needed
        if file.name.lower().endswith(("png", "webp")):
            new_jpg_name = convert_to_jpg(file_path)
            os.remove(file_path)
            st.sidebar.success(f"Converted {file.name} to {new_jpg_name}")

    st.sidebar.success("Files uploaded & renamed successfully!")

# ✅ File listing with serial numbers
files = list_files(selected_path)
if selected_path.exists():
    st.subheader(f"📂 Viewing: {selected_folder}")
    for idx, file in enumerate(files, start=1):
        st.write(f"**{idx}. {file}**")
else:
    st.error(f"🚨 Folder '{selected_folder}' does not exist. Try creating it first.")

# ✅ Folder download as ZIP
if files:
    st.markdown("---")
    st.subheader("📦 Download Entire Folder")

    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for file in files:
            file_path = selected_path / file
            zip_file.write(file_path, arcname=file)

    zip_buffer.seek(0)
    st.download_button(
        label=f"⬇️ Download '{selected_folder}' Folder as ZIP",
        data=zip_buffer,
        file_name=f"{selected_folder}.zip",
        mime="application/zip"
    )

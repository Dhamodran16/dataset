<h1 align="center">
  <img src="https://i.ibb.co/6XZ5hV5/file-manager-icon.png" alt="File Manager Logo" width="150">
  <br>
  Streamlit File Manager App
  <br>
</h1>

<p align="center">
  A Streamlit-based File Manager App that allows users to:
  <br>
  ➤ Create and manage folders  
  ➤ Upload images (PNG, JPG, JPEG, WEBP)  
  ➤ Automatically convert to JPG  
  ➤ Rename using custom pattern  
  ➤ View files with serial numbers  
</p>

<p align="center">
  <a href="https://www.python.org">
    <img src="https://img.shields.io/badge/Python-3.9+-blue.svg?style=flat-square" alt="Python">
  </a>
  <a href="https://streamlit.io">
    <img src="https://img.shields.io/badge/Streamlit-1.x-red.svg?style=flat-square" alt="Streamlit">
  </a>
  <a href="https://pillow.readthedocs.io">
    <img src="https://img.shields.io/badge/Pillow-9.x-yellow.svg?style=flat-square" alt="Pillow">
  </a>
  <a href="https://github.com/your-username/streamlit-file-manager/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/your-username/streamlit-file-manager?style=flat-square" alt="License">
  </a>
</p>

---

## 🌟 Features

### 📁 Folder Management
- Create new folders
- Select existing folders to view/manage files

### 📤 File Upload
- Upload multiple images
- Supports PNG, JPG, JPEG, WEBP

### 🔁 File Conversion
- Auto converts PNG/WEBP to JPG after upload

### ✏️ File Renaming
- Rename files using a pattern like `image_TIMESTAMP.jpg`

### 📑 File Listing
- View all files in the folder
- Each file listed with serial number

---

## 🛠 Tech Stack

- **Python** – Core backend logic
- **Streamlit** – For the interactive UI
- **Pillow** – For image processing/conversion

---

## 📦 Prerequisites

Before running the app, make sure the following are installed:

- **Python 3.7 or higher**  
  👉 [Download Python](https://www.python.org/downloads/)

- **Streamlit**  
  ```bash
  pip install streamlit

Pillow

```pip install Pillow ```

🚀 How to Run the App Locally
1. Clone the Repository

git clone https://github.com/your-username/streamlit-file-manager.git


cd streamlit-file-manager


2. Install Dependencies

pip install -r requirements.txt


💡 Tip: It's recommended to use a virtual environment.

3. Run the App

streamlit run app.st12.py

🌐 Access the App


Once running, open your browser and go to:


http://localhost:8501

📸 Sample Screenshot

<p align="center"> <img src="https://i.ibb.co/vzTtNnL/full-interface.png" alt="Full Interface" width="750"> </p>


📂 Folder Structure


streamlit-file-manager/
│
├── app.st12.py               # Main Streamlit app
├── requirements.txt          # Python dependencies
└── uploads/                  # Upload folder (auto-created)

⚠️ Notes
The app auto-creates folders under /uploads/

Non-JPG files are auto-converted and renamed

Files are listed with their names and serial number

Files uploaded to the same folder will append, not overwrite


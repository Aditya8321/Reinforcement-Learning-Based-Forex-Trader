!pip install dotenv
import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv


# Step 1: Find project root dynamically (look for folder containing .env)
current_dir = os.getcwd()
project_root = current_dir

while not os.path.isfile(os.path.join(project_root, ".env")):
    # Go one directory up
    parent_dir = os.path.abspath(os.path.join(project_root, ".."))
    if parent_dir == project_root:
        raise FileNotFoundError(".env file not found in any parent directory")
    project_root = parent_dir

# Step 2: Load .env from project root
load_dotenv(os.path.join(project_root, ".env"))

# --- Page Config ---
st.set_page_config(
    page_title="Trading RL Report",
    layout="wide",
)

st.title("📊 Trading Reinforcement Learning Report")

# --- Helper function to display all images in a folder ---
def show_images(folder, title):
    if not os.path.exists(folder):
        st.warning(f"⚠️ Folder not found: {folder}")
        return
    
    st.header(title)
    image_files = [f for f in os.listdir(folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        st.info("No images found in this folder.")
        return
    
    # Display in a grid (3 per row)
    cols = st.columns(3)
    for i, img_file in enumerate(sorted(image_files)):
        img_path = os.path.join(folder, img_file)
        image = Image.open(img_path)
        with cols[i % 3]:
            st.image(image, caption=img_file, use_container_width=True)

# --- Show sections ---
show_images(os.getenv("EDA_IMG_PATH"), "📈 Exploratory Data Analysis")
show_images(os.getenv("MODEL_OUTPUT_IMG_PATH"), "🤖 Model Outputs")

st.markdown("---")
st.success("✅ Report generation complete. Use sidebar to navigate between sections if needed.")

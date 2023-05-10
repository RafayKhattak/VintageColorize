# Import required libraries
import io
import os
import streamlit as st
import requests
from PIL import Image
import warnings
from deoldify import device
from deoldify.device_id import DeviceId

# Set up GPU for DeOldify
device.set(device=DeviceId.GPU0)
from deoldify.visualize import *
torch.backends.cudnn.benchmark=True

# Suppress user warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

# Initialize the DeOldify colorizer
colorizer = get_image_colorizer(artistic=True)
    
# Converts and colorizes the image from the provided URL.
def convert_image_url(url):
        render_factor=35
        source_url= url
        source_path = 'test_images/image.png'
        result_path = None

        if source_url is not None:
            result_path = colorizer.plot_transformed_image_from_url(url=source_url, path=source_path, render_factor=render_factor, compare=True)
        else:
            result_path = colorizer.plot_transformed_image(path=source_path, render_factor=render_factor, compare=True)
  
# Converts and colorizes the uploaded image
def convert_image():
         render_factor=35
         source_url= None
         source_path = 'test_images/image.png'
         result_path = None

         if source_url is not None:
            result_path = colorizer.plot_transformed_image_from_url(url=source_url, path=source_path, render_factor=render_factor, compare=True)
         else:
            result_path = colorizer.plot_transformed_image(path=source_path, render_factor=render_factor, compare=True)

         
    

# Set page configuration and title
st.set_page_config(page_title="VintageColorize", page_icon="🖌", layout="wide")

# Add header with title and description
st.markdown('<p style="display:inline-block;font-size:40px;font-weight:bold;">🎨VintageColorize </p> <p style="display:inline-block;font-size:16px;">VintageColorize is a tool that breathes new life into old black and white photos. It leverages the powerful technology developed by Jantic called Deoldify, which employs Self-Attention GAN and the innovative NoGAN architecture. <br><br></p>', unsafe_allow_html=True)

# Get image URL input from user
img_url = st.text_input(label='Enter Image URL')

# If user has provided an image URL
if (img_url != "") and (img_url != None):
    st.text("Wait a lil bit....")
    convert_image_url(img_url)
    # Display the converted Image
    st.markdown('#### 🤖 Converted Image:')
    im = Image.open("result_images\\image.png")
    st.image(im)


# Display option to upload an image
st.markdown('<center style="opacity: 70%">OR</center>', unsafe_allow_html=True)
img_upload = st.file_uploader(label='Upload Image', type=['jpg', 'png', 'jpeg'])

# If user has uploaded an image
if img_upload != None:
    st.text("Wait a lil bit....")
    # Read the image from the uploaded file
    img = img_upload.read()
    img = Image.open(io.BytesIO(img))
    # Save the image to a file and convert it
    img.save("test_images\\image.png")
    convert_image()
     # Display the converted image
    st.markdown('#### 🤖 Converted Image:')
    im = Image.open("result_images\\image.png")
    st.image(im)

# This is a multi-line string containing CSS code that hides the Streamlit header, footer, and menu
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""

# This line displays the CSS code in the Streamlit app, effectively hiding the header, footer, and menu
st.markdown(hide_st_style, unsafe_allow_html=True)

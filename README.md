# VintageColorize
VintageColorize is a web application that brings old black and white photos to life by adding color. It utilizes the powerful technology of DeOldify, developed by Jantic, which employs Self-Attention GAN and the innovative NoGAN architecture.
## Description
VintageColorize is a Streamlit application that allows users to colorize black and white photos using the DeOldify library. It provides two methods for colorizing images: through a provided image URL or by uploading an image file.
![imgonline-com-ua-twotoone-3B2l6mIcJ52](https://github.com/RafayKhattak/VintageColorize/assets/90026724/3c57d75a-8869-4cae-8136-3d0ba9cf2744)
The application uses the DeOldify library, which is a deep learning-based image colorization tool. It leverages Self-Attention GAN and the NoGAN architecture to produce impressive colorized results.

The application has the following features:

- Colorize images from a provided image URL.
- Colorize uploaded image files (supported formats: jpg, png, jpeg).
- Display the colorized images in the application.

## Installation
To run the VintageColorize application locally, you need to follow these steps:

1. Clone the repository:
```
git clone https://github.com/<username>/<repository>.git
```
2. Change into the project directory:
```
cd <repository>
```
3. Install the required dependencies. It is recommended to use a virtual environment:
```
pip install -r requirements.txt
```
4. Download the pre-trained DeOldify model:
```
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth
```
## Usage
To run the VintageColorize application, use the following command:
```
streamlit run app.py
```
This command will start the application and provide a local URL (e.g., http://localhost:8501). Open the URL in your web browser to access the application.


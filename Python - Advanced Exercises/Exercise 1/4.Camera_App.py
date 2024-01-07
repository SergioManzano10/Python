import streamlit as st
from PIL import Image # Sirve para convertir una foto a escala de grises

# Add an expand button

with st.expander("Start Camera"):
    # Start the camera
    camera_image = st.camera_input("Camera")


if camera_image: # Condicional que sirve para que no nos muestre un error por defecto antes de dar el permiso a la cámara

    # Create a pillow image instance
    img = Image.open(camera_image)

    # Convert the pillow image tograyscale
    gray_img = img.convert("L") # L es uno de los algoritmos que convierte a escala de gries

    # Render the grayscale image on the web page
    st.image(gray_img)
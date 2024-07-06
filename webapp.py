import streamlit as st
from Diffusion_model import *


st.title("Diffusion model")
ingested_query=  st.text_input("Please enter input query")

if ingested_query:
    image_bytes= query({
        "inputs": ingested_query
    })


import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

st.image(image)




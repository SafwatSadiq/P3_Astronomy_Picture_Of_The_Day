import requests
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
api = os.getenv("API")
url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

response = requests.get(url)
content = response.json()
image = requests.get(content["url"]).content

st.header(content["title"])

with open("image.jpg", "wb") as img:
    img.write(image)
st.image("image.jpg")

st.write(content["explanation"])
import requests
import streamlit as st

url = f"https://api.nasa.gov/planetary/apod?api_key={api}"

response = requests.get(url)
content = response.json()
image = requests.get(content["url"]).content

st.header(content["title"])

with open("image.jpg", "wb") as img:
    img.write(image)
st.image("image.jpg")

st.write(content["explanation"])
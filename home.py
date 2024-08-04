import streamlit as st
from PIL import Image

def app():
    # Ensure session state variables are initialized
    if 'username' in st.session_state:
        uid = st.session_state.username
    else:
        uid = "Guest"

    st.title(f"Welcome to SafeSpace: {uid}")

    # Ensure image paths are correct
    image_1 = Image.open("icons/logo.jpeg")
    image_2 = Image.open("icons/chatbot.jpeg")
    image_3 = Image.open("icons/forums.jpeg")
    image_4 = Image.open("icons/resources 2.png")

    # Create the first row with one image
    row1 = st.columns([1])
    row1[0].image(image_1, caption="At SafeSpace, we have:", use_column_width=True)

    # Create the second row with three images
    row2 = st.columns(3)
    row2[0].image(image_2, caption="Our Chatbot: Protecta", use_column_width=True)
    row2[1].image(image_3, caption="Forums for Women", use_column_width=True)
    row2[2].image(image_4, caption="Resources like helplines and NGOs", use_column_width=True)

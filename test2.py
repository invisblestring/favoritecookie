import os 
import streamlit as st
from streamlit_extras.let_it_rain import rain
def example():
    rain(
        emoji="🌸",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
st.title("good morning Cookie")
resault = st.button("Click me ^_^", on_click=example)
if resault:
    st.write("**I love you**")

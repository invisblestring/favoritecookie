import streamlit as st
from streamlit_extras.let_it_rain import rain
import json
import streamlit-lottie as st

def load_lottiefile(filepath: str):
    with open (filepath, "r") as f:
        return json.load(f)


def example():
    rain(
        emoji="🌸",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
        
    )
    
st.title("good morning Witchy")
witch = load_lottiefile("C:\\Users\\abalm\\test\\1721807061415.json")
love = load_lottiefile("C:\\Users\\abalm\\test\\1721810066289.json")
mixed = load_lottiefile("main_scene3.json")


 
resault = st.button("Click me ^_^", on_click=example)
if resault:
    st.title("**I love you**")
    ##col1, col2= st.columns(2,gap="small")
    st_lottie(mixed,quality="high",loop=True)
    ##with col1:
     ##st_lottie(love,quality="high",loop=True,height=50,width=50)
     ##st.write(' ')

    ##with col2:
     ##st_lottie(witch,quality="high",loop=True,height=50,width=50)
    ## st.write('')
   
    st.text("-       couldn't make u look like \n you would kill with all that cuteness")

 

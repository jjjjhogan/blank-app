import streamlit as st
from openai import OpenAI
import pandas as pd
import random

mode = st.selectbox('Choose mode',['Learn','Game','Sentence'])
morse_code = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}
if mode == "":
    st.write('Choose mode')
elif mode == 'Learn':
    st.write(f"Translate {random.choice(list(morse_code.keys())) }")
    i = st.text_input("Put . and - with / inbetween for spaces")





import streamlit as st
from openai import OpenAI
import pandas as pd
import random


st.success('Your operation was successful')
mode = st.selectbox('Choose mode',['Learn','Game','Sentence'])
if 'letter' not in st.session_state:
    st.session_state['letter'] = ''
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
    if st.session_state['letter'] == '': st.session_state['letter'] = random.choice(list(morse_code.keys()))
       
    st.write(f"Translate { st.session_state['letter']}")
    i = st.text_input("Put . and - with / inbetween for spaces")
    submit = st.button('submit')

    if submit:
        if i.strip() == morse_code[st.session_state['letter']]:
            st.write("Correct")
        else:
            st.write(morse_code[st.session_state['letter']])





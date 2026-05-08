import streamlit as st
from openai import OpenAI
import pandas as pd

mode = st.selectbot('Choose mode',['Learn','Game','Sentence'])

if mode == "":
    st.write('Choose mode')
elif mode == 'Learn'
    st.write("Translate 'L'")
    i = st.text_input("Put . and - with / inbetween for spaces")





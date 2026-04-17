import streamlit as st
from openai import OpenAI
from pandas import dataframe as pd
d = {-1:1,0:2,1:3,2:4,3:5}

df = pd.dataframe(data=d)

st.line_chart(df,x='x',y='y')

client = OpenAI(api_key=st.secrets['key'])
with st.form('my-form'):
    answer = st.text_input('What is the answer to the bots question?')

    s = st.form_submit_button('submit')

    if s:
        st.session_state['history'].append({'role':'user','content':answer})

        response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = st.session_state['history']
        )   
        st.session_state['history'].append({'role':'assistant','content':response.choices[0].message.content}) 


if 'history' not in st.session_state:
    st.session_state['history'] = [{'role':'system','content':'You are a word guesser bot. You will be guessing a word, ask yes or no questions to the user and use their responses to make a guess. You have 3 chances to make final guess or the round is over. for each final guess start with *FINAL GUESS*. Keep a background counter of all final guessese you have made and stop when you make 3. Start with a simple queestion like "is the word a noun"'}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = st.session_state['history']
    ) 
    st.session_state['history'].append({'role':'assistant','content':response.choices[0].message.content}) 




for message in st.session_state['history']:
    if message['role'] == 'assistant':
        with st.chat_message('ai'):
            st.write(message['content'])
    elif message['role']=='user':
        with st.chat_message('user'):
            st.write(message['content'])










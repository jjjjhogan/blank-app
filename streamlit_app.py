import streamlit as st
from openai import OpenAI
import pandas as pd
import requests
d = {'x':[-3,-2,-1,0,1,2,3],'y':[-1,0,1,2,3,4,5]}
# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
r = requests.get(url)
data = r.json()

st.write(data)
df = pd.DataFrame(data=d)

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










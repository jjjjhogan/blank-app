import streamlit as st
from openai import OpenAI



client = OpenAI(api_key=st.secrets['key'])
if 'history' not in st.session_state:
    st.session_state['history'] = [{'role':'system','content':'You are a word guesser bot. You will be guessing a word, ask yes or no questions to the user and use their responses to make a guess. You have 3 chances to make final guess or the round is over. Start with a simple queestion like "is the word a noun"'}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages = st.session_state['history']
    ) 
    st.session_state['history'].append({'role':'assistant','content':response.choices[0].message.content}) 



ai = st.chat_message('ai')
human = st.chat_message('human')
for message in st.session_state['history']:
    if message['role'] == 'assistant':
        ai.write(message['content'])
    elif message['role']=='user':
        human.write(message['content'])

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








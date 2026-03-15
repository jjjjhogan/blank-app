# 1
from json import loads
from openai import OpenAI
import streamlit as st


def printdict(dictionary):
    s = ""
    for k,v in dictionary.items():
        if type(v) == str:
            s+= (k +': ' + v) + '\n'
        else:
            if type(v) == dict:
                s+= k + '\n'
                for x,y in dictionary[k].items():
                    s += '    ' + str(x) +': ' + str(y) + '\n'
            elif type(v) == list:
                s+= k + '\n'
                for val in v:
                    s+= '    ' + val + '\n'
    return s




client = OpenAI(
    api_key = st.secrets['key']
    )
if 'pokedex' not in st.session_state:

    st.session_state['pokedex'] = []
# 2
system_prompt = """
You are a pokedex. Output in the form of json in this format: Put the values for each key where 'value' is. The stats values will be from 0 to 15. The entry value will be a 4 digit code like 0000. Type_weak and type_strong will be where you put what types the pokemon is weak and strong to.

 {
    'name':'value',
    'entry':'value',
    'stats':
        {'hp':'value',
        'attack':'value',
        'def':'value',
        'attack_special':'value',
        'defense_special':'value',
        'speed':'value'}
    'desc':'value'
    'details':
        {'height':'value'
        'weight':'value'
        'gender':'value'
        'category':'value'
        'abilities':['value1','value2']}
    
    'type_weak':'value',
    'type_strong':'value'
    'evolves_into':'value'
    }
    """
with st.form('my_form'):
    running = True
    while(running):
        # 3
        inquiry = st.text_input("""Welcome to the Pokedex!
        What would you like to do?
        1. View generated Pokedex entries
        2. Create a new Pokedex entry
        3. Exit with 'q' or 'e'
        :""")
        if inquiry == '1':
            print('Here are all of your entries: ')
            if len(st.session_state['pokedex'])==0:
                print('You have no entries, use 2. Create a new Pokedex entry')
            else:
                for i in range(len(st.session_state['pokedex'])):
                    st.write(str(i+1) + '. ' + str(st.session_state['pokedex'][i]['name']))
                num = st.text_input('What pokemon num do you want to see')

                st.write(printdict(st.session_state['pokedex'][int(num)-1]))

        elif inquiry == 'q' or inquiry == 'e':
            running = False
        else:
            user_prompt = st.text_input('What pokemon would you like to add')

            b = st.form_submit_button('Generate entry')
            if b:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    response_format={ "type": "json_object" },
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ]
                )

                # 5

                st.write(printdict(loads(response.choices[0].message.content)))
                st.session_state['pokedex'].append(loads(response.choices[0].message.content))      
    




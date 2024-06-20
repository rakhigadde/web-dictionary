import streamlit as st
import requests 
import json
from streamlit_option_menu import option_menu


st.header("Search a word")
word = st.text_input('Enter the word: ')
if word != "":
    st.write('\nThe meaning(s) of the word is: ')
    response = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    json_data = json.loads(response.text
                           
                           )  # Convert response text to JSO
    if response.status_code == 200:
        try:
            json_data = json.loads(response.text)  # Convert response text to JSON
            if json_data == "":
                st.write('No meaning for the word found')
            if isinstance(json_data, list) and json_data:
                word_info = json_data[0]  # Assuming the response is a list containing word information
                word = word_info.get("word")
                meanings = word_info.get("meanings", [])
                st.write("Word:", word)
                st.write("Definitions:")
                for idx, meaning in enumerate(meanings, start=1):
                    definitions = meaning.get("definitions", [])
                    for definition_idx, definition in enumerate(definitions, start=1):
                        if definition_idx > 2:
                            break
                        st.write(f"{idx}. {definition['definition']}")
            else:
                st.write("No data found for the word.")
        except json.JSONDecodeError:
            st.write("Error decoding JSON data")

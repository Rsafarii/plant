# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:16:37 2020

@author: RASA-
"""
import numpy as np
import streamlit as st
import wikipedia
from googletrans import Translator

import requests
import json
st.beta_set_page_config(
 page_title="Plant identifier",
  layout="centered"
)
st.title('Plant Identification Service')
#st.image("2.jpeg", use_column_width=True)
@st.cache(suppress_st_warning=True,persist=False,allow_output_mutation=True) 
def PASS():
	passw = st.text_input('Enter password')
	if passw == 'r.faghihi':
		pass
	else :
		st.stop()
#PASS()

uploaded_file = st.file_uploader("browse your plant image:")
if uploaded_file is not None:
    try:
        bytes_data = uploaded_file.read()
        st.image(bytes_data, use_column_width=True)
        image_data_1 = bytes_data
        image_path_1 = '2.jpg'
        #st.write(image_path_1)
        API_KEY = "2a10ibWmb8fqHUhEVzUMTc6O"  # Set you API_KEY here
        api_endpoint = f"https://my-api.plantnet.org/v2/identify/all?api-key={API_KEY}"
        data = {
            'organs': ['leaf']
            }

        files = [
            ('images', (image_path_1, image_data_1)),
            ]

        req = requests.Request('POST', url=api_endpoint, files=files, data=data)
        prepared = req.prepare()
        s = requests.Session()
        response = s.send(prepared)
        json_result = json.loads(response.text)
       
        Type=json_result['results'][0]['species']['genus']['scientificNameWithoutAuthor']
        st.write(f"Type of the your Plant with {json_result['results'][0]['score']} is {Type}")
        try:
        	translator = Translator()
        	result = translator.translate(Type, src='en', dest='fa')
        except:
        	pass
        try:
        
        	wikipedia.set_lang("en")
        	W=wikipedia.summary(Type)
        	st.write((W))
        except:
        	pass
        try:
        	wikipedia.set_lang("fa")
        	W_p=wikipedia.summary(Type)
        	st.markdown("<h1 style='text-align:  justify; color: blue;'> </h1>", unsafe_allow_html=True)
        	st.write(W_p)
        except:
        	pass
    except:
        st.write('Please browse your image again')
        


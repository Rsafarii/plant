import numpy as np
import streamlit as st
import streamlit.components.v1 as components

import wikipedia
from googletrans import Translator
import requests
import json

st.beta_set_page_config(
 page_title="Plant identifier",
  layout="centered")
@st.cache(suppress_st_warning=True,persist=False,allow_output_mutation=True) 
def PASS():
	passw = st.text_input('Enter password')
	if passw == 'r.faghihi':
		pass
	else :
		st.stop()
PASS()

components.html(
f'''
<style>
h1 {{
text-align: center;
color:green;
font-family:TimesNewRoman, Times, serif;

}}
#v1 {{
background-image: url("https://demo.w3layouts.com/demos_new/template_demo/29-12-2018/plants-demo_Free/1725139257/web/images/2.jpg");
background-size: cover;
background-attachment: scroll;
width: 100%;
height: 300px; 
}}
#v2 {{
background-image: url("https://image.freepik.com/foto-gratis/mano-turistica-que-sostiene-telefono-movil-mientras-que-toma-fotografia-hoja-arce-estacion-follaje_55877-521.jpg");
background-size: cover;
background-attachment: scroll;
width: 100%;
height: 300px; 
}}

</style>
<div id='v1'>
  <h1 >PLANT SEARCH</h1>
</div>
<div id='v2'>

</div>
''',height=600,)
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
        st.write(f"<p style='text-align:center'> Your Plant is :  {Type}</p>", unsafe_allow_html=True)
        try:
        	translator = Translator()
        	result = translator.translate(Type, src='en', dest='fa')
        except:
        	pass
        try:
        
        	wikipedia.set_lang("en")
        	W=wikipedia.summary(Type)
        	st.write(f"<p style='text-align: justify; color: black; border: 1px solid black;margin:10px; padding: 15px;' lang='en' dir='ltr'> {W} </p>", unsafe_allow_html=True)
        except:
        	pass
        try:
        	wikipedia.set_lang("fa")
        	W_p=wikipedia.summary(Type)
        	#with open('font.css') as f:
        		#st.write(f"<style>{f.read()}</style> <article id='mp' lang='fa' dir='rtl'> {W_p} </article>", unsafe_allow_html=True)
        	st.write(f"<p style='text-align: justify; color: blue;border: 1px solid blue;margin:10px; padding: 15px;' lang='fa' dir='rtl'> {W_p} </p>", unsafe_allow_html=True)
        except:
        	pass
    except:
        st.write('Please browse your image again')

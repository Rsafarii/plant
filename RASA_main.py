import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from bs4 import BeautifulSoup
from googlesearch import search 
import wikipedia
from googletrans import Translator
import requests
import json
import time
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
color:#ff944d;
font-family:TimesNewRoman, Times, serif;
font-size:20px;

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
        API_KEY2 = "2a10qFkaUAYqr4EaMzFvFuwwPe"
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
        #st.write(f"<p style='text-align:center'> Your Plant is :  {Type}</p>", unsafe_allow_html=True)
        placeholder = st.empty()
        with placeholder.beta_container():
            components.html('''
                
<style>                
   * {
  border: 0;
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  font-size: calc(16px + (24 - 16)*(100vw - 320px)/ (1280 - 320));
}

body, .preloader {
  display: flex;
}

body {
  background: #ffffff;
  color: #33ff33;
  font: 1em Dosis, sans-serif;
  height: 100vh;
  line-height: 1.5;
  perspective: 40em;
}

.preloader {
  animation: tiltSpin 8s linear infinite;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: auto;
  width: 17em;
  height: 17em;
}
.preloader, .preloader__ring {
  transform-style: preserve-3d;
}
.preloader__ring {
  animation-name: spin;
  animation-duration: 4s;
  animation-timing-function: inherit;
  animation-iteration-count: inherit;
  font-size: 2em;
  position: relative;
  height: 3rem;
  width: 1.5rem;
}
.preloader__ring:nth-child(even) {
  animation-direction: reverse;
}
.preloader__sector {
  font-weight: 600;
  position: absolute;
  top: 0;
  left: 0;
  text-align: center;
  text-transform: uppercase;
  transform: translateZ(7rem);
}
.preloader__sector, .preloader__sector:empty:before {
  display: inline-block;
  width: 100%;
  height: 100%;
}
.preloader__sector:empty:before {
  background: linear-gradient(transparent 45%, currentColor 45% 55%, transparent 55%);
  content: "";
}
.preloader__sector:nth-child(2) {
  transform: rotateY(12deg) translateZ(7rem);
}
.preloader__sector:nth-child(3) {
  transform: rotateY(24deg) translateZ(7rem);
}
.preloader__sector:nth-child(4) {
  transform: rotateY(36deg) translateZ(7rem);
}
.preloader__sector:nth-child(5) {
  transform: rotateY(48deg) translateZ(7rem);
}
.preloader__sector:nth-child(6) {
  transform: rotateY(60deg) translateZ(7rem);
}
.preloader__sector:nth-child(7) {
  transform: rotateY(72deg) translateZ(7rem);
}
.preloader__sector:nth-child(8) {
  transform: rotateY(84deg) translateZ(7rem);
}
.preloader__sector:nth-child(9) {
  transform: rotateY(96deg) translateZ(7rem);
}
.preloader__sector:nth-child(10) {
  transform: rotateY(108deg) translateZ(7rem);
}
.preloader__sector:nth-child(11) {
  transform: rotateY(120deg) translateZ(7rem);
}
.preloader__sector:nth-child(12) {
  transform: rotateY(132deg) translateZ(7rem);
}
.preloader__sector:nth-child(13) {
  transform: rotateY(144deg) translateZ(7rem);
}
.preloader__sector:nth-child(14) {
  transform: rotateY(156deg) translateZ(7rem);
}
.preloader__sector:nth-child(15) {
  transform: rotateY(168deg) translateZ(7rem);
}
.preloader__sector:nth-child(16) {
  transform: rotateY(180deg) translateZ(7rem);
}
.preloader__sector:nth-child(17) {
  transform: rotateY(192deg) translateZ(7rem);
}
.preloader__sector:nth-child(18) {
  transform: rotateY(204deg) translateZ(7rem);
}
.preloader__sector:nth-child(19) {
  transform: rotateY(216deg) translateZ(7rem);
}
.preloader__sector:nth-child(20) {
  transform: rotateY(228deg) translateZ(7rem);
}
.preloader__sector:nth-child(21) {
  transform: rotateY(240deg) translateZ(7rem);
}
.preloader__sector:nth-child(22) {
  transform: rotateY(252deg) translateZ(7rem);
}
.preloader__sector:nth-child(23) {
  transform: rotateY(264deg) translateZ(7rem);
}
.preloader__sector:nth-child(24) {
  transform: rotateY(276deg) translateZ(7rem);
}
.preloader__sector:nth-child(25) {
  transform: rotateY(288deg) translateZ(7rem);
}
.preloader__sector:nth-child(26) {
  transform: rotateY(300deg) translateZ(7rem);
}
.preloader__sector:nth-child(27) {
  transform: rotateY(312deg) translateZ(7rem);
}
.preloader__sector:nth-child(28) {
  transform: rotateY(324deg) translateZ(7rem);
}
.preloader__sector:nth-child(29) {
  transform: rotateY(336deg) translateZ(7rem);
}
.preloader__sector:nth-child(30) {
  transform: rotateY(348deg) translateZ(7rem);
}

/* Animations */
@keyframes tiltSpin {
  from {
    transform: rotateY(0) rotateX(30deg);
  }
  to {
    transform: rotateY(1turn) rotateX(30deg);
  }
}
@keyframes spin {
  from {
    transform: rotateY(0);
  }
  to {
    transform: rotateY(1turn);
  }
}
</style>
	
	<div class="preloader">
  <div class="preloader__ring">
    <div class="preloader__sector">L</div>
    <div class="preloader__sector">o</div>
    <div class="preloader__sector">a</div>
    <div class="preloader__sector">d</div>
    <div class="preloader__sector">i</div>
    <div class="preloader__sector">n</div>
    <div class="preloader__sector">g</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
  </div>
  <div class="preloader__ring">
    <div class="preloader__sector">L</div>
    <div class="preloader__sector">o</div>
    <div class="preloader__sector">a</div>
    <div class="preloader__sector">d</div>
    <div class="preloader__sector">i</div>
    <div class="preloader__sector">n</div>
    <div class="preloader__sector">g</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector">.</div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
    <div class="preloader__sector"></div>
  </div>
</div>
''',height=300,)
        try:
        	translator = Translator()
        	result = translator.translate(Type, src='en', dest='fa')
        except:
        	pass
        try:
        
        	wikipedia.set_lang("en")
        	W=wikipedia.summary(Type)
        	#st.write(f"<p style='text-align: center; color: black; border: 1px solid black;margin:10px; padding: 15px;' lang='en' dir='ltr'> {W} </p>", unsafe_allow_html=True)
        except:
        	W='No information found '
        try:
        	wikipedia.set_lang("fa")
        	W_p=wikipedia.summary(Type)
        	#with open('font.css') as f:
        		#st.write(f"<style>{f.read()}</style> <article id='mp' lang='fa' dir='rtl'> {W_p} </article>", unsafe_allow_html=True)
        	#st.write(f"<p style='text-align: center; color: blue;border: 1px solid blue;margin:10px; padding: 15px;' lang='fa' dir='rtl'> {W_p} </p>", unsafe_allow_html=True)
        except:
        	W_p='اطلاعاتی یافت نشد'
        try :
            for j in range(3):
                char = 'nargil.com:'+Type+ ' شرایط نگهداری '
                try : 
                    for i in  search(char, tld="com", num=1, stop=1, pause=1):
		           		#print(i)
                           google_search = i
                    #print(j)
                    break
                except:
                    pass
            URL_1 = google_search
            page = requests.get(URL_1)
            soup = BeautifulSoup(page.content, 'html.parser')
        except:
            pass
        try:
            results = soup.find("meta", attrs={'name':'Description'})
            #print(type(results),results['content'])
        except:
            pass
        try:
            ID_list = ['ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_plant_en',
                       'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_plant_fa',
		           'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_sname',
		           'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_family_en',
                   'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_family_fa',
		           'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_native',
		           'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_othernames']
            ID_list2=['ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_light',
		          'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_water',
		          'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_temprature',
		          'ContentPlaceHolder_NargilBaseBody_ContentPlaceHolder_NargilContentBody_lbl_soil']
            ID_find = []
            ID_find2=[]
            for i in ID_list:
                R = soup.find(id=i).text
                ID_find.append((R))
            for i in ID_list2:
                R = soup.find(id=i).text
                ID_find2.append((R))
            #st.write(ID_find)
        except:
            pass
        
        
        try:
            st.write(f"<p style='text-align:center; color:green'> Your Plant is :  {Type}</p>", unsafe_allow_html=True)
            import base64
            data_url = base64.b64encode(bytes_data).decode("utf-8")
            components.html(
                f'''
                <table>
                <tr>
                <td width="80%" align="center" valign="middle">
                <table height="100%" border="1" bordercolor="#99ffeb" cellpadding="4" cellspacing="4" width="100%">
                <tbody><tr>
                <td dir="rtl" align="center" colspan="2">
                <span  style="font-size: 15pt; color: #0d0d0d">{ID_find[1]}</span>
                        &nbsp;-&nbsp;
                    <span  style="font-size: 14pt; color: #0d0d0d">{ID_find[0]}</span>
                </td>
                </tr>
                <tr>
                <td align="right">
                    <span  style="font-size:10pt;font-size: 11pt;color: #0d0d0d">{ID_find[2]}</span>
                </td>
                <td align="right" width="20%" bgcolor=" #ccfff5">
                    <span  style="font-size:10pt;font-weight: 700">:نام علمی</span>
                </td>
                </tr>
                <tr>
                <td align="right">
                    &nbsp;
                    <span   style="color:#0d0d0d;text-decoration:none;font-size: 11pt">{ID_find[3]}</span>
                    &nbsp;-
                    <span   style="color:#0d0d0d;text-decoration:none;font-size: 11pt">{ID_find[4]}</span>
                </td>
                <td align="right" width="20%" bgcolor=" #ccfff5">
                    <span  style="font-size:10pt;font-weight: 700">:خانواده</span>
                </td>
                </tr>
                <tr>
                <td align="right" dir="rtl">
                    <span  style="font-size:10pt;font-size: 11pt">{ID_find[5]}</span>
                </td>
                <td align="right" width="20%" bgcolor=" #ccfff5">
                    <span  style="font-size:10pt;font-weight: 700">:بومی منطقه</span>
                </td>
                </tr>
                <tr>
                <td align="right" dir="rtl">
                    <span  style="font-size:10pt;font-size: 11pt">{ID_find[6]}</span>
                </td>
                <td align="right" width="20%" bgcolor=" #ccfff5">
                    <span  style="font-size:10pt;font-weight: 700">:نام های دیگر</span>
                </td>
                </tr>
                </tbody></table>
                </td>
                
                </tr>
               
               
                <tr>
                <td colspan="2" align="right" valign="middle"><table height="20%" width="100%" border="0" cellpadding="0" cellspacing="1" bordercolor="#009900">
                <tbody><tr>
                <td width="25%" align="center" valign="middle" bgcolor="#ccfff5">
            <span  style=" font-weight: 700; font-size: 9pt">خاک و تغذیه</span>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#ccfff5">
            <span  style=" font-weight: 700; font-size: 9pt">دمای ایده آل محیط</span>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#ccfff5">
            <span  style=" font-weight: 700; font-size: 9pt">آبیاری و رطوبت</span>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#ccfff5">
            <span  style=" font-weight: 700; font-size: 9pt">نور  محیط</span>
            </td>
            </tr>
            <tr>
            <td width="25%" align="center" valign="middle" bgcolor="#DBF7E3">
            <table border="0" cellpadding="0" cellspacing="0" width="100%">
                <tbody><tr>
                    <td align="right" valign="middle" dir="rtl">
                        <span style=" font-size: 9pt">{ID_find2[3]}</span>
                    </td>
                    <td align="center" valign="middle" width="30">
                        <img  src="https://nargil.ir/plant/images/measures/soil.png" style="height:40px;width:35px;">
                        </td>
                </tr>
            </tbody></table>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#DBF7E3">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" >
                <tbody><tr>
                    <td align="right" valign="middle" dir="rtl">
                        <span  style=" font-size: 9pt">{ID_find2[2]}</span>
                        
                    </td>
                    <td align="center" valign="middle" width="30">
                        <img  src="https://nargil.ir/plant/images/measures/thermometer/3.png" style="height:40px;width:35px;">
                        </td>
                </tr>
            </tbody></table>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#DBF7E3">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" >
                <tbody><tr>
                    <td align="right" valign="middle">
                        <span  style=" font-size: 9pt">{ID_find2[1]}</span>
                    </td>
                    <td align="center" valign="middle" width="30" >
                        <img  src="https://nargil.ir/plant/images/measures/water/4.png" style="height:40px;width:35px;">
                       </td>
                </tr>
            </tbody></table>
            </td>
            <td width="25%" align="center" valign="middle" bgcolor="#DBF7E3">
            <table border="0" cellpadding="0" cellspacing="0" width="100%" >
                <tbody><tr>
                    <td align="right" valign="middle">
                        <span  style=" font-size: 9pt">{ID_find2[0]} </span>
                    </td>
                    <td align="center" valign="middle" width="30">
                        <img  src="https://nargil.ir/plant/images/measures/sun/4.png" style="height:40px;width:40px;">
                        </td>
                </tr>
            </tbody></table>
            </td>
            </tr>
            </tbody></table></td>
            </tr>
                </table>
                
                
                ''',height=450,)
                
            
        except:
            pass
        
        
        try:
            components.html(
                f"""
                <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                <div id="accordion">
                <div align="center" class="card">
                <div  class="card-header" id="headingOne">
                <h5  class="mb-0">
                <button  style='font-size:12px' class="btn btn-info" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                English Wikipedia 
                </button>
                </h5>
                </div>
                <div  id="collapseOne" class="collapse " aria-labelledby="headingOne" data-parent="#accordion">
                <div class="card-body">
                <p style='text-align: center; color: blue; border: 1px solid blue;margin:10px; padding: 15px;' lang='en' dir='ltr'> {W} </p> 
                </div>
                </div>
                </div>
                <div align="center" class="card">
                <div class="card-header" id="headingTwo">
                <h5 class="mb-0">
                <button bgcolor="#DBF7E3" style='font-size:12px' class="btn btn-info" collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            ویکیپدیا فارسی                
                </button>
                </h5>
                </div>
                <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
                <div class="card-body">
                <p style='text-align: center; color: blue;border: 1px solid blue;margin:10px; padding: 15px;' lang='fa' dir='rtl'> {W_p} </p>
                </div>
                </div>
                </div>
                </div>
                """,
                height=1100,
                )
        except:
                pass
        placeholder.empty()
    except:
        st.write('Please browse your image again')




import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Extract Medical Entities App", layout="centered")
st.image(image, caption='Extract Medical Entities')
#
# page header
st.title(f"Extract Medical Entities App")
with st.form("Extract"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Extract Medical Entities and Abbreviations")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/detect-entities-from-medical-text-f425f34b/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key lMITVdij.OYYST24hriXWlI4ZvDcRSUCKcBidbiqn','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Entities and Abbreviations Detected")
        # output results
        st.success(response.text.split("response\\")[1])
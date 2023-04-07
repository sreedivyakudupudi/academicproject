# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 12:21:17 2023

@author: SREE DIVYA
"""
import numpy as np
import pickle
import pandas as pd

import base64
import streamlit as st

#from PIL import Image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
        
        
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local("security-ge4cee84f8_1920.jpg")
pickle_in = open("classifier_rf.pkl","rb")
classifier_rf=pickle.load(pickle_in)





def malware_detection(Machine,SizeOfOptionalHeader,Characteristics,MajorLinkerVersion,MinorLinkerVersion,SizeOfCode,SizeOfInitializedData,SizeOfUninitializedData,AddressOfEntryPoint,BaseOfCode):
    prediction = classifier_rf.predict([[Machine,SizeOfOptionalHeader,Characteristics,MajorLinkerVersion,MinorLinkerVersion,SizeOfCode,SizeOfInitializedData,SizeOfUninitializedData,AddressOfEntryPoint,BaseOfCode]])
    print(prediction)
    return prediction
    




def main():
    #st.title("Malware Detection")
    original_title = '<p style="font-family:Times; color:white; font-size: 40px;text-align: center; color:#283593;font-weight: 800; ;">Malware Detection</p>'
    st.markdown(original_title, unsafe_allow_html=True)
    html_temp ="""<div style="background-color:#1976d2;padding:10px">
    <h2 style = "color:white;text-align:center;font-family:Times">Malware Detection ML APP</h2>
    </div>"""
   
    st.markdown(html_temp,unsafe_allow_html=True)
    #input1="""<div style= color:#1A237E;>
    Machine = st.text_input("Machine","Type Here")
    SizeOfOptionalHeader = st.text_input("Size Of Optional Header","Type Here")
    Characteristics = st.text_input("Characteristics","Type Here")
    MajorLinkerVersion = st.text_input("Major Linker Version","Type Here")
    MinorLinkerVersion = st.text_input("Minor Linker Version","Type Here")
    SizeOfCode = st.text_input("Size Of Code","Type Here")
    SizeOfInitializedData = st.text_input("Size Of Initialized Data","Type Here")
    SizeOfUninitializedData = st.text_input("Size Of Uninitialized Data        ","Type Here")
    AddressOfEntryPoint = st.text_input("Address Of Entry Point","Type Here")
    BaseOfCode = st.text_input("Base Of Code","Type Here")
    #</div>"""
    
    #st.markdown(input1,unsafe_allow_html=True)
    s = f"""
    <style>
    div.stButton > button:first-child {{ border: 2px solid #444490; border-radius:15px 15px 15px 15px; font-family:Times;background-color:#e7fbff;font-size:10px;color:#1A237E;}}
    div.stButton > button:hover {{background-color: #FFFDE7;color:red}}
   
    """
    st.markdown(s, unsafe_allow_html=True)
    result=""
    if st.button("Predict"):
        result=malware_detection(Machine,SizeOfOptionalHeader,Characteristics,MajorLinkerVersion,MinorLinkerVersion,SizeOfCode,SizeOfInitializedData,SizeOfUninitializedData,AddressOfEntryPoint,BaseOfCode)
    #st.success('output is {}'.format(result))
    if(result==0):
        st.success("Malware is not present")
    else:
        st.success("Malware is present")
    if st.button("About"):
        st.text("Leats Learn")
        st.text("Built with streamlit")
       
        
if __name__=='__main__':
    main()

    
    
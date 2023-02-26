import streamlit as st
from matplotlib import image
import pandas as pd
import os

st.title("Dashboard - Naruto Uzumaki")

FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Naruto.jpg")

img = image.imread(IMAGE_PATH)
st.image(img)

st.header("Select the Power:")
power = st.selectbox("To See his Form",{"Six_Paths_Sage_Mode","Super_Tailed_Beast_Rasen_Shuriken","Bijuu_Mode"})
    
if power == 'Six_Paths_Sage_Mode':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "Six_Paths_Sage_Mode.jpeg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Super_Tailed_Beast_Rasen_Shuriken':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "Super_Tailed_Beast_Rasen_Shuriken.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)
if power == 'Bijuu_Mode':
    IMAGE_PATH1 = os.path.join(dir_of_interest, "images", "Bijuu_Mode.jpg")
    imgg = image.imread(IMAGE_PATH1)
    st.image(imgg)









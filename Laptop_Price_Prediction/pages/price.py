import streamlit as st
import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from PIL import Image
import os


st.set_page_config(page_title='Laptop Price Prediction App')

FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
DATA_PATH = os.path.join(dir_of_interest, "data", "laptop.csv")



FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "images", "laptop.jpg")



df = pd.read_csv(DATA_PATH)
X = df.drop('MRP', axis=1)
y = df['MRP']


preprocessor = ColumnTransformer(
    [
        ('onehot', OneHotEncoder(handle_unknown='ignore'), ['Processor', 'OS', 'Storage','RAM_type','RAM_SIZE','Brand']),
        ('scaler', StandardScaler(), ['Display_Size'])
    ],
    remainder='passthrough'
)
X_pr = preprocessor.fit_transform(X)
rfr = RandomForestRegressor(random_state=42)
rfr.fit(X_pr, np.log(y))

st.header('Laptop Price Prediction')

# Add input widgets to sidebar
Brand = st.selectbox('Select Brand', ['ASUS','Lenovo','Vaio','Nokia','Ultimus','ALIENWARE','realme','Infinix','APPLE','MSI','acer','DELL','RedmiBook','HP'])
Ram_type = st.selectbox('Select RAM Type',
                        ['DDR4 RAM', 'DDR5 RAM', 'LPDDR4X RAM','LPDDR5 RAM'])

RAM_SIZE = st.selectbox('Select RAM Size', ['8 GB','16 GB','4 GB','32 GB'])


OS = st.selectbox('Select Operating System', ['Windows 11 Operating System','Windows 10 Operating System', 'Mac OS Operating System',         
                                        'Chrome Operating System',  'DOS Operating System'])

Storage=st.selectbox('select Storage',['512 GB SSD','1 TB SSD','256 GB SSD','1 TB HDD256 GB SSD',     
            '1 TB HDD', '64 GB EMMC', '2 TB SSD','128 GB SSD'])
Processor=st.selectbox('Select Processor type', ['Intel Core i5 Processor','Intel Core i3 Processor', 'AMD Ryzen 9 Octa Core Processor', 
                   'AMD Ryzen 7 Octa Core Processor','Intel Core i7 Processor','AMD Ryzen 5 Hexa Core Processor'
'AMD Ryzen 3 Dual Core Processor','AMD Ryzen 5 Quad Core Processor','Intel Celeron Dual Core Processor',    
'Intel Core i9 Processor','Apple M1 Processor', 'Apple M1 Pro Processor', 'Apple M2 Processor',                        
'AMD Ryzen 3 Quad Core Processor','Qualcomm Snapdragon 7c Gen 2 Processor'])
Display_Size=st.select_slider('Choose any display (in inches):',
                               (11.6, 13., 13.3, 13.4, 13.5, 13.6, 14., 14.1, 14.2, 14.96, 15., 15.6, 16., 16.1, 16.2, 16.6, 17.3))


X_test = pd.DataFrame({'Brand': [Brand], 'Processor': [Processor],
                       'OS': [OS], 'RAM_SIZE': [RAM_SIZE],
                       'RAM_type': [Ram_type], 'Storage': [Storage],
                       'Display_Size': [Display_Size]})


X_test_pr = preprocessor.transform(X_test)
if st.button('Predict laptop price'):
    y_pr = round(np.exp(rfr.predict(X_test_pr))[0])
    st.markdown('Predicted price is <span style="color: red; font-size: 25px;">' + str(y_pr) + ' INR</span>', unsafe_allow_html=True)
st.image(Image.open(IMAGE_PATH),width=270)

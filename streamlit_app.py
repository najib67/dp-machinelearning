import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
  df

st.write('**X**')
X = df.drop('species', axis=1)
X

st.write('**y**')
y = df.species
y

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

#Data preparation

with st.sidebar:
  st.header('Input features')
  "","bill_depth_mm","flipper_length_mm","body_mass_g"
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('male', 'femal'))
  bill_length_mm = st.slider('Bull length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.stider('bill depth (mm)', 13.&, 21.5, 17.2)
  flipper_lendth_mm = st.slider('Flipper length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body mass (g)',2700.0, 6300.0, 4207.0)

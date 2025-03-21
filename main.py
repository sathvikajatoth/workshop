import streamlit as st

st.title('Hello World')
st.write('This is a simple Streamlit app.')

st.button("submit")
st.text("hello,streamlit")



st.radio("gender",["male","female"],index=None)

name=st.text_input('enter ur name')
if name:
	st.write(f'hello ,{name}!')
	
if st.file_uploader('pls upload file:',type=['txt','csv']):
	st.write("thanks for uploading")

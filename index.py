import streamlit as st
st.set_page_config("First Streamlit web-app")

st.header("Table printer")



num = st.number_input("Enter a number", 1, 1000)

for i in range (1,11):

    st.write(num,'X', i,'=', num*i)
st.balloons()
import streamlit as st
st.header("Hello World")

num = st.number_input("Enter a number", 1, 10)

for i in (1,11):

    st.write(num,'X', i,'=', num*i)

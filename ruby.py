import streamlit as st
import datetime
st.title('R.J College')
st.header("Mater's application")
name=st.text_input('Enter your name :')
f=st.text_input("Enter Father's name: ")
m=st.text_input("Enter your Mother's name :")
l=st.text_input('Enter your last name :')
g=st.radio("Genger",('Male','Female','Trans','Other'))
q=st.write('Qualification:')
op1=st.checkbox('ssc')
op2=st.checkbox('Hsc')
op3=st.checkbox('Bsc')
op4=st.checkbox('Msc')
st.text_area('Write your SOP',max_chars=1000)
d=st.date_input(
    "Date of Birth")

st.button('Submit')
if(st.button('submit')):
    st.warning("your form is submitted")
    st.write("Your name: ",name,f,m)
    st.write("your DOB",d)
    st.write("your qualification","SSC",op1,"HSC",op2,"Bsc",op3,"Msc",op4)
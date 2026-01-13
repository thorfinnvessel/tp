import streamlit as st 
st.title("Make a calculator applet:")

num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")



op = st.selectbox("Choose operation:",["add","subtract","multi","div"])

if st.button("Calculate"):
    if op=="add":
        result = num1+num2
    elif op=="subtract":
        result = num1-num2
    elif op=="multi":
        result = num1*num2
    elif op=="div":
        if num2!=0:
            result = num1/num2
        else:
            result ="Not divisible by zero!"

st.write("The result is:", result)      
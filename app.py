#from flask import Flask, render_template, request
# import ipynb notebook
# import import_ipynb 
import model1
import streamlit as st

st.header("TEXT to SQL query generator")
st.write("Hey there! This is a simple text to SQL query generator. It is based on a openAI's GPT-3 model that predicts the SQL query based on the text.")


question = st.text_input("write your text here")
if st.button("Generate SQL query"):
    reply = model1.gpt.get_top_reply(prompt= question)
    st.write(reply)


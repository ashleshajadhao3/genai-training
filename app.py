import streamlit as st
import pandas as pd
import numpy as np
st.title("My First Streamlit App")
st.write("Hello Urvashi")
st.text("Lets start")
name = st.text_input("Enter name:")
if st.button("Greet"):
    st.success(f"hello, {name}!")
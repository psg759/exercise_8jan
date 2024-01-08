import numpy as np
import pickle
import pandas as pd
import streamlit as st 

pickle_in = open("reg_RF.pkl","rb")
reg=pickle.load(pickle_in)


def predict_note_authentication(hour_s,pre_score):
    prediction=reg.predict([[hour_s,pre_score]])
    print(prediction)
    return prediction

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(hour_s,pre_score)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn Python")
        st.text("Built with Streamlit")

if __name__ == '__main__':
    main()

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

#from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("kmean.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def K_Means_UI_Issue(Diff_TTVC_TTLC,E2E,cli_cpu,TTVC):
    prediction=classifier.predict([[Diff_TTVC_TTLC,E2E,cli_cpu,TTVC]])
    print(prediction)
    return prediction



def main():
    st.title("UI Issue Prediction For Performance") 
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;"> UI Issue Prediction For Performance-ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Diff_TTVC_TTLC = st.text_input("TTVC - TTLC [s]","")
    E2E = st.text_input("End to end response time [s]","")
    cli_cpu = st.text_input("Client CPU Time [s]","")
    TTVC = st.text_input("Time to Visually Complete [s]","")
    result=""
    if st.button("Predict"):
        result=K_Means_UI_Issue(Diff_TTVC_TTLC,E2E,cli_cpu,TTVC)
    if result==0:
        result="UI - Low Risk"
        st.success(result)
    elif result==1:
        result="UI - High Risk"
        st.warning(result)
    elif result==2:
        result="UI - Very High Risk"
        st.error(result)
    else:
        result="Click on Predict button"
      
    #st.success(result)

if __name__=='__main__':
    main()
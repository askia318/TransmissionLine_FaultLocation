import pickle
import streamlit as st
import pandas as pd
import numpy as np

# loading the trained model
pickle_in = open('Random_Forest.pkl', 'rb')
classifier = pickle.load(pickle_in)

# loading the dataset
data = pd.read_csv("result.csv")

@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(
    IAang, IAang2, IAmag,
    IAmag2, IBang, IBang2,
    IBmag, IBmag2, ICang,
    ICang2, ICmag, ICmag2,
    VAang1, VAang2, VAmag1,
    VAmag2, VBang1, VBang2,
    VBmag1, VBmag2, VCang1,
    VCang2, VCmag1, VCmag2
):

    # Making predictions
    prediction = classifier.predict(
        [[IAang, IAang2, IAmag,
    IAmag2, IBang, IBang2,
    IBmag, IBmag2, ICang,
    ICang2, ICmag, ICmag2,
    VAang1, VAang2, VAmag1,
    VAmag2, VBang1, VBang2,
    VBmag1, VBmag2, VCang1,
    VCang2, VCmag1, VCmag2]])

    if prediction == 0:
        pred = '0%'
    elif prediction == 1:
        pred = '25%'
    elif prediction == 2:
        pred = '50%'
    else:
        pred = '75%'
    return pred


# this is the main function in which we define our webpage
def main():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:green;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Transmission Line Fault Location Prediction App</h1>
    <h2 style ="color:grey;text-align:center;">by HV-Lab Dr. Cheng-Chung Li</h2>
    <img class="fit-picture"
     src="taipower.jpeg"
     alt="Taipower">
    </div> 
    """

    from PIL import Image
    image = Image.open('taipower.png')

    # display the front end aspect
    #st.markdown(html_temp, unsafe_allow_html=True)
    st.title('Transmission Line Fault Location ML App')
    st.caption('By HV_Lab Dr. Cheng-Chung Li')
    #st.image((image, caption='Taipower')

    # following lines create boxes in which user can enter data required to make prediction
    IAang = st.slider('IAang', min(data['IAang']), max(data["IAang"]))
    IAang2 = st.slider('IAang2', min(data['IAang2']), max(data["IAang2"]))
    IAmag = st.slider('IAmag', min(data['IAmag']), max(data["IAmag"]))
    IAmag2 = st.slider('IAmag2', min(data['IAmag2']), max(data["IAmag2"]))
    IBang = st.slider('IBang', min(data['IBang']), max(data["IBang"]))
    IBang2 = st.slider('IBang2', min(data['IBang2']), max(data["IBang2"]))
    IBmag = st.slider('IBmag', min(data['IBmag']), max(data["IBmag"]))
    IBmag2 = st.slider('IBmag2', min(data['IBmag2']), max(data["IBmag2"]))
    ICang = st.slider('ICang', min(data['ICang']), max(data["ICang"]))
    ICang2 = st.slider('ICang2', min(data['ICang2']), max(data["ICang2"]))
    ICmag = st.slider('ICmag', min(data['ICmag']), max(data["ICmag"]))
    ICmag2 = st.slider('ICmag2', min(data['ICmag2']), max(data["ICmag2"]))
    VAang1 = st.slider('VAang1', min(data['VAang1']), max(data["VAang1"]))
    VAang2 = st.slider('VAang2', min(data['VAang2']), max(data["VAang2"]))
    VAmag1 = st.slider('VAmag1', min(data['VAmag1']), max(data["VAmag1"]))
    VAmag2 = st.slider('VAmag2', min(data['VAmag2']), max(data["VAmag2"]))
    VBang1 = st.slider('VBang1', min(data['VBang1']), max(data["VBang1"]))
    VBang2 = st.slider('VBang2', min(data['VBang2']), max(data["VBang2"]))
    VBmag1 = st.slider('VBmag1', min(data['VBmag1']), max(data["VBmag1"]))
    VBmag2 = st.slider('VBmag2', min(data['VBmag2']), max(data["VBmag2"]))
    VCang1 = st.slider('VCang1', min(data['VCang1']), max(data["VCang1"]))
    VCang2 = st.slider('VCang2', min(data['VCang2']), max(data["VCang2"]))
    VCmag1 = st.slider('VCmag1', min(data['VCmag1']), max(data["VCmag1"]))
    VCmag2 = st.slider('VCmag2', min(data['VCmag2']), max(data["VCmag2"]))




    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(
    IAang, IAang2, IAmag,
    IAmag2, IBang, IBang2,
    IBmag, IBmag2, ICang,
    ICang2, ICmag, ICmag2,
    VAang1, VAang2, VAmag1,
    VAmag2, VBang1, VBang2,
    VBmag1, VBmag2, VCang1,
    VCang2, VCmag1, VCmag2)
        st.success('The Fault Location is  {}'.format(result))

if __name__ == '__main__':
    main()
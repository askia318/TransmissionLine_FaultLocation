import pickle
import streamlit as st
import pandas as pd
import numpy as np

# loading the trained model
pickle_in = open('Random_Forest.pkl', 'rb')
classifier = pickle.load(pickle_in)

# loading the dataset
data = pd.read_csv("minmax.csv")

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

    #from PIL import Image
    #image = Image.open('taipower.png')

    # display the front end aspect
    #st.markdown(html_temp, unsafe_allow_html=True)
    st.title('Transmission Line Fault Location ML App')
    st.caption('By HV_Lab Dr. Cheng-Chung Li')
    #st.image((image, caption='Taipower')

    # following lines create boxes in which user can enter data required to make prediction
    IAang = st.slider('IAang', data['Min'].loc[0].astype(float), data['Max'].loc[0].astype(float))
    IAang2 = st.slider('IAang2', data['Min'].loc[1].astype(float), data['Max'].loc[1].astype(float))
    IAmag = st.slider('IAmag', data['Min'].loc[2].astype(float), data['Max'].loc[2].astype(float))
    IAmag2 = st.slider('IAmag2', data['Min'].loc[3].astype(float), data['Max'].loc[3].astype(float))
    IBang = st.slider('IBang', data['Min'].loc[4].astype(float), data['Max'].loc[4].astype(float))
    IBang2 = st.slider('IBang2', data['Min'].loc[5].astype(float), data['Max'].loc[5].astype(float))
    IBmag = st.slider('IBmag', data['Min'].loc[6].astype(float), data['Max'].loc[6].astype(float))
    IBmag2 = st.slider('IBmag2', data['Min'].loc[7].astype(float), data['Max'].loc[7].astype(float))
    ICang = st.slider('ICang', data['Min'].loc[8].astype(float), data['Max'].loc[8].astype(float))
    ICang2 = st.slider('ICang2', data['Min'].loc[9].astype(float), data['Max'].loc[9].astype(float))
    ICmag = st.slider('ICmag', data['Min'].loc[10].astype(float), data['Max'].loc[10].astype(float))
    ICmag2 = st.slider('ICmag2', data['Min'].loc[11].astype(float), data['Max'].loc[11].astype(float))
    VAang1 = st.slider('VAang1', data['Min'].loc[12].astype(float), data['Max'].loc[12].astype(float))
    VAang2 = st.slider('VAang2', data['Min'].loc[13].astype(float), data['Max'].loc[13].astype(float))
    VAmag1 = st.slider('VAmag1', data['Min'].loc[14].astype(float), data['Max'].loc[14].astype(float))
    VAmag2 = st.slider('VAmag2', data['Min'].loc[15].astype(float), data['Max'].loc[15].astype(float))
    VBang1 = st.slider('VBang1', data['Min'].loc[16].astype(float), data['Max'].loc[16].astype(float))
    VBang2 = st.slider('VBang2', data['Min'].loc[17].astype(float), data['Max'].loc[17].astype(float))
    VBmag1 = st.slider('VBmag1', data['Min'].loc[18].astype(float), data['Max'].loc[18].astype(float))
    VBmag2 = st.slider('VBmag2', data['Min'].loc[19].astype(float), data['Max'].loc[19].astype(float))
    VCang1 = st.slider('VCang1', data['Min'].loc[20].astype(float), data['Max'].loc[20].astype(float))
    VCang2 = st.slider('VCang2', data['Min'].loc[21].astype(float), data['Max'].loc[21].astype(float))
    VCmag1 = st.slider('VCmag1', data['Min'].loc[22].astype(float), data['Max'].loc[22].astype(float))
    VCmag2 = st.slider('VCmag2',data['Min'].loc[23].astype(float), data['Max'].loc[23].astype(float))




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
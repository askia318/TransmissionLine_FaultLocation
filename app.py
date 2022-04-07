import pickle
import streamlit as st

# loading the trained model
pickle_in = open('Random_Forest.pkl', 'rb')
classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
def prediction(
    Subsystem_1_CTLs_Vars_IAang, Subsystem_1_CTLs_Vars_IAang2, Subsystem_1_CTLs_Vars_IAmag,
    Subsystem_1_CTLs_Vars_IAmag2, Subsystem_1_CTLs_Vars_IBang, Subsystem_1_CTLs_Vars_IBang2,
    Subsystem_1_CTLs_Vars_IBmag, Subsystem_1_CTLs_Vars_IBmag2, Subsystem_1_CTLs_Vars_ICang,
    Subsystem_1_CTLs_Vars_ICang2, Subsystem_1_CTLs_Vars_ICmag, Subsystem_1_CTLs_Vars_ICmag2,
    Subsystem_1_CTLs_Vars_VAang1, Subsystem_1_CTLs_Vars_VAang2, Subsystem_1_CTLs_Vars_VAmag1,
    Subsystem_1_CTLs_Vars_VAmag2, Subsystem_1_CTLs_Vars_VBang1, Subsystem_1_CTLs_Vars_VBang2,
    Subsystem_1_CTLs_Vars_VBmag1, Subsystem_1_CTLs_Vars_VBmag2, Subsystem_1_CTLs_Vars_VCang1,
    Subsystem_1_CTLs_Vars_VCang2, Subsystem_1_CTLs_Vars_VCmag1, Subsystem_1_CTLs_Vars_VCmag2
):

    # Making predictions
    prediction = classifier.predict(
        [[Subsystem_1_CTLs_Vars_IAang, Subsystem_1_CTLs_Vars_IAang2, Subsystem_1_CTLs_Vars_IAmag,
    Subsystem_1_CTLs_Vars_IAmag2, Subsystem_1_CTLs_Vars_IBang, Subsystem_1_CTLs_Vars_IBang2,
    Subsystem_1_CTLs_Vars_IBmag, Subsystem_1_CTLs_Vars_IBmag2, Subsystem_1_CTLs_Vars_ICang,
    Subsystem_1_CTLs_Vars_ICang2, Subsystem_1_CTLs_Vars_ICmag, Subsystem_1_CTLs_Vars_ICmag2,
    Subsystem_1_CTLs_Vars_VAang1, Subsystem_1_CTLs_Vars_VAang2, Subsystem_1_CTLs_Vars_VAmag1,
    Subsystem_1_CTLs_Vars_VAmag2, Subsystem_1_CTLs_Vars_VBang1, Subsystem_1_CTLs_Vars_VBang2,
    Subsystem_1_CTLs_Vars_VBmag1, Subsystem_1_CTLs_Vars_VBmag2, Subsystem_1_CTLs_Vars_VCang1,
    Subsystem_1_CTLs_Vars_VCang2, Subsystem_1_CTLs_Vars_VCmag1, Subsystem_1_CTLs_Vars_VCmag2]])

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
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Transmission Line Fault Location Prediction ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    Subsystem_1_CTLs_Vars_IAang = st.number_input("Subsystem_1_CTLs_Vars_IAang")
    Subsystem_1_CTLs_Vars_IAang2 = st.number_input("Subsystem_1_CTLs_Vars_IAang2")
    Subsystem_1_CTLs_Vars_IAmag = st.number_input("Subsystem_1_CTLs_Vars_IAmag")
    Subsystem_1_CTLs_Vars_IAmag2 = st.number_input("Subsystem_1_CTLs_Vars_IAmag2")
    Subsystem_1_CTLs_Vars_IBang = st.number_input("Subsystem_1_CTLs_Vars_IBang")
    Subsystem_1_CTLs_Vars_IBang2 = st.number_input("Subsystem_1_CTLs_Vars_IBang2")
    Subsystem_1_CTLs_Vars_IBmag = st.number_input("Subsystem_1_CTLs_Vars_IBmag")
    Subsystem_1_CTLs_Vars_IBmag2 = st.number_input("Subsystem_1_CTLs_Vars_IBmag2")
    Subsystem_1_CTLs_Vars_ICang = st.number_input("Subsystem_1_CTLs_Vars_ICang")
    Subsystem_1_CTLs_Vars_ICang2 = st.number_input("Subsystem_1_CTLs_Vars_ICang2")
    Subsystem_1_CTLs_Vars_ICmag = st.number_input("Subsystem_1_CTLs_Vars_ICmag")
    Subsystem_1_CTLs_Vars_ICmag2 = st.number_input("Subsystem_1_CTLs_Vars_ICmag2")
    Subsystem_1_CTLs_Vars_VAang = st.number_input("Subsystem_1_CTLs_Vars_VAang1")
    Subsystem_1_CTLs_Vars_VAang2 = st.number_input("Subsystem_1_CTLs_Vars_VAang2")
    Subsystem_1_CTLs_Vars_VAmag = st.number_input("Subsystem_1_CTLs_Vars_VAmag1")
    Subsystem_1_CTLs_Vars_VAmag2 = st.number_input("Subsystem_1_CTLs_Vars_VAmag2")
    Subsystem_1_CTLs_Vars_VBang = st.number_input("Subsystem_1_CTLs_Vars_VBang1")
    Subsystem_1_CTLs_Vars_VBang2 = st.number_input("Subsystem_1_CTLs_Vars_VBang2")
    Subsystem_1_CTLs_Vars_VBmag = st.number_input("Subsystem_1_CTLs_Vars_VBmag1")
    Subsystem_1_CTLs_Vars_VBmag2 = st.number_input("Subsystem_1_CTLs_Vars_VBmag2")
    Subsystem_1_CTLs_Vars_VCang = st.number_input("Subsystem_1_CTLs_Vars_VCang1")
    Subsystem_1_CTLs_Vars_VCang2 = st.number_input("Subsystem_1_CTLs_Vars_VCang2")
    Subsystem_1_CTLs_Vars_VCmag = st.number_input("Subsystem_1_CTLs_Vars_VCmag1")
    Subsystem_1_CTLs_Vars_VCmag2 = st.number_input("Subsystem_1_CTLs_Vars_VCmag2")


    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):
        result = prediction(
    Subsystem_1_CTLs_Vars_IAang, Subsystem_1_CTLs_Vars_IAang2, Subsystem_1_CTLs_Vars_IAmag,
    Subsystem_1_CTLs_Vars_IAmag2, Subsystem_1_CTLs_Vars_IBang, Subsystem_1_CTLs_Vars_IBang2,
    Subsystem_1_CTLs_Vars_IBmag, Subsystem_1_CTLs_Vars_IBmag2, Subsystem_1_CTLs_Vars_ICang,
    Subsystem_1_CTLs_Vars_ICang2, Subsystem_1_CTLs_Vars_ICmag, Subsystem_1_CTLs_Vars_ICmag2,
    Subsystem_1_CTLs_Vars_VAang1, Subsystem_1_CTLs_Vars_VAang2, Subsystem_1_CTLs_Vars_VAmag1,
    Subsystem_1_CTLs_Vars_VAmag2, Subsystem_1_CTLs_Vars_VBang1, Subsystem_1_CTLs_Vars_VBang2,
    Subsystem_1_CTLs_Vars_VBmag1, Subsystem_1_CTLs_Vars_VBmag2, Subsystem_1_CTLs_Vars_VCang1,
    Subsystem_1_CTLs_Vars_VCang2, Subsystem_1_CTLs_Vars_VCmag1, Subsystem_1_CTLs_Vars_VCmag2)
        st.success('The Fault Location is  {}'.format(result))

if __name__ == '__main__':
    main()
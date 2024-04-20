import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    st.markdown("<h1 style='text-align: center; color: #ff5733;'>Multiple Disease Prediction System</h1>", unsafe_allow_html=True)
    selected = option_menu('',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    st.write("<h3>Input Information</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        SkinThickness = st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose = st.text_input('Glucose Level')
        Insulin = st.text_input('Insulin Level')
        Age = st.text_input('Age of the Person')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        BMI = st.text_input('BMI value')

    # code for Prediction
    diab_diagnosis = ''
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        if diab_prediction[0] == 1:
            diab_diagnosis = '<h2 style="color: #ff5733;">The person is diabetic</h2>'
        else:
            diab_diagnosis = '<h2 style="color: #33ff5b;">The person is not diabetic</h2>'
    st.markdown(diab_diagnosis, unsafe_allow_html=True)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    st.write("<h3>Input Information</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
        trestbps = st.text_input('Resting Blood Pressure')
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        restecg = st.text_input('Resting Electrocardiographic results')
        exang = st.text_input('Exercise Induced Angina')
        slope = st.text_input('Slope of the peak exercise ST segment')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col2:
        sex = st.text_input('Sex')
        chol = st.text_input('Serum Cholestoral in mg/dl')
        thalach = st.text_input('Maximum Heart Rate achieved')
        oldpeak = st.text_input('ST depression induced by exercise')
        ca = st.text_input('Major vessels colored by flourosopy')
    with col3:
        cp = st.text_input('Chest Pain types')

    # code for Prediction
    heart_diagnosis = ''
    # creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0] == 1:
            heart_diagnosis = '<h2 style="color: #ff5733;">The person is having heart disease</h2>'
        else:
            heart_diagnosis = '<h2 style="color: #33ff5b;">The person does not have any heart disease</h2>'
    st.markdown(heart_diagnosis, unsafe_allow_html=True)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")

    st.write("<h3>Input Information</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        RAP = st.text_input('MDVP:RAP')
        APQ3 = st.text_input('Shimmer:APQ3')
        APQ = st.text_input('MDVP:APQ')
        HNR = st.text_input('HNR')
        spread1 = st.text_input('spread1')
        D2 = st.text_input('D2')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        PPQ = st.text_input('MDVP:PPQ')
        APQ5 = st.text_input('Shimmer:APQ5')
        DDA = st.text_input('Shimmer:DDA')
        RPDE = st.text_input('RPDE')
        spread2 = st.text_input('spread2')
        PPE = st.text_input('PPE')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
        DDP = st.text_input('Jitter:DDP')
        Shimmer = st.text_input('MDVP:Shimmer')
        NHR = st.text_input('NHR')
        DFA = st.text_input('DFA')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    # code for Prediction
    parkinsons_diagnosis = ''
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "<h2 style='color: #ff5733;'>The person has Parkinson's disease</h2>"
        else:
            parkinsons_diagnosis = "<h2 style='color: #33ff5b;'>The person does not have Parkinson's disease</h2>"
    st.markdown(parkinsons_diagnosis, unsafe_allow_html=True)

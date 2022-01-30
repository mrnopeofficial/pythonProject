import pickle
import streamlit as st

# loading the trained model

pickle_in = open('classifierReal.pkl', 'rb')

classifier = pickle.load(pickle_in)

@st.cache()
# defining the function which will make the prediction using the data which the user inputs
#Random Forest

def prediction(studyStyle, SchoolType, A, B, C, D, E, F, HouseIncome):

    # Pre-processing user input
    if studyStyle == "Slow":
        studyStyle = 0

    elif studyStyle == "Moderate":
        studyStyle = 1

    else:
        studyStyle = 2

    if SchoolType == "SM/SMK":
        SchoolType = 1

    elif SchoolType == "SBP":
        SchoolType = 2

    elif SchoolType == "MRSM":
        SchoolType = 3

    elif SchoolType == "SMT":
        SchoolType = 4

    elif SchoolType == "SMA/SMKA":
        SchoolType = 5

    else:
        SchoolType = 0

    # Making predictions
    prediction = classifier.predict([[studyStyle, SchoolType, A, B, C, D, E, F, HouseIncome]])
    if prediction == 0:
        pred = 'Other'

    elif prediction == 1:
        pred = 'Foundation'

    elif prediction == 2:
        pred = 'Matriculation'

    else:
        pred = 'Diploma'

    return pred

# this is the main function in which we define our webpage
def main():

    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:Crimson; width: 700px; height: 70px; border-radius: 100px / 90px"> 
    <h1 style ="color:White;text-align:center;">Study Pathway MyCareer</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)

    # following lines create boxes in which user can enter data required to make prediction
    studyStyle = st.selectbox('Study Style', ("Slow", "Moderate", "Fast"))

    SchoolType = st.selectbox('School Type', ("SM/SMK", "SBP", "MRSM", "SMT", "SMA/SMKA", "Other"))

    A = st.sidebar.slider("A subject", 0, 12)

    B = st.sidebar.slider("B subject", 0, 12)

    C = st.sidebar.slider("C subject", 0, 12)

    D = st.sidebar.slider("D subject", 0, 12)

    E = st.sidebar.slider("E subject", 0, 12)

    F = st.sidebar.slider("F subject", 0, 12)

    HouseIncome = st.text_input("House Income", 1000)

    result = ""

    # when 'Predict' is clicked, make the prediction and store it
    if st.button("Predict"):

        result = prediction(studyStyle, SchoolType, A, B, C, D, E, F, HouseIncome)

        st.success('Your next study pathway is {}'.format(result))

        print("Done!")


if __name__ == '__main__':
    main()

#Run @local host guna command -streamlit run main.py
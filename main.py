import pickle
import streamlit as st
import datetime
from PIL import Image

# loading the trained model

pickle_in = open('classifierReal.pkl', 'rb')

classifier = pickle.load(pickle_in)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs
# Random Forest

def prediction(studyStyle, SchoolType, a, B, C, D, E, F, HouseIncome):
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
    prediction = classifier.predict([[studyStyle, SchoolType, a, B, C, D, E, F, HouseIncome]])
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
    menu = ["Home", "Task"]
    choice = st.sidebar.selectbox("", menu)
    image = Image.open('MyCareer.png')
    st.image(image, width=100)

    if choice == "Home":
        # front end elements of the web page
        html_temp = """
            <div style ="background-color:Crimson; width: 700px; height: 70px; border-radius: 100px / 90px"> 
            <h1 style ="color:White;text-align:center;">Study Pathway MyCareer</h1> 
            </div> 
            """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)
        st.subheader("Fill in your detail below to get your study pathway :)")

        # following lines create boxes in which user can enter data required to make prediction
        studyStyle = st.selectbox('Study Style', ("Slow", "Moderate", "Fast"))
        SchoolType = st.selectbox('School Type', ("SM/SMK", "SBP", "MRSM", "SMT", "SMA/SMKA", "Other"))
        HouseIncome = st.text_input("House Income", 1000)

        A = st.sidebar.slider("A subject", 0, 12)
        B = st.sidebar.slider("B subject", 0, 12)
        C = st.sidebar.slider("C subject", 0, 12)
        D = st.sidebar.slider("D subject", 0, 12)
        E = st.sidebar.slider("E subject", 0, 12)
        F = st.sidebar.slider("F subject", 0, 12)
        totalgrade = A+B+C+D+E+F
        predict = st.button("Predict")

        # when 'Predict' is clicked, make the prediction and store it
        if predict and 6 <= totalgrade <= 12:
            result = prediction(studyStyle, SchoolType, A, B, C, D, E, F, HouseIncome)
            st.success('Your next study pathway is {}'.format(result))
            print("Done!")

        elif predict and totalgrade < 6 or totalgrade > 12:
            st.error("Make sure you enter between 6-12 grades only")
        else:
            desc = st.warning("Fill in all of the detail first")

    else:
        # front end elements of the web page
        html_temp = """ 
                    <div style ="background-color:Crimson; width: 700px; height: 70px; border-radius: 100px / 90px"> 
                    <h1 style ="color:White;text-align:center;">Task</h1> 
                    </div> 
                    """

        lastUpdate = datetime.datetime(2022, 2, 4)
        urlTelegram = "https://t.me/mycareerofficial"
        urlFoundation = "https://upu.mohe.gov.my/"
        urlFoundation2 = "https://t.me/mrnopeofficial"
        urlMatriculation = "https://online.mohe.gov.my/UPUOnlinev2/login"
        urlMatriculation2 = "https://t.me/najeeha"
        urlDiploma = "https://upu.mohe.gov.my/index.php/panduan-calon/kategori-stpm-setaraf"
        urlDiploma2 = "https://t.me/amriiiiiiiiiiiiiiiiiiiiii"

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)
        st.subheader("Choose your predicted study pathway")
        option = st.selectbox(
            '',
            ('Foundation', 'Matriculation', 'Diploma'))
        if option == 'Foundation':
            st.write('Task')
            st.write('1. Fill in your UPU [here](%s)' % urlFoundation)
            st.write('2. Join Telegram group [here](%s)' % urlTelegram)
            st.write('3. Ask [Syahmi](%s) for consultation' % urlFoundation2)
        elif option == 'Matriculation':
            st.write('Task')
            st.write('1. Buy your UPU pin & register [here](%s)' % urlMatriculation)
            st.write('2. Join Telegram group [here](%s)' % urlTelegram)
            st.write('3. Ask [Najeeha](%s) for consultation' % urlMatriculation2)
        else:
            st.write('Task')
            st.write('1. Look into your interested field of study [here](%s)' % urlDiploma)
            st.write('2. Join Telegram group [here](%s)' % urlTelegram)
            st.write('3. Ask [Meor](%s) for consultation' % urlDiploma2)
        st.text('Last update on ' + str(lastUpdate.strftime("%x")))


if __name__ == '__main__':
    main()

# Run @local host guna command -streamlit run main.py

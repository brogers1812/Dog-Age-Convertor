import streamlit as st
import streamlit as st
from datetime 

st.header("Official Date Picker")
st.date_input('start date')



st.title("Dog Age Convertor")
html_temp="A basic dog age convertor<br> July 26, 2021 <br> By. Sophia & Beau Rogers "
st.markdown(html_temp,unsafe_allow_html = True)
human_year = st.number_input('Enter your dog age in human years',value=5,min_value=0,max_value=25,step=1)
human_month = st.number_input('Enter your dog age in human months',value=5,min_value=0,max_value=12,step=1)
if human_year == 0:
	dog_age = float(human_month*84/12/12)
	dog_age_months = dog_age % 1
	dog_age_months = int(dog_age_months*12)
	st.text("Your dog is {} years and {} months old.".format(int(dog_age),dog_age_months))
else:
	dog_age_month = float(human_month*84/12/12)
	dog_age_months = dog_age_month % 1
	dog_age_months = int(dog_age_months*12)
	dog_age = human_year*7 + dog_age_month
	st.text("Your dog is {} years and {} months old.".format(int(dog_age),dog_age_months))

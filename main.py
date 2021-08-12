from dateutil.relativedelta import relativedelta
import datetime
import math
import streamlit as st


st.title("Dog Age Convertor")
html_temp="A basic dog age convertor<br> July 26, 2021 <br> By. Sophia & Beau Rogers "
st.markdown(html_temp,unsafe_allow_html = True)
deadline = st.date_input("Select your dog's birthday.")
deadline = str(deadline)

currentDate = datetime.datetime.now()

deadlineDate= datetime.datetime.strptime(deadline,'%Y-%m-%d')
time_difference = relativedelta(currentDate, deadlineDate)
difference_in_years = time_difference.years
if difference_in_years <= 1:
    human_age = 31
    st.text("Your dog's age is approximately equivalent to {} in human years.".format(human_age))
else:
    a = math.log(difference_in_years)
    human_age = round(a * 16 + 31,1)
    st.text("Your dog's age of {} years is approximately equivalent to {} in human years.".format(difference_in_years,human_age))

import streamlit as st


human_year = int(input("How old is your dog in years?"))
human_month = int(input("How old is your dog in months?"))

if human_year == 0:
    dog_age = float(human_month*84/12/12)
    dog_age_months = dog_age % 1
    dog_age_months = int(dog_age_months*12)
    print("Your dog is {} years and {} months old.".format(int(dog_age),dog_age_months))
else:
    dog_age_month = float(human_month*84/12/12)
    dog_age_months = dog_age_month % 1
    dog_age_months = int(dog_age_months*12)
    dog_age = human_year*7 + dog_age_month
    print("Your dog is {} years and {} months old.".format(int(dog_age),dog_age_months))
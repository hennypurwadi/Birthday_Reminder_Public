
import os
import streamlit as st
import csv
from datetime import datetime

st.title("Monthly Birthday Reminder")

# get the current month and year
now = datetime.now()
current_month = now.month
current_year = now.year

# open the CSV file and read the data
with open('Bday_List.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)

  # skip the header row
  next(reader)

  # create a placeholder for the birthday list
  birthday_list = []

  # iterate over the rows in the file
  for row in reader:
    # parse the start work date and birthday date, handling any errors
    try:
      start_work = datetime.strptime(row[1], '%d/%m/%Y')
      birthday = datetime.strptime(row[2], '%d/%m/%Y')
    except ValueError:
      continue

    # check if the employee's birthday is in the current month
    if birthday.month == current_month:
      # calculate the employee's age
      age = current_year - birthday.year

      # calculate the number of years the employee has worked
      years_worked = current_year - start_work.year

      # add the employee's information to the birthday list
      birthday_list.append((row[0], birthday, age, years_worked))

  # check if there are any birthdays in the current month
  if len(birthday_list) > 0:
    st.header("Birthdays in the current month:")

    # iterate over the birthday list and print the employee's information
    for name, birthday, age, years_worked in birthday_list:
      st.write(f"{name} has a birthday on {birthday:%d %B} and is {age} years old. They have worked for {years_worked} years.")
  else:
    st.write("There are no birthdays in the current month.")

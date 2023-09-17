import streamlit as st
import pandas as pd
import json

import DB_Access as dbs
import Price_Functions as pf  # Import the necessary module

with open('output.txt', 'r') as file:
    # Load the contents of the file as a JSON object
    data = json.load(file)

user_id = data["userinfo"]["email"]

users_db = dbs.db.Users

st.header("Hello There")
st.write("If you're looking to trade stocks, head over to TRADES")
st.write("If you want to check out your portfolio, head over to PORTFOLIO")

st.write("### Budgeting")
st.write('''Budgeting is an important part of learning investing. By having a fixed budget, we learn to manage our 
         resources wisely and think about the choices we make. This is why our software allocates you $100000 of 
         simulated currency to use to invest. 
         Although in most cases it might be detrimental to your learning experience as someone learning to invest, we offer you the 
         option to change your budget, or potentially set it to infinite so that it is not a constraint.''')

existing_user = users_db.find_one({"email_id": user_id})
if not existing_user:
    # If the user doesn't exist, create a new user record
    new_user = {
        "email_id": user_id,
        "budget": 100000,
        "is_infinite": False
    }
    users_db.insert_one(new_user)
    st.write(f"Welcome {user_id}! A new account has been created for you.")



# Allow user to modify budget
budget_change = st.number_input("Change budget by (use negative value to reduce):", value=0.0)
is_infinite = st.checkbox("Set budget to infinite")

# Update the database when the user inputs a value
if st.button("Update Budget"):
    if is_infinite:
        users_db.update_one({"email_id": user_id}, {"$set": {"is_infinite": True}})
        st.write("Budget set to infinite!")
    else:
        new_budget = existing_user['budget'] + budget_change
        users_db.update_one({"email_id": user_id}, {"$set": {"budget": new_budget, "is_infinite": False}})
        st.write(f"Budget updated to {new_budget}")
else:
    st.write(f"Current budget: ${existing_user['budget']}")



st.markdown("""
    <a href="http://172.29.6.73:3000/logout" target="_blank">Logout</a>
""", unsafe_allow_html=True)


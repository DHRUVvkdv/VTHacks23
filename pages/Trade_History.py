import streamlit as st
import random
import pandas as pd
import json

# Assuming you have the Price_Functions as pf imported
import Price_Functions as pf
import DB_Access as dbs

with open('output.txt', 'r') as file:
    # Load the contents of the file as a JSON object
    data = json.load(file)

user_id = data["userinfo"]["email"]

st.write("### Trade History")

def generate_trade_history_data(user_id):
    trades = dbs.db.Trades
    user_trades = trades.find({"user_id": user_id})
    
    trade_history_data = []
    for trade in user_trades:
        stock_id = trade["stock_id"]
        stock_name = pf.get_company_name(stock_id)  # Fetch the stock name
        quantity = trade["qty"]
        is_buy = "Buy" if trade["is_buy"] else "Sell"
        price = float(trade["price"])
        
        trade_history_data.append([stock_id, stock_name, quantity, is_buy, price])  # Include the stock name in the data
    
    return trade_history_data

def main():
    # st.set_page_config(page_title="Trade History", page_icon="📜")
    
    trade_history_data = generate_trade_history_data(user_id)
    df = pd.DataFrame(trade_history_data, columns=["Stock ID", "Stock Name", "Quantity", "Buy/Sell", "Price"])  # Update the column names
    df.index = range(1, len(df) + 1)
    st.dataframe(df)

if __name__ == '__main__':
    main()

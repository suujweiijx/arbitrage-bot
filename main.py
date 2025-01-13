import streamlit as st
import pandas as pd
import time
from datetime import datetime
from fetch_odds_api import fetch_odds_api
from calculate_arbitrage import calculate_arbitrage

st.set_page_config(layout="wide")
st.title("Real-Time Arbitrage Dashboard")
st.write("Fetching the latest arbitrage opportunities...")

placeholder = st.empty()

while True:
    start_time = time.time()

    # Fetch odds from Odds API
    odds_api_data = fetch_odds_api()

    # Calculate arbitrage opportunities
    opportunities = calculate_arbitrage(odds_api_data)

    with placeholder.container():
        if opportunities:
            df = pd.DataFrame(opportunities)
            st.subheader("Arbitrage Opportunities")
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No arbitrage opportunities found.")

    print(f"Data fetched at: {datetime.utcnow()} (Execution time: {time.time() - start_time:.2f} seconds)")
    time.sleep(10)
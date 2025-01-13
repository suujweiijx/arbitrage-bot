import requests
import pandas as pd
from datetime import datetime
import time
import streamlit as st

# Your Odds API key
API_KEY = "b00df938b0e9ad6dbca184839f06b2af"

# Parameters for the API
SPORT = "upcoming"
REGIONS = "us"
MARKETS = "h2h"
ODDS_FORMAT = "decimal"
DATE_FORMAT = "iso"
ODDS_API_URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"

# Function to fetch arbitrage opportunities
def fetch_arbitrage_opportunities():
    response = requests.get(
        ODDS_API_URL,
        params={
            "api_key": API_KEY,
            "regions": REGIONS,
            "markets": MARKETS,
            "oddsFormat": ODDS_FORMAT,
            "dateFormat": DATE_FORMAT,
        },
    )

    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code}, {response.text}")
        return []

    odds_data = response.json()
    opportunities = []

    for event in odds_data:
        home_team = event.get("home_team")
        away_team = event.get("away_team")
        league = event.get("sport_title")
        bookmakers = event.get("bookmakers", [])

        # Filter bookmakers
        allowed_bookmakers = ["Bovada", "BetMGM", "DraftKings", "FanDuel", "Pinnacle", "William Hill", "Unibet", "Bet365", "Betway", "Caesars", "PointsBet", "Barstool"]
        filtered_bookmakers = [b for b in bookmakers if b.get("title") in allowed_bookmakers]

        best_home_odds = 0
        best_away_odds = 0
        best_draw_odds = 0
        best_home_bookmaker = ""
        best_away_bookmaker = ""
        best_draw_bookmaker = ""

        for bookmaker in filtered_bookmakers:
            bookmaker_name = bookmaker.get("title")
            for market in bookmaker.get("markets", []):
                if market["key"] == "h2h":
                    for outcome in market["outcomes"]:
                        if outcome["name"] == home_team:
                            if outcome["price"] > best_home_odds:
                                best_home_odds = outcome["price"]
                                best_home_bookmaker = bookmaker_name
                        elif outcome["name"] == away_team:
                            if outcome["price"] > best_away_odds:
                                best_away_odds = outcome["price"]
                                best_away_bookmaker = bookmaker_name
                        elif outcome["name"] == "Draw":
                            if outcome["price"] > best_draw_odds:
                                best_draw_odds = outcome["price"]
                                best_draw_bookmaker = bookmaker_name

        if best_home_odds > 0 and best_away_odds > 0 and best_draw_odds > 0:
            implied_prob_home = 1 / best_home_odds
            implied_prob_away = 1 / best_away_odds
            implied_prob_draw = 1 / best_draw_odds
            total_implied_prob = implied_prob_home + implied_prob_away + implied_prob_draw

            if total_implied_prob < 1:
                profit_percentage = round((1 - total_implied_prob) * 100, 2)
                opportunities.append({
                    "Home Team": home_team,
                    "Away Team": away_team,
                    "League": league,
                    "Profit %": profit_percentage,
                    "Home Odds": best_home_odds,
                    "Away Odds": best_away_odds,
                    "Draw Odds": best_draw_odds,
                    "Home Bookmaker": best_home_bookmaker,
                    "Away Bookmaker": best_away_bookmaker,
                    "Draw Bookmaker": best_draw_bookmaker,
                })

    return opportunities

# Streamlit Dashboard
st.set_page_config(layout="wide")  # Make the dashboard use the full page width

# Static components (title and intro message)
st.title("Real-Time Arbitrage Dashboard")
st.write("Fetching the latest arbitrage opportunities...")

# Create a placeholder for the arbitrage table
placeholder = st.empty()

while True:
    start_time = time.time()
    opportunities = fetch_arbitrage_opportunities()

    with placeholder.container():
        if opportunities:
            df = pd.DataFrame(opportunities)
            st.subheader("Arbitrage Opportunities")
            st.dataframe(df, use_container_width=True)
        else:
            st.write("No arbitrage opportunities found.")

    # Log the execution time and API rate limits
    print(f"Data fetched at: {datetime.utcnow()} (Execution time: {time.time() - start_time:.2f} seconds)")

    # Fetch data every 10 seconds (adjust based on API quota)
    time.sleep(10)
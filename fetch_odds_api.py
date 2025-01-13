import requests

# Your Odds API key and parameters
API_KEY = "b00df938b0e9ad6dbca184839f06b2af"
SPORT = "upcoming"
REGIONS = "us"
MARKETS = "h2h"
ODDS_FORMAT = "decimal"
DATE_FORMAT = "iso"
ODDS_API_URL = f"https://api.the-odds-api.com/v4/sports/{SPORT}/odds"

def fetch_odds_api():
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
    return response.json()
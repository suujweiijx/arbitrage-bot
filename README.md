# Real-Time Arbitrage Dashboard

This project tracks and visualizes **real-time sports betting arbitrage opportunities**. The core idea is simple: if the **implied probabilities** from different bookmakers for all outcomes of an event add up to **less than 1**, there's a chance to lock in **risk-free profit** by betting on each outcome proportionally. 

---

## Features

- **Live Odds Fetching**: Retrieves the latest sports odds from Odds API.
- **Arbitrage Opportunity Detection**: Calculates arbitrage opportunities across multiple bookmakers and presents them with profit percentages.
- **Interactive Dashboard**: Displays results in an easy-to-read and responsive table powered by Streamlit.
- **Customizable Bookmakers**: Focuses only on bookmakers you specify.
- **Real-Time Updates**: Automatically refreshes data every 10 seconds to keep odds and arbitrage opportunities current.
- **Wide Coverage**: Supports multiple sports and markets, including head-to-head (h2h) bets, spreads, and totals.
- **Profitability Highlighting**: Emphasizes the most profitable arbitrage opportunities for quick decision-making.

---

## How It Works

1. **Fetch Odds**:
   - The application fetches real-time odds data from **Odds API** for various sports and bookmakers.
   
2. **Calculate Arbitrage**:
   - The program identifies arbitrage opportunities by comparing odds across bookmakers.
   - It calculates implied probabilities for each outcome and determines if the total probability is less than 1, which indicates a potential arbitrage.

3. **Display Opportunities**:
   - Results are presented in a streamlined table format showing teams, leagues, odds, bookmakers, and potential profit percentages.

---

## Installation

### Prerequisites

- Python 3.8 or higher
- A valid API key from [The Odds API](https://the-odds-api.com/)

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/](https://github.com/)<your-username>/arbitrage-bot.git
   cd arbitrage-bot
   
2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv 
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   
4. **Set Your Odds API Key** <br> Open the main.py file and replace the placeholder with your actual API key from The Odds API.
   ```python
   API_KEY = "your_api_key_here"
   
5. **Run the Streamlit Application**
   ```bash
   streamlit run main.py
   
6. **View the Dashboard** <br> Open the URL provided by Streamlit in your terminal (e.g., http://localhost:8501) to view the interactive dashboard.

---

## File Structure
```plaintext
arbitrage-bot/
├── main.py                  # Main Streamlit application
├── fetch_odds_api.py        # Fetches live odds from Odds API
├── calculate_arbitrage.py   # Calculates arbitrage opportunities
├── requirements.txt         # Lists project dependencies
├── README.md                # Project documentation 
```

---

## Example Output
```plaintext
| Home Team              | Away Team             | League              | Profit % | Home Odds | Away Odds | Draw Odds | Home Bookmaker | Away Bookmaker | Draw Bookmaker |
|------------------------|-----------------------|---------------------|----------|-----------|-----------|-----------|----------------|----------------|----------------|
| Arkansas Golden Lions  | Prairie View Panthers | NCAA Basketball     | 1.26     | 2.55      | 1.68      | None      | Bovada         | FanDuel        | None           |
| OFI Crete              | Levadiakos            | Super League Greece | 54.48    | 21.00     | 29.00     | 2.68      | DraftKings     | DraftKings     | Bovada         |
```

---

## Future Improvements
- Additional Sports and Markets:
  - Expand support for more sports and betting markets (e.g., player props, totals). 
- Automated Betting Integration:
  - Develop automated placement of bets using bookmaker APIs or scraping techniques.
from selenium.webdriver.chrome.options import Options

def fetch_bodog_odds():
    # Configure headless mode for Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=chrome_options)  # Ensure you have the appropriate driver installed
    driver.get("https://www.bodog.eu/sports")  # Adjust the URL for Bodog's sports odds

    odds = []
    try:
        # Locate matches and odds (adjust selectors based on Bodog's HTML structure)
        matches = driver.find_elements(By.CLASS_NAME, "match-class")  # Replace 'match-class' with actual class names
        for match in matches:
            home_team = match.find_element(By.CLASS_NAME, "home-team-class").text
            away_team = match.find_element(By.CLASS_NAME, "away-team-class").text
            home_odds = float(match.find_element(By.CLASS_NAME, "home-odds-class").text)
            away_odds = float(match.find_element(By.CLASS_NAME, "away-odds-class").text)
            odds.append({
                "Home Team": home_team,
                "Away Team": away_team,
                "Home Odds": home_odds,
                "Away Odds": away_odds,
                "Bookmaker": "Bodog"
            })
    finally:
        driver.quit()

    return odds
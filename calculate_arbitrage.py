def calculate_arbitrage(odds_api_data):
    all_odds = []

    # Process Odds API data
    for event in odds_api_data:
        home_team = event.get("home_team")
        away_team = event.get("away_team")
        league = event.get("sport_title")
        for bookmaker in event.get("bookmakers", []):
            for market in bookmaker.get("markets", []):
                if market["key"] == "h2h":
                    outcomes = {outcome["name"]: outcome["price"] for outcome in market["outcomes"]}
                    all_odds.append({
                        "Home Team": home_team,
                        "Away Team": away_team,
                        "League": league,
                        "Home Odds": outcomes.get(home_team),
                        "Away Odds": outcomes.get(away_team),
                        "Draw Odds": outcomes.get("Draw"),  # May be None for sports without a draw
                        "Bookmaker": bookmaker["title"],
                    })

    # Find arbitrage opportunities
    arbitrage_opportunities = []
    unique_events = {(odds["Home Team"], odds["Away Team"]) for odds in all_odds}

    for home_team, away_team in unique_events:
        event_odds = [odds for odds in all_odds if odds["Home Team"] == home_team and odds["Away Team"] == away_team]

        best_home = max(event_odds, key=lambda x: x["Home Odds"] or 0)
        best_away = max(event_odds, key=lambda x: x["Away Odds"] or 0)
        best_draw = None

        # Handle sports that allow draws
        if any(odds["Draw Odds"] for odds in event_odds if odds["Draw Odds"] is not None):
            best_draw = max(event_odds, key=lambda x: x["Draw Odds"] or 0)

        implied_prob_home = 1 / best_home["Home Odds"] if best_home["Home Odds"] else 0
        implied_prob_away = 1 / best_away["Away Odds"] if best_away["Away Odds"] else 0
        implied_prob_draw = 0  # Default to 0 if no draw is possible

        if best_draw and best_draw["Draw Odds"]:
            implied_prob_draw = 1 / best_draw["Draw Odds"]

        total_implied_prob = implied_prob_home + implied_prob_away + implied_prob_draw

        if total_implied_prob < 1:
            profit_percentage = round((1 - total_implied_prob) * 100, 2)
            arbitrage_opportunities.append({
                "Home Team": home_team,
                "Away Team": away_team,
                "League": best_home["League"],
                "Profit %": profit_percentage,
                "Home Odds": best_home["Home Odds"],
                "Away Odds": best_away["Away Odds"],
                "Draw Odds": best_draw["Draw Odds"] if best_draw else None,  # Ensure None for non-draw sports
                "Home Bookmaker": best_home["Bookmaker"],
                "Away Bookmaker": best_away["Bookmaker"],
                "Draw Bookmaker": best_draw["Bookmaker"] if best_draw else None,  # Ensure None for non-draw sports
            })

    return arbitrage_opportunities
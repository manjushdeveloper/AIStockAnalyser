from agents.market_agent import MarketAgent

market = MarketAgent()

data = market.collect_market_data("Reliance Industries")

print(data.keys())

print(data["company"])

print(data["historical"].head())

print(data["financials"])
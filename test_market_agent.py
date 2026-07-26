from agents.market_agent import MarketAgent

agent = MarketAgent()

data = agent.collect_market_data("Reliance Industries")

print(data.keys())
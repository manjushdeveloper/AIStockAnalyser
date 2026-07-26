from agents.technical_agent import TechnicalAgent

agent = TechnicalAgent()

result = agent.analyze("RELIANCE")

for key, value in result.items():
    print(f"{key:20}: {value}")
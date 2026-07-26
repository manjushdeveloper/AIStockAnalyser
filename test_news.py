from agents.news_agent import NewsAgent

agent = NewsAgent()

result = agent.analyze("RELIANCE")

print("=" * 100)
print("LATEST NEWS")
print("=" * 100)

if not result["success"]:
    print(result["message"])
    exit()

for i, article in enumerate(result["news"], start=1):

    print(f"\nArticle {i}")
    print("-" * 100)

    print("Title      :", article["title"])
    print("Publisher  :", article["publisher"])
    print("Published  :", article["published"])
    print("Summary    :", article["summary"])
    print("URL        :", article["url"])
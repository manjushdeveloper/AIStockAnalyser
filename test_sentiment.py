from agents.news_agent import NewsAgent
from agents.sentiment_agent import SentimentAgent


news_agent = NewsAgent()

sentiment_agent = SentimentAgent()


news = news_agent.analyze("RELIANCE")


result = sentiment_agent.analyze(

    news["news"]

)


print()

print("=" * 80)

print("OVERALL SENTIMENT")

print("=" * 80)

print()

print("Overall :", result["overall_sentiment"])

print("Score :", result["sentiment_score"])

print()

print("Positive :", result["positive_news"])

print("Neutral :", result["neutral_news"])

print("Negative :", result["negative_news"])

print()

print("=" * 80)

print("ARTICLE ANALYSIS")

print("=" * 80)

for article in result["articles"]:

    print()

    print(article["title"])

    print("Publisher :", article["publisher"])

    print("Sentiment :", article["sentiment"])

    print("Confidence:", article["confidence"])

    print("Reason :", article["reason"])

    print("-" * 80)
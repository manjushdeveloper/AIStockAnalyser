from datetime import datetime
from tools.yahoo_tool import YahooTool


class NewsAgent:

    def __init__(self):
        self.tool = YahooTool()

    def analyze(self, symbol: str, limit: int = 10):

        news = self.tool.get_news(symbol)

        if not news:
            return {
                "success": False,
                "message": "No news found.",
                "news": []
            }

        articles = []

        for item in news[:limit]:

            content = item.get("content", {})

            provider = content.get("provider", {})

            url = content.get("clickThroughUrl", {}).get("url")

            articles.append({

                "title": content.get("title"),

                "summary": content.get("summary"),

                "publisher": provider.get("displayName"),

                "publisher_url": provider.get("url"),

                "published": self.format_date(
                    content.get("pubDate")
                ),

                "url": url,

                "content_type": content.get("contentType")
            })

        return {
            "success": True,
            "total_articles": len(articles),
            "news": articles
        }

    def format_date(self, value):

        if value is None:
            return None

        try:

            dt = datetime.fromisoformat(
                value.replace("Z", "+00:00")
            )

            return dt.strftime("%d-%b-%Y %H:%M")

        except Exception:

            return value
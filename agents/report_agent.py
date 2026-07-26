from datetime import datetime

from agents.recommendation_agent import RecommendationAgent


class ReportAgent:

    def __init__(self):
        self.recommendation = RecommendationAgent()

    def generate(
        self,
        financial,
        technical,
        sentiment
    ):

        result = self.recommendation.analyze(
            financial,
            technical,
            sentiment
        )

        report = {

            "generated_at":
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

            # ====================================================
            # Company Information
            # ====================================================

            "company":
                financial.get("company_name"),

            "symbol":
                financial.get("symbol"),

            "sector":
                financial.get("sector"),

            "industry":
                financial.get("industry"),

            # ====================================================
            # Market Data
            # ====================================================

            "current_price":
                financial.get("current_price"),

            "target_price":
                financial.get("target_price"),

            "market_cap":
                financial.get("market_cap"),

            # ====================================================
            # Financial Summary
            # ====================================================

            "financial_summary": {

                "PE Ratio":
                    financial.get("pe_ratio"),

                "PEG Ratio":
                    financial.get("peg_ratio"),

                "EPS":
                    financial.get("eps"),

                "Revenue Growth (%)":
                    financial.get("revenue_growth"),

                "Earnings Growth (%)":
                    financial.get("earnings_growth"),

                "Profit Margin (%)":
                    financial.get("profit_margin"),

                "Operating Margin (%)":
                    financial.get("operating_margin"),

                "Debt to Equity":
                    financial.get("debt_to_equity"),

                "Beta":
                    financial.get("beta"),

                "Dividend Yield":
                    financial.get("dividend_yield")

            },

            # ====================================================
            # Technical Summary
            # ====================================================

            "technical_summary": {

                "RSI":
                    technical.get("rsi"),

                "MACD":
                    technical.get("macd"),

                "Signal":
                    technical.get("signal"),

                "Trend":
                    technical.get("trend"),

                "ADX":
                    technical.get("adx"),

                "SMA20":
                    technical.get("sma20"),

                "SMA50":
                    technical.get("sma50"),

                "EMA20":
                    technical.get("ema20"),

                "EMA50":
                    technical.get("ema50"),

                "High Volume":
                    technical.get("high_volume")

            },

            # ====================================================
            # News Sentiment
            # ====================================================

            "sentiment_summary":
                sentiment,

            # ====================================================
            # Final Recommendation
            # ====================================================

            "overall_score": result["overall_score"],

            "confidence": result["confidence"],

            "recommendation": result["recommendation"],

            "strengths": result["strengths"],
        }

        return report
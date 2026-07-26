import traceback
import yfinance as yf


class YahooTool:

    def __init__(self):
        pass

    def _safe_value(self, value):
        if value in [None, "", "N/A", "nan"]:
            return None
        return value

    def _format_symbol(self, symbol: str):
        symbol = symbol.strip().upper()

        if "." not in symbol:
            symbol += ".NS"

        return symbol

    def get_company_details(self, symbol: str):

        try:

            symbol = self._format_symbol(symbol)

            ticker = yf.Ticker(symbol)

            if ticker.history(period="1d").empty:
                return None

            info = ticker.info

            if not info:
                return None

            return {

                # --------------------------------------------------
                # Company Information
                # --------------------------------------------------

                "company_name": self._safe_value(info.get("longName")),
                "sector": self._safe_value(info.get("sector")),
                "industry": self._safe_value(info.get("industry")),
                "website": self._safe_value(info.get("website")),
                "country": self._safe_value(info.get("country")),
                "exchange": self._safe_value(info.get("exchange")),
                "currency": self._safe_value(info.get("currency")),
                "employees": self._safe_value(info.get("fullTimeEmployees")),
                "business_summary": self._safe_value(info.get("longBusinessSummary")),

                # --------------------------------------------------
                # Market Information
                # --------------------------------------------------

                "current_price": self._safe_value(info.get("currentPrice")),
                "previous_close": self._safe_value(info.get("previousClose")),
                "open": self._safe_value(info.get("open")),
                "day_high": self._safe_value(info.get("dayHigh")),
                "day_low": self._safe_value(info.get("dayLow")),

                "market_cap": self._safe_value(info.get("marketCap")),
                "enterprise_value": self._safe_value(info.get("enterpriseValue")),
                "shares_outstanding": self._safe_value(info.get("sharesOutstanding")),
                "beta": self._safe_value(info.get("beta")),

                # --------------------------------------------------
                # Valuation
                # --------------------------------------------------

                "pe": self._safe_value(info.get("trailingPE")),
                "forward_pe": self._safe_value(info.get("forwardPE")),
                "peg": self._safe_value(info.get("pegRatio")),
                "price_to_book": self._safe_value(info.get("priceToBook")),
                "book_value": self._safe_value(info.get("bookValue")),

                # --------------------------------------------------
                # Earnings
                # --------------------------------------------------

                "eps": self._safe_value(info.get("trailingEps")),
                "forward_eps": self._safe_value(info.get("forwardEps")),

                "revenue_growth": (
                    round(info.get("revenueGrowth") * 100, 2)
                    if info.get("revenueGrowth") is not None
                    else None
                ),

                "earnings_growth": (
                    round(info.get("earningsGrowth") * 100, 2)
                    if info.get("earningsGrowth") is not None
                    else None
                ),

                # --------------------------------------------------
                # Profitability
                # --------------------------------------------------

                "roe": self._safe_value(info.get("returnOnEquity")),

                # Yahoo doesn't provide ROCE
                "roce": None,

                "profit_margin": (
                    round(info.get("profitMargins") * 100, 2)
                    if info.get("profitMargins") is not None
                    else None
                ),

                "operating_margin": (
                    round(info.get("operatingMargins") * 100, 2)
                    if info.get("operatingMargins") is not None
                    else None
                ),

                "gross_margin": (
                    round(info.get("grossMargins") * 100, 2)
                    if info.get("grossMargins") is not None
                    else None
                ),

                # --------------------------------------------------
                # Financial Health
                # --------------------------------------------------

                "debt_to_equity": self._safe_value(info.get("debtToEquity")),
                "current_ratio": self._safe_value(info.get("currentRatio")),
                "quick_ratio": self._safe_value(info.get("quickRatio")),

                "total_cash": self._safe_value(info.get("totalCash")),
                "total_debt": self._safe_value(info.get("totalDebt")),

                "free_cashflow": self._safe_value(info.get("freeCashflow")),
                "operating_cashflow": self._safe_value(info.get("operatingCashflow")),

                # --------------------------------------------------
                # Dividend
                # --------------------------------------------------

                "dividend_yield": self._safe_value(info.get("dividendYield")),
                "dividend_rate": self._safe_value(info.get("dividendRate")),

                # --------------------------------------------------
                # Trading Statistics
                # --------------------------------------------------

                "fifty_two_week_high": self._safe_value(info.get("fiftyTwoWeekHigh")),
                "fifty_two_week_low": self._safe_value(info.get("fiftyTwoWeekLow")),

                "average_volume": self._safe_value(info.get("averageVolume")),
                "volume": self._safe_value(info.get("volume")),

                # --------------------------------------------------
                # Analyst Recommendation
                # --------------------------------------------------

                "recommendation": self._safe_value(info.get("recommendationKey")),
                "target_price": self._safe_value(info.get("targetMeanPrice")),
            }

        except Exception:

            print(traceback.format_exc())

            return None

    def get_historical_data(self, symbol, period="1y"):

        try:
            return yf.Ticker(
                self._format_symbol(symbol)
            ).history(period=period)

        except Exception:
            return None

    def get_financials(self, symbol):

        try:
            return yf.Ticker(
                self._format_symbol(symbol)
            ).financials

        except Exception:
            return None

    def get_balance_sheet(self, symbol):

        try:
            return yf.Ticker(
                self._format_symbol(symbol)
            ).balance_sheet

        except Exception:
            return None

    def get_cashflow(self, symbol):

        try:
            return yf.Ticker(
                self._format_symbol(symbol)
            ).cashflow

        except Exception:
            return None

    def get_news(self, symbol):

        try:
            return yf.Ticker(
                self._format_symbol(symbol)
            ).news

        except Exception:
            return []
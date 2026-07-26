from tools.yahoo_tool import YahooTool


class FinancialAgent:

    def __init__(self):
        self.tool = YahooTool()

    def analyze(self, symbol: str):

        info = self.tool.get_company_details(symbol)

        if not info:
            return {
                "success": False,
                "message": "Unable to fetch financial information."
            }

        return {

            "success": True,

            "symbol": symbol.upper(),

            # =====================================================
            # Company Information
            # =====================================================

            "company_name": info.get("company_name"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "website": info.get("website"),
            "country": info.get("country"),
            "exchange": info.get("exchange"),
            "currency": info.get("currency"),
            "employees": info.get("employees"),
            "business_summary": info.get("business_summary"),

            # =====================================================
            # Market Data
            # =====================================================

            "current_price": info.get("current_price"),
            "previous_close": info.get("previous_close"),
            "open": info.get("open"),
            "day_high": info.get("day_high"),
            "day_low": info.get("day_low"),

            "market_cap": info.get("market_cap"),
            "enterprise_value": info.get("enterprise_value"),
            "shares_outstanding": info.get("shares_outstanding"),

            # =====================================================
            # Valuation
            # =====================================================

            "pe_ratio": info.get("pe"),
            "forward_pe": info.get("forward_pe"),
            "peg_ratio": info.get("peg"),
            "price_to_book": info.get("price_to_book"),
            "book_value": info.get("book_value"),

            # =====================================================
            # Earnings
            # =====================================================

            "eps": info.get("eps"),
            "forward_eps": info.get("forward_eps"),

            "revenue_growth": info.get("revenue_growth"),
            "earnings_growth": info.get("earnings_growth"),

            # =====================================================
            # Profitability
            # =====================================================

            "roe": info.get("roe"),
            "roce": info.get("roce"),

            "profit_margin": info.get("profit_margin"),
            "operating_margin": info.get("operating_margin"),
            "gross_margin": info.get("gross_margin"),

            # =====================================================
            # Financial Health
            # =====================================================

            "debt_to_equity": info.get("debt_to_equity"),
            "current_ratio": info.get("current_ratio"),
            "quick_ratio": info.get("quick_ratio"),

            "total_cash": info.get("total_cash"),
            "total_debt": info.get("total_debt"),

            "free_cashflow": info.get("free_cashflow"),
            "operating_cashflow": info.get("operating_cashflow"),

            # =====================================================
            # Risk
            # =====================================================

            "beta": info.get("beta"),

            # =====================================================
            # Dividend
            # =====================================================

            "dividend_yield": info.get("dividend_yield"),
            "dividend_rate": info.get("dividend_rate"),

            # =====================================================
            # Analyst Opinion
            # =====================================================

            "analyst_recommendation": info.get("recommendation"),
            "target_price": info.get("target_price"),

            # =====================================================
            # Trading Statistics
            # =====================================================

            "fifty_two_week_high": info.get("fifty_two_week_high"),
            "fifty_two_week_low": info.get("fifty_two_week_low"),

            "average_volume": info.get("average_volume"),
            "volume": info.get("volume"),
            "revenue_growth": info.get("revenue_growth"),

            "earnings_growth": info.get("earnings_growth"),

            "target_price": info.get("target_price"),

            "analyst_recommendation": info.get("recommendation")
        }
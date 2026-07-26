import os
import requests
from dotenv import load_dotenv


class UpstoxTool:
    """
    Market Data Tool

    Uses IndianAPI instead of Upstox.
    Later, if you move to Upstox,
    only this file needs to change.
    """

    def __init__(self):

        load_dotenv()

        self.api_key = os.getenv("INDIAN_API_KEY")

        # Change to dev.indianapi.in if your plan requires it.
        self.base_url = "https://stock.indianapi.in"

        self.headers = {
            "X-API-Key": self.api_key,
            "accept": "application/json"
        }

    ########################################################

    def _request(self, endpoint, params=None):

        url = f"{self.base_url}/{endpoint}"

        response = requests.get(
            url,
            headers=self.headers,
            params=params,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    ########################################################
    # Company Details
    ########################################################

    def get_company_details(self, stock_name):

        return self._request(
            "stock",
            {
                "name": stock_name
            }
        )

    ########################################################
    # Historical Price Data
    ########################################################

    def get_historical_data(
        self,
        stock_name,
        period="1yr",
        filter_type="default"
    ):

        return self._request(
            "historical_data",
            {
                "stock_name": stock_name,
                "period": period,
                "filter": filter_type
            }
        )

    ########################################################
    # Financial Statements
    ########################################################

    def get_statement(
        self,
        stock_name,
        stats
    ):

        return self._request(
            "statement",
            {
                "stock_name": stock_name,
                "stats": stats
            }
        )

    ########################################################
    # Historical Statistics
    ########################################################

    def get_historical_stats(
        self,
        stock_name,
        stats
    ):

        return self._request(
            "historical_stats",
            {
                "stock_name": stock_name,
                "stats": stats
            }
        )

    ########################################################
    # Target Price
    ########################################################

    def get_target_price(self, stock_id):

        return self._request(
            "stock_target_price",
            {
                "stock_id": stock_id
            }
        )

    ########################################################
    # Corporate Actions
    ########################################################

    def get_corporate_actions(self, stock_name):

        return self._request(
            "corporate_actions",
            {
                "stock_name": stock_name
            }
        )

    ########################################################
    # Recent Announcements
    ########################################################

    def get_recent_announcements(self, stock_name):

        return self._request(
            "recent_announcements",
            {
                "stock_name": stock_name
            }
        )

    ########################################################
    # Trending Stocks
    ########################################################

    def get_trending_stocks(self):

        return self._request("trending")

    ########################################################
    # NSE Most Active
    ########################################################

    def get_nse_most_active(self):

        return self._request("NSE_most_active")

    ########################################################
    # BSE Most Active
    ########################################################

    def get_bse_most_active(self):

        return self._request("BSE_most_active")

    ########################################################
    # News
    ########################################################

    def get_news(self):

        return self._request("news")
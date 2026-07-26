import pandas as pd


class ParserAgent:
    """
    Parser Agent

    Responsibilities
    ----------------
    1. Convert raw API responses into structured data.
    2. Extract company information.
    3. Convert historical price data into a DataFrame.
    """

    def __init__(self):
        pass

    ############################################################

    def parse(self, market_data):

        company = market_data["company"]
        historical = market_data["historical_data"]

        ########################################################
        # Company Information
        ########################################################

        profile = company.get("companyProfile", {})

        fundamentals = {

            "company_name": company.get("companyName"),

            "industry": company.get("industry"),

            "description": profile.get("companyDescription"),

            "isin": profile.get("isInId"),

            "management": profile.get("officers", {})

        }

        ########################################################
        # Historical Price Data
        ########################################################

        historical_df = pd.DataFrame()

        datasets = historical.get("datasets", [])

        price_dataset = None

        for dataset in datasets:

            if dataset.get("metric") == "Price":

                price_dataset = dataset

                break

        if price_dataset is not None:

            historical_df = pd.DataFrame(
                price_dataset["values"],
                columns=[
                    "Date",
                    "Close"
                ]
            )

            historical_df["Date"] = pd.to_datetime(
                historical_df["Date"]
            )

            historical_df["Close"] = historical_df["Close"].astype(
                float
            )

            historical_df.sort_values(
                "Date",
                inplace=True
            )

            historical_df.reset_index(
                drop=True,
                inplace=True
            )

        ########################################################

        return {

             "company": fundamentals,

            "historical": historical_df,
            
            "financials": {

                "roe": None,

                "roce": None,

                "pe": None,

                "peg": None,

                "eps": None,

                "debt_to_equity": None,

                "current_ratio": None,

                "promoter_holding": None,

                "operating_margin": None,

                "net_profit_margin": None,

                "beta": None

            }

        }
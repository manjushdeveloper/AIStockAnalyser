import pandas as pd
import ta


class IndicatorAgent:
    """
    Indicator Agent

    Calculates all technical indicators required
    by the investment strategy.
    """

    def __init__(self):
        pass

    ##########################################################

    def calculate_indicators(self, historical_data):

        """
        historical_data

        Expected columns:

        Date
        Open
        High
        Low
        Close
        Volume
        """

        df = historical_data.copy()

        ######################################################
        # Convert columns to numeric
        ######################################################

        numeric_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]

        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col])

        ######################################################
        # RSI
        ######################################################

        df["RSI"] = ta.momentum.RSIIndicator(
            close=df["Close"],
            window=14
        ).rsi()

        ######################################################
        # EMA
        ######################################################

        df["EMA20"] = ta.trend.EMAIndicator(
            close=df["Close"],
            window=20
        ).ema_indicator()

        df["EMA50"] = ta.trend.EMAIndicator(
            close=df["Close"],
            window=50
        ).ema_indicator()

        df["EMA200"] = ta.trend.EMAIndicator(
            close=df["Close"],
            window=200
        ).ema_indicator()

        ######################################################
        # SMA
        ######################################################

        df["SMA50"] = ta.trend.SMAIndicator(
            close=df["Close"],
            window=50
        ).sma_indicator()

        df["SMA200"] = ta.trend.SMAIndicator(
            close=df["Close"],
            window=200
        ).sma_indicator()

        ######################################################
        # MACD
        ######################################################

        macd = ta.trend.MACD(
            close=df["Close"]
        )

        df["MACD"] = macd.macd()
        df["MACD_SIGNAL"] = macd.macd_signal()
        df["MACD_HIST"] = macd.macd_diff()

        ######################################################
        # ADX
        ######################################################

        adx = ta.trend.ADXIndicator(
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )

        df["ADX"] = adx.adx()

        ######################################################
        # ATR
        ######################################################

        atr = ta.volatility.AverageTrueRange(
            high=df["High"],
            low=df["Low"],
            close=df["Close"]
        )

        df["ATR"] = atr.average_true_range()

        ######################################################
        # Bollinger Bands
        ######################################################

        bb = ta.volatility.BollingerBands(
            close=df["Close"]
        )

        df["BB_UPPER"] = bb.bollinger_hband()
        df["BB_MIDDLE"] = bb.bollinger_mavg()
        df["BB_LOWER"] = bb.bollinger_lband()

        ######################################################
        # Volume Moving Average
        ######################################################

        df["AVG_VOLUME"] = (
            df["Volume"]
            .rolling(20)
            .mean()
        )

        ######################################################
        # Latest Values
        ######################################################

        latest = df.iloc[-1]

        return {

            "current_price": latest["Close"],

            "rsi": latest["RSI"],

            "ema20": latest["EMA20"],

            "ema50": latest["EMA50"],

            "ema200": latest["EMA200"],

            "sma50": latest["SMA50"],

            "sma200": latest["SMA200"],

            "macd": latest["MACD"],

            "macd_signal": latest["MACD_SIGNAL"],

            "macd_histogram": latest["MACD_HIST"],

            "adx": latest["ADX"],

            "atr": latest["ATR"],

            "bb_upper": latest["BB_UPPER"],

            "bb_middle": latest["BB_MIDDLE"],

            "bb_lower": latest["BB_LOWER"],

            "volume": latest["Volume"],

            "average_volume": latest["AVG_VOLUME"]

        }
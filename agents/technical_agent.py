from tools.yahoo_tool import YahooTool

import ta


class TechnicalAgent:

    def __init__(self):

        self.tool = YahooTool()

    def analyze(self, symbol):

        df = self.tool.get_historical_data(
            symbol,
            period="1y"
        )

        if df is None or df.empty:

            return {
                "success": False,
                "message": "No historical data found."
            }

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # -----------------------------
        # RSI
        # -----------------------------

        df["RSI"] = ta.momentum.RSIIndicator(
            close
        ).rsi()

        # -----------------------------
        # MACD
        # -----------------------------

        macd = ta.trend.MACD(close)

        df["MACD"] = macd.macd()

        df["MACD_SIGNAL"] = macd.macd_signal()

        # -----------------------------
        # SMA
        # -----------------------------

        df["SMA20"] = ta.trend.SMAIndicator(
            close,
            window=20
        ).sma_indicator()

        df["SMA50"] = ta.trend.SMAIndicator(
            close,
            window=50
        ).sma_indicator()

        # -----------------------------
        # EMA
        # -----------------------------

        df["EMA20"] = ta.trend.EMAIndicator(
            close,
            window=20
        ).ema_indicator()

        df["EMA50"] = ta.trend.EMAIndicator(
            close,
            window=50
        ).ema_indicator()

        # -----------------------------
        # Bollinger Bands
        # -----------------------------

        bb = ta.volatility.BollingerBands(close)

        df["BB_UPPER"] = bb.bollinger_hband()

        df["BB_LOWER"] = bb.bollinger_lband()

        # -----------------------------
        # ADX
        # -----------------------------

        adx = ta.trend.ADXIndicator(
            high,
            low,
            close
        )

        df["ADX"] = adx.adx()

        latest = df.iloc[-1]

        return {

            "success": True,

            "current_price": round(latest["Close"], 2),

            "rsi": round(latest["RSI"], 2),

            "macd": round(latest["MACD"], 2),

            "signal": round(latest["MACD_SIGNAL"], 2),

            "macd_bullish":
                latest["MACD"] > latest["MACD_SIGNAL"],

            "sma20": round(latest["SMA20"], 2),

            "sma50": round(latest["SMA50"], 2),

            "ema20": round(latest["EMA20"], 2),

            "ema50": round(latest["EMA50"], 2),

            "trend":
                "Bullish"
                if latest["SMA20"] > latest["SMA50"]
                else "Bearish",

            "bollinger_upper":
                round(latest["BB_UPPER"], 2),

            "bollinger_lower":
                round(latest["BB_LOWER"], 2),

            "adx":
                round(latest["ADX"], 2),

            "volume":
                int(latest["Volume"]),

            "average_volume":
                int(df["Volume"].tail(20).mean()),

            "high_volume":
                latest["Volume"] >
                df["Volume"].tail(20).mean()
        }
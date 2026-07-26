import pandas as pd
import ta

from tools.yahoo_tool import YahooTool


class MarketAgent:

    def __init__(self):
        self.tool = YahooTool()

    def analyze(self, symbol):

        df = self.tool.get_historical_data(symbol)

        if df is None or len(df) < 60:
            return {
                "success": False,
                "message": "Not enough historical data."
            }

        close = df["Close"]
        high = df["High"]
        low = df["Low"]
        volume = df["Volume"]

        # ============================
        # Indicators
        # ============================

        rsi = ta.momentum.RSIIndicator(close).rsi().iloc[-1]

        macd_indicator = ta.trend.MACD(close)

        macd = macd_indicator.macd().iloc[-1]
        signal = macd_indicator.macd_signal().iloc[-1]

        sma20 = ta.trend.SMAIndicator(close, window=20).sma_indicator().iloc[-1]
        sma50 = ta.trend.SMAIndicator(close, window=50).sma_indicator().iloc[-1]

        ema20 = ta.trend.EMAIndicator(close, window=20).ema_indicator().iloc[-1]
        ema50 = ta.trend.EMAIndicator(close, window=50).ema_indicator().iloc[-1]

        bb = ta.volatility.BollingerBands(close)

        upper = bb.bollinger_hband().iloc[-1]
        lower = bb.bollinger_lband().iloc[-1]

        adx = ta.trend.ADXIndicator(
            high=high,
            low=low,
            close=close
        ).adx().iloc[-1]

        current_price = close.iloc[-1]

        avg_volume = volume.tail(20).mean()

        latest_volume = volume.iloc[-1]

        high_volume = latest_volume > avg_volume

        macd_bullish = macd > signal

        trend = "Bullish" if sma20 > sma50 else "Bearish"

        # ============================
        # Return Python types only
        # ============================

        return {

            "success": True,

            "current_price": float(current_price),

            "rsi": round(float(rsi), 2),

            "macd": round(float(macd), 2),

            "signal": round(float(signal), 2),

            "macd_bullish": bool(macd_bullish),

            "sma20": round(float(sma20), 2),

            "sma50": round(float(sma50), 2),

            "ema20": round(float(ema20), 2),

            "ema50": round(float(ema50), 2),

            "trend": trend,

            "uptrend": bool(sma20 > sma50),

            "bollinger_upper": round(float(upper), 2),

            "bollinger_lower": round(float(lower), 2),

            "adx": round(float(adx), 2),

            "volume": int(latest_volume),

            "average_volume": int(avg_volume),

            "high_volume": bool(high_volume)
        }
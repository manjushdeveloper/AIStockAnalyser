class RecommendationAgent:

    def analyze(self, financial, technical=None, sentiment=None):

        score = 50
        strengths = []
        risks = []

        # ====================================================
        # FUNDAMENTALS
        # ====================================================

        pe = financial.get("pe_ratio")
        peg = financial.get("peg_ratio")
        revenue = financial.get("revenue_growth")
        earnings = financial.get("earnings_growth")
        margin = financial.get("profit_margin")
        operating = financial.get("operating_margin")
        debt = financial.get("debt_to_equity")
        beta = financial.get("beta")
        dividend = financial.get("dividend_yield")

        analyst = financial.get("analyst_recommendation")
        target = financial.get("target_price")
        current = financial.get("current_price")

        # ---------------- PE ----------------

        if pe is not None:

            if pe < 20:
                score += 8
                strengths.append("Low PE ratio")

            elif pe < 30:
                score += 4

            else:
                score -= 5
                risks.append("High valuation")

        # ---------------- PEG ----------------

        if peg is not None:

            if peg < 1:
                score += 10
                strengths.append("Excellent PEG ratio")

            elif peg < 1.5:
                score += 5

            else:
                score -= 5

        # ---------------- Revenue ----------------

        if revenue is not None:

            if revenue > 20:
                score += 8
                strengths.append("Strong revenue growth")

            elif revenue > 10:
                score += 5

            elif revenue < 0:
                score -= 8
                risks.append("Revenue declining")

        # ---------------- Earnings ----------------

        if earnings is not None:

            if earnings > 15:
                score += 8
                strengths.append("Strong earnings growth")

            elif earnings > 0:
                score += 4

            else:
                score -= 8
                risks.append("Earnings declining")

        # ---------------- Profit Margin ----------------

        if margin is not None:

            if margin > 15:
                score += 6

            elif margin < 5:
                score -= 6

        # ---------------- Operating Margin ----------------

        if operating is not None:

            if operating > 15:
                score += 5

        # ---------------- Debt ----------------

        if debt is not None:

            if debt < 30:
                score += 6
                strengths.append("Low debt")

            elif debt < 60:
                score += 2

            else:
                score -= 6
                risks.append("High debt")

        # ---------------- Beta ----------------

        if beta is not None:

            if beta < 1:
                score += 4
                strengths.append("Low volatility")

        # ---------------- Dividend ----------------

        if dividend is not None and dividend > 0:

            score += 3
            strengths.append("Dividend paying company")

        # ---------------- Analyst Recommendation ----------------

        if analyst == "strong_buy":
            score += 12
            strengths.append("Analysts recommend Strong Buy")

        elif analyst == "buy":
            score += 8

        elif analyst == "sell":
            score -= 8

        # ---------------- Target Price ----------------

        if target and current:

            upside = ((target-current)/current)*100

            if upside > 20:
                score += 10
                strengths.append(
                    f"Target price implies {round(upside,1)}% upside"
                )

            elif upside > 10:
                score += 5

        # ====================================================
        # TECHNICALS
        # ====================================================

        if technical:

            rsi = technical.get("rsi")
            trend = technical.get("trend")
            macd = technical.get("macd_bullish")
            adx = technical.get("adx")
            volume = technical.get("high_volume")

            if rsi is not None:

                if 40 <= rsi <= 60:
                    score += 4
                    strengths.append("Healthy RSI")

                elif rsi < 30:
                    score += 8
                    strengths.append("Oversold")

                elif rsi > 70:
                    score -= 6
                    risks.append("Overbought")

            if macd:
                score += 8
                strengths.append("Bullish MACD")

            else:
                score -= 5
                risks.append("Bearish MACD")

            if trend == "Bullish":
                score += 8
                strengths.append("Uptrend")

            else:
                score -= 6
                risks.append("Downtrend")

            if adx is not None:

                if adx > 25:
                    score += 5
                    strengths.append("Strong trend")

            if volume:
                score += 4
                strengths.append("High buying volume")

        # ====================================================
        # SENTIMENT
        # ====================================================

        if sentiment:

            overall = sentiment.get("overall")
            news_score = sentiment.get("score",0)

            if overall == "Positive":
                score += 8

            elif overall == "Neutral":
                score += 2

            elif overall == "Negative":
                score -= 8

            score += int(news_score/20)

        # ====================================================

        score = max(0, min(100, score))

        # ====================================================

        if score >= 85:
            recommendation = "STRONG BUY"

        elif score >= 70:
            recommendation = "BUY"

        elif score >= 55:
            recommendation = "HOLD"

        elif score >= 40:
            recommendation = "REDUCE"

        else:
            recommendation = "SELL"

        return {

            "overall_score": score,

            "confidence": score,

            "recommendation": recommendation,

            "strengths": strengths,

            "risks": risks
            

        }
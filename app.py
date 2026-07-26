import streamlit as st

from agents.financial_agent import FinancialAgent
from agents.market_agent import MarketAgent
from agents.news_agent import NewsAgent
from agents.sentiment_agent import SentimentAgent
from agents.report_agent import ReportAgent

st.set_page_config(
    page_title="AI Stock Analyser",
    page_icon="📈",
    layout="wide"
)

st.title("📈 AI Powered Stock Analyser")

st.write("Analyze Indian stocks using AI.")

stock = st.text_input(
    "Enter Stock Symbol",
    "RELIANCE"
).upper()

if st.button("Analyze"):

    with st.spinner("Analyzing..."):

        financial = FinancialAgent().analyze(stock)

        technical = MarketAgent().analyze(stock)

        sentiment = SentimentAgent().analyze(stock)

        report = ReportAgent().generate(
            financial,
            technical,
            sentiment
        )

    st.success("Analysis Completed")

    st.divider()

    st.subheader(report["company"])

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Current Price",
        f"₹ {report['current_price']}"
    )

    col2.metric(
        "Recommendation",
        report["recommendation"]
    )

    col3.metric(
        "AI Score",
        f"{report['overall_score']}/100"
    )

    st.divider()

    st.subheader("Financial Summary")

    st.write(report["financial_summary"])

    st.divider()

    st.subheader("Technical Analysis")

    st.write(report["technical_summary"])

    st.divider()

    st.subheader("Strengths")

    for item in report["strengths"]:
        st.success(item)

    if "risks" in report:

        st.subheader("Risks")

        for item in report["risks"]:
            st.error(item)

    st.divider()

    st.subheader("News Sentiment")

    sentiment_data = report["sentiment_summary"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Overall",
            sentiment_data.get("overall_sentiment", "N/A")
    )

    col2.metric(
        "Score",
        sentiment_data["score"]
    )

    col3.metric(
        "Positive",
        sentiment_data["positive"]
    )

    col4.metric(
        "Negative",
        sentiment_data["negative"]
    )

    st.divider()

    st.subheader("News Articles")

    for article in sentiment_data["articles"]:

        with st.expander(article.get("title", "News")):

            st.write("Publisher:", article.get("publisher"))

            st.write("Sentiment:", article.get("sentiment"))

            st.write("Confidence:", article.get("confidence"))

            st.write("Reason:")

            st.write(article.get("reason"))
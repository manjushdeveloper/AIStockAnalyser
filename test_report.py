from pprint import pprint

from agents.financial_agent import FinancialAgent
from agents.technical_agent import TechnicalAgent
from agents.sentiment_agent import SentimentAgent
from agents.report_agent import ReportAgent

symbol = "RELIANCE"

financial = FinancialAgent().analyze(symbol)

technical = TechnicalAgent().analyze(symbol)

sentiment = SentimentAgent().analyze(symbol)

report = ReportAgent().generate(
    financial,
    technical,
    sentiment
)

pprint(report)
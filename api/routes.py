from fastapi import APIRouter

from api.schemas import StockRequest
from agents.financial_agent import FinancialAgent
from agents.market_agent import MarketAgent
from agents.sentiment_agent import SentimentAgent
from agents.report_agent import ReportAgent

router = APIRouter()


@router.post("/analyze")
def analyze_stock(request: StockRequest):

    symbol = request.symbol.upper()

    financial = FinancialAgent().analyze(symbol)

    technical = MarketAgent().analyze(symbol)

    sentiment = SentimentAgent().analyze(symbol)

    report = ReportAgent().generate(
        financial,
        technical,
        sentiment
    )

    return report
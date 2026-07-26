from pydantic import BaseModel


class StockRequest(BaseModel):
    symbol: str


class StockResponse(BaseModel):
    company: str
    symbol: str
    recommendation: str
    overall_score: float
    confidence: float
    current_price: float
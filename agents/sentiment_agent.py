
from google import genai
from dotenv import load_dotenv
import os, json
from tools.yahoo_tool import YahooTool

load_dotenv()

class SentimentAgent:
    def __init__(self):
        self.yahoo=YahooTool()
        self.client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def analyze(self,symbol):
        news=self.yahoo.get_news(symbol)
        if not news:
            return {"success":False,"overall":"Neutral","score":0,"positive":0,"neutral":0,"negative":0,"articles":[]}
        news_text=""
        for i,a in enumerate(news,1):
            news_text+=f"Article {i}\nTitle:{a.get('title','')}\nPublisher:{a.get('publisher','')}\nSummary:{a.get('summary','')}\n\n"
        prompt=f'''You are an expert financial analyst.
Analyze ALL news and return ONLY JSON:
{{"articles":[{{"title":"","publisher":"","sentiment":"Positive","confidence":90,"reason":"Short explanation"}}]}}
News:
{news_text}
'''
        try:
            resp=self.client.models.generate_content(model="gemini-2.5-flash",contents=prompt)
            txt=resp.text.replace("```json","").replace("```","").strip()
            result=json.loads(txt)
            articles=result.get("articles",[])
        except Exception as e:
            articles=[{"title":a.get("title",""),"publisher":a.get("publisher",""),"sentiment":"Neutral","confidence":50,"reason":str(e)} for a in news]
        pos=sum(1 for x in articles if x["sentiment"].lower().startswith("positive"))
        neg=sum(1 for x in articles if x["sentiment"].lower().startswith("negative"))
        neu=len(articles)-pos-neg
        score=round((pos/max(len(articles),1))*100,2)
        overall="Positive" if score>=70 else "Neutral" if score>=40 else "Negative"
        return {"success":True,"overall":overall,"score":score,"positive":pos,"neutral":neu,"negative":neg,"articles":articles}

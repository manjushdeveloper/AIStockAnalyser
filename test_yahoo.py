from tools.yahoo_tool import YahooTool

tool = YahooTool()

data = tool.get_company_details("RELIANCE")

if data:
    for key, value in data.items():
        print(f"{key:25}: {value}")
else:
    print("Unable to fetch data.")
import yfinance as yf
import pandas as pd
from datetime import datetime

etfs = {
    "VFV": "VFV.TO",
    "XIT": "XIT.TO",
    "TEC": "TEC.TO",
    "ZEA": "ZEA.TO",
    "XSU": "XSU.TO"
}

results = []

for name, ticker in etfs.items():

    data = yf.download(
        ticker,
        period="3mo",
        interval="1d",
        auto_adjust=True,
        progress=False
    )

    close = data["Close"]

    price = float(close.iloc[-1])

    sma20 = float(
        close.rolling(20).mean().iloc[-1]
    )

    change_1m = (
        price / float(close.iloc[-22]) - 1
    ) * 100

    results.append({
        "ETF": name,
        "Close": round(price,2),
        "SMA20": round(sma20,2),
        "Above SMA20": price > sma20,
        "1M Change %": round(change_1m,2)
    })


df = pd.DataFrame(results)

print("ETF Weekly Report")
print(datetime.now())

print(df.to_string(index=False))

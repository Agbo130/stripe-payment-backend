import requests
import random

def fetch_price(symbol_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol_id}&vs_currencies=usd"
    response = requests.get(url).json()
    return response[symbol_id]["usd"]

def generate_crypto_signal():
    coin = random.choice([
        {"id": "bitcoin", "symbol": "BTC/USD"},
        {"id": "ethereum", "symbol": "ETH/USD"},
        {"id": "ripple", "symbol": "XRP/USD"}
    ])
    price = fetch_price(coin["id"])
    direction = random.choice(["Buy", "Sell"])

    sl = price - random.uniform(30, 100) if direction == "Buy" else price + random.uniform(30, 100)
    tp = price + random.uniform(50, 150) if direction == "Buy" else price - random.uniform(50, 150)

    return {
        "pair": coin["symbol"],
        "price": price,
        "signal": direction,
        "entry": round(price, 2),
        "stop_loss": round(sl, 2),
        "take_profit": round(tp, 2)
    }

import random

def generate_crypto_signal():
    symbol = random.choice(["BTC/USD", "ETH/USD", "XRP/USD"])
    direction = random.choice(["Buy", "Sell"])
    entry = round(random.uniform(1000, 30000), 2)
    sl = entry - 100 if direction == "Buy" else entry + 100
    tp = entry + 200 if direction == "Buy" else entry - 200
    return {
        "pair": symbol,
        "signal": direction,
        "entry": entry,
        "stop_loss": sl,
        "take_profit": tp
    }

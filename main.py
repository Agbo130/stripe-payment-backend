from fastapi import FastAPI
from signal_logic import generate_crypto_signal
from stripe_payment import app as stripe_app

app = FastAPI()
app.mount("/", stripe_app)

@app.get("/public-signal")
def public():
    return {"signal": generate_crypto_signal()}

@app.get("/vip-signal")
def vip():
    return {
        "vip": True,
        "signal": generate_crypto_signal(),
        "message": "You are viewing VIP signals"
    }

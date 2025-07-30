import os
from fastapi import FastAPI
from stripe_payment import app as stripe_app
from signal_logic import generate_crypto_signal

app = FastAPI()
app.mount("/stripe", stripe_app)

@app.get("/")
def root():
    return {"message": "Crypto Signal App Running"}

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

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

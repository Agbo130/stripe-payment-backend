from fastapi import FastAPI
import stripe
import os
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Allow all origins (adjust for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Stripe Secret Key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

@app.get("/")
def home():
    return {"message": "Stripe Payment API is live"}

@app.post("/create-checkout-session")
def create_checkout_session():
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "usd",
                    "unit_amount": 1000,  # $10
                    "product_data": {
                        "name": "VIP Signal Access",
                    },
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="https://yourwebsite.com/success",
            cancel_url="https://yourwebsite.com/cancel",
        )
        return {"checkout_url": session.url}
    except Exception as e:
        return {"error": str(e)}

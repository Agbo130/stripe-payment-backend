import React from "react";
import axios from "axios";

function App() {
  const handleBuy = async () => {
    try {
      const response = await axios.post("http://localhost:8002/stripe/create-checkout-session");
      window.location.href = response.data.checkout_url;
    } catch (error) {
      console.error("Payment failed:", error);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Crypto VIP Signal</h1>
      <button
        onClick={handleBuy}
        style={{
          padding: "12px 24px",
          fontSize: "18px",
          backgroundColor: "#6772E5",
          color: "white",
          border: "none",
          borderRadius: "6px",
          cursor: "pointer"
        }}
      >
        Buy VIP Access with Stripe 💳
      </button>
    </div>
  );
}

export default App;

from fastapi import FastAPI
from pydantic import BaseModel
import os

app = FastAPI()

# Modèle du body JSON
class SymbolRequest(BaseModel):
    symbol: str
    price: float

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render"}

@app.post("/predict")
def predict(request: SymbolRequest):
    signal = "BUY"
    confidence = 0.75

    if signal == "BUY":
        stop_loss = request.price * (1 - 0.005)   # -0.5%
        take_profit = request.price * (1 + 0.02)  # +2%
    else:
        stop_loss = request.price * (1 + 0.005)   # +0.5%
        take_profit = request.price * (1 - 0.02)  # -2%

    return {
        "symbol": request.symbol,
        "price": request.price,
        "signal": signal,
        "confidence": confidence,
        "stop_loss": round(stop_loss, 5),
        "take_profit": round(take_profit, 5)
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
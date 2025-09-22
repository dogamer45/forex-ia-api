from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import os

app = FastAPI()

# Modèle pour la requête
class PredictRequest(BaseModel):
    symbol: str
    price: float

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render"}

@app.post("/predict")
def predict(request: PredictRequest):
    return {
        "symbol": request.symbol,
        "price": request.price,
        "signal": "BUY",
        "confidence": 0.75,
        "stop_loss": 1.0945,
        "take_profit": 1.122,
        "timestamp": datetime.utcnow().isoformat()  # <-- ajout du timestamp
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI on Render"}

@app.post("/predict")
def predict(symbol: str):
    return {"signal": "BUY", "confidence": 0.75, "symbol": symbol}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

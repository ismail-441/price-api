from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pricing import final_price

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Pricing API is alive"}


@app.get("/price")
def get_price(base_price: float, discount_percent: float, tax_percent: float):
    result = final_price(base_price, discount_percent, tax_percent)
    return {"final_price": result}
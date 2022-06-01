import pandas as pd
df = pd.read_csv("eda.csv")
df.sample(3)

from typing import List
from fastapi import FastAPI, Query
app = FastAPI(
    title="My lovely API"
    )

@app.get("/")
def root()->dict:
    return{"message": "Hello world!"}

@app.get("/items/")
def read_items(q: List[int] = Query(None)):
    return {"q": q}

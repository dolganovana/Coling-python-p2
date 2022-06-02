import pandas as pd
df = pd.read_csv("eda.csv")

from typing import List
from fastapi import FastAPI, Query
app = FastAPI(
    title="Recipes Dolganova"
    )

@app.get("/")
def root()->dict:
    return{"message": "Hello!"}

@app.get("/items/")
def read_items(q: List[int] = Query(None)):
    return {"q": q}

@app.get('/recipes/diet/')
def recipes_by_calories(calories: int, top_n: int) -> dict:
    suitable = df[df['cal'] <= calories]
    top_sorted = suitable.sort_values(by='cal').head(top_n)
    logger.info(f"{top_n} most suitable recipes under {calories} calories successfully fetched")
    return top_sorted.to_dict(orient='index')

@app.get('/recipes/')
def recipes_by_difficulty(difficulty: str, top_n: int) -> dict:
    ascending = True if difficulty == 'simple' else False
    new_df = pd.DataFrame().assign(id = df['id'], name = df['name'], steps = df['list_resipe'])
    new_df['difficulty'] = new_df.apply(lambda row: len(row.steps), axis=1)
    new_df.drop('steps', axis=1)
    top_sorted = new_df.sort_values(by='difficulty', ascending=ascending).head(top_n)
    return top_sorted.to_dict(orient='index')

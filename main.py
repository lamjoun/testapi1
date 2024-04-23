from fastapi import FastAPI
from fastapi.param_functions import Depends

V = 100
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "===Hello World==="}

@app.get("/valeur_v")
async def valeur_v():
    return {"message": f"La variable V est : {V}"}

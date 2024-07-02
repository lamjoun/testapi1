import uvicorn
from fastapi import FastAPI

V = 100
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "===Hello World==="}

@app.get("/valeurv")
async def valeurv():
    return {"message": f"La variable V est : {V}"}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=int(os.environ.get('PORT', 8888)))

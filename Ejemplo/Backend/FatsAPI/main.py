from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "!Hello World¡å"}

@app.get("/url")
async def root():
    return {"message": "Nueva ruta "}
from fastapi import FastAPI

app = FastAPI()

@app.get("/api-endpoint") 
async def fast_api():
    return {'message': 'Hello, Jeremy'}
import uvicorn
from fastapi import FastAPI
from routes import ocr, translation

app = FastAPI()

# Include routes
app.include_router(ocr.router)
app.include_router(translation.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

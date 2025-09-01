from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Chat service is running 🚀"}
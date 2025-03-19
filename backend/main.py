from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.generate_recipe import router as recipe_router

app = FastAPI()

# Allow requests from frontend (adjust origin in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Dice Recipe API is running!"}

app.include_router(recipe_router, prefix="/api")
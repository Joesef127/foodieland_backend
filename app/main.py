from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models, database
from .routes import recipe


# Initialize the FastAPI app
app = FastAPI()

# Allow CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)
# Include the database dependency
@app.get("/")
async def root():
    return {"message": "Welcome to the Recipe API!"}

# Include the recipe router
app.include_router(recipe.router)


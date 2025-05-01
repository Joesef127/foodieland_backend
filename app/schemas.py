from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    time: int
    type: str
    image: str
    isFavorite: bool

class CreateRecipe(Recipe):
    id: int

    class Config:
        orm_mode = True
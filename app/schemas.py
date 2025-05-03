from pydantic import BaseModel
from typing import Optional, Union
from fastapi import UploadFile

class Recipe(BaseModel):
    id: Optional[int] = None
    name: str
    time: int
    category: str
    image: Optional[Union[UploadFile, str]] = None  
    isFavorite: Optional[bool] = None
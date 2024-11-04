import datetime
from typing import Optional
from pydantic import BaseModel, Field, validator


class Movie(BaseModel):
    id: Optional[int]=None # puede ser opcional o un valor entero
    title:str
    overview:str
    year:int
    rating:float
    category:str
class MovieUpdate(BaseModel):
    title:str
    overview:str
    year:int
    rating:float
    category:str
class MovieCreate(BaseModel):
    id: int
    title: str= Field(min_length=5,max_length=15)
    overview:str=Field(min_length=5,max_length=50)
    year:int=Field(le=datetime.date.today().year,ge=1924)
    rating:float = Field(ge=0, le=10)
    category:str =Field(min_length=5,max_length=20)
    model_config={
        "json_schema_extra":{
            "example":{
                "id":1,
                "title":"My Movie",
                "overview":"This movie is about ...",
                "year":2024,
                "rating":5,
                "category": "Action"               
            }
        }
    }
    @validator("title")
    def validate_title(cls, value):
        if len(value)<5:
            raise ValueError("Title field must be less than 5 char")
        if len(value)>15:
            raise ValueError("Title field must be greater than 15 char")

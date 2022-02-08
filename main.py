#python
from typing import Optional
from enum import Enum


#pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path


app = FastAPI()


#Models

class HairColor(Enum):
    white= "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"

class Location(BaseModel):
    city: str
    state: str
    country: str

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="FAcundo"
        )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Torres"
        )
    age: int = Field(
        ..., 
        gt=0,
        le=115,
        example =21
        )
    hail_color: Optional[HairColor] = Field(default=None, example="black")
    is_married: Optional[bool] = Field(default=None, example=False)

   # class Config:
    #    schema_extra = {
   #         "example": {
   #             "first_name": "Facudno",
    #            "last_name": "Garcia",
   #             "age": 21,
   #             "hair_color": "black",
   #             "is_married": "true"
   #         }
    #    } 






@app.get('/')
def home():
    return {"Hello": "World"}


#Request and Response

@app.post('/person/new')
def create_person(person: Person = Body(...)):
    return person


#validations query parameters

@app.get('/person/detail')
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1,
        max_length=50,
        title ="Person name",
        description= "Description title name"
    ),
    age: int = Query(...)
):
    return {name: age}


#validations path parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(..., gt=0) #mayor a cero
):
    return {person_id: "It exists!"}


#validations request body
# no funciona elf astdoc con dos body request para el caso del schema_extra
@app.put('/person/{person_id}')
def update_person(
    person_id: int = Path(
        ..., 
        title = "Person ID",
        description ="This is the person id",
        gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results



#python
from typing import Optional

#pydantic
from pydantic import BaseModel


#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query


app = FastAPI()


#Models


class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hail_color: Optional[str] = None
    is_married: Optional[bool] = None





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
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: int = Query(...)
):
    return {name: age}
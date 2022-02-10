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

class Employee(BaseModel):
    id_employee_unique: int = Field(
        ..., 
        gt=0,
        le=115,
        example =21
        )
    name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="FAcundo"
        )
    image_photo_employee_work: str = Field(
        ..., 
        min_length=1,
        max_length=150,
        example ="/images/man.jpeg"
        )        

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
    password: str = Field(
        ...,
        min_length=8
    )

class PersonOut(BaseModel):
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

@app.post('/person/new', response_model=PersonOut)
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
        description= "Description title name",
        example="Rocio"
    ),
    age: int = Query(
        ...,
        title="Person Age",
        description="This is a person age. It's required",
        example=25
    )
):
    return {name: age}


#validations path parameters

@app.get('/person/detail/{person_id}')
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        example= 123
    ) #mayor a cero
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



@app.get('/employee')
def get_employee():

    list = [] 
  
    # appending instances to list 
    list.append( Employee(id_employee_unique=1,name='Juan Perez', image_photo_employee_work='https://employee.setcoding.com/images/man.jpg') )
    list.append( Employee(id_employee_unique=2,name='María Lopez', image_photo_employee_work= 'https://employee.setcoding.com/images/woman.jpg') )
    list.append( Employee(id_employee_unique=3,name='Mario Rosas',  image_photo_employee_work='https://employee.setcoding.com/images/man.jpg') )
    list.append( Employee(id_employee_unique=4,name='Guadalupe Rojas',  image_photo_employee_work='https://employee.setcoding.com/images/woman.jpg') )
    list.append( Employee(id_employee_unique=5,name='Miguel Castro',  image_photo_employee_work='https://employee.setcoding.com/images/man.jpg') )
    list.append( Employee(id_employee_unique=6,name='Raquel Martinez ',  image_photo_employee_work='https://employee.setcoding.com/images/woman.jpg') )
    list.append( Employee(id_employee_unique=7,name='Sergio de Dulce',  image_photo_employee_work='https://employee.setcoding.com/images/man.jpg') )
    list.append( Employee(id_employee_unique=8,name='Dulce Adriana',  image_photo_employee_work='https://employee.setcoding.com/images/woman.jpg') )
    list.append( Employee(id_employee_unique=9,name='Alejandro Villanueva',  image_photo_employee_work='https://employee.setcoding.com/images/man.jpg') )
    list.append( Employee(id_employee_unique=10,name='Patricia Drako',  image_photo_employee_work='https://employee.setcoding.com/images/woman.jpg') )

   # results = list.dict()
    return {"employee":list}
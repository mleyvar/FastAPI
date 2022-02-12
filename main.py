#python
from typing import Optional
from enum import Enum


#pydantic
from pydantic import BaseModel, EmailStr
from pydantic import Field
from pydantic import EmailStr

#FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form, Header, Cookie


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

class PersonBase(BaseModel):
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

class Person(PersonBase):
   password: str = Field(
        ...,
        min_length=8
    )
    
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

class Product(BaseModel):
    id_product_unique: int = Field(..., gt=0, le=115, example =21 )
    name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example ="FAcundo"
    )
    price: float
    discount: float
    image_photo_product_work: str = Field(
        ..., 
        min_length=1,
        max_length=150,
        example ="/images/man.jpeg"
        )
    stock: int            



class PersonOut(PersonBase):
    pass

class LoginOut(BaseModel):
    username: str = Field(..., max_length=20, example= "Miguel2022")
    message: str = Field(default= "Login succesfully")


@app.get(
    path='/',
    status_code=status.HTTP_200_OK
    )
def home():
    return {"Hello": "World"}


#Request and Response

@app.post(
    path='/person/new', 
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED
    )
def create_person(person: Person = Body(...)):
    return person

#validations query parameters

@app.get(
    path='/person/detail',
    status_code=status.HTTP_200_OK
    )
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

@app.get(
    path='/person/detail/{person_id}',
    status_code=status.HTTP_200_OK
    )
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
@app.put(
    path='/person/{person_id}',
    status_code=status.HTTP_200_OK
    )
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



@app.get(
    path='/employee',
    status_code=status.HTTP_200_OK
    )
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


  
@app.get(
    path='/product',
    status_code=status.HTTP_200_OK
    )
def get_product():

    list = [] 
  
    # appending instances to list 
    list.append( Product(id_product_unique=1,name='Producto 1', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod1.jpg', stock=100) )
    list.append( Product(id_product_unique=2,name='Producto 2', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod2.jpg', stock=100) )
    list.append( Product(id_product_unique=3,name='Producto 3', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod3.jpg', stock=100) )
    list.append( Product(id_product_unique=4,name='Producto 4', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod1.jpg', stock=100) )
    list.append( Product(id_product_unique=5,name='Producto 5', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod2.jpg', stock=100) )
    list.append( Product(id_product_unique=6,name='Producto 6', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod3.jpg', stock=100) )
    list.append( Product(id_product_unique=7,name='Producto 7', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod1.jpg', stock=100) )
    list.append( Product(id_product_unique=8,name='Producto 8', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod2.jpg', stock=100) )
    list.append( Product(id_product_unique=9,name='Producto 9', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod3.jpg', stock=100) )
    list.append( Product(id_product_unique=10,name='Producto 10', price=10.0, discount=0.0, image_photo_product_work='https://employee.setcoding.com/images/prod1.jpg', stock=100) )

   # results = list.dict()
    return {"product":list}  


# forms

@app.post(
    path='/login',
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return LoginOut(username=username)


# cookies and headers parameters

@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str = Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(...),
    message: str = Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)

):
    return user_agent

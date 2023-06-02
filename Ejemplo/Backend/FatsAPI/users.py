from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#inicia el servidor: uvicorn users:app --reload

@app.get("/usersjson")
async def usersjson():
    return [
        {"name":"Esteban", "Surname":"Sanchez","url":"https://tete.dev", "age":36},
        {"name":"Inocencio", "Surname":"Scotf","url":"https://info.com", "age":23},
        {"name":"Arlin", "Surname":"Vasquez","url":"https://lele.com", "age":33}
    ]
 
#Entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int
    id: int

users_list = [User(id=1, name="Esteban", surname="Sanchez", url="http://lelo.com", age=36),
              User(id=2, name="steven", surname="San", url="http://lkj.net",age=30),
               User(id=3, name="Ino", surname="Sanchez",url="http://leo.tv",age=23)]

#path
@app.get("/user/{id}")
async def user(id:int):
   return search_user(id)

#query
@app.get("/userquery")
async def user(id:int):
   return search_user(id)


def search_user(id: int):
     users = filter(lambda user: user.id == id, users_list)
     try:
       return list(users)[0]
     except:
       return {"error":"No se ha encontrado el usuario."}
from fastapi import FastAPI,HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
import bcrypt
import jwt
import secrets
from datetime import datetime , timezone , timedelta
from typing import Annotated



app_nueva= FastAPI()

JWT_SECRET= "67c5efdcfee96ba4bb34a008c5776501182dead5f80ac5767085fc3d823c7156" # Firma del token , con esto si se cambia el email se sabe que no coincide y tira error
JWT_ALGORITHM= "HS256"
oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/login") #Es el que mira el Header.Si la peticion no tiene el header lanza un error.

class user(BaseModel):
    user_name:str
    email:EmailStr
    password:str

class login_user(BaseModel):
    email:EmailStr
    password:str

class Task(BaseModel):
    title: str
    description: str

def sign(email):
    now_utc= datetime.now(timezone.utc)
    new_time= now_utc + timedelta(minutes=15)
    payload={
        "email": email,
        "exp": new_time
    }
    token= jwt.encode(payload,JWT_SECRET, algorithm= JWT_ALGORITHM)

    return token


users={}
contador=0
@app_nueva.post("/users")
def register_user(data_user:user):
    global contador
    for u in users.values():
        if u["email"] == data_user.email:
            return {"Menssage": "This email has been registred"}

    #Convertir la contraseña de texto plano a bytes y hashearla
    password_bytes=data_user.password.encode("utf-8")
    salt=bcrypt.gensalt()
    password_hash=bcrypt.hashpw(password_bytes,salt)

    contador += 1
    user_data={
        "user_name":data_user.user_name,
        "email":data_user.email,
        "password_hash": password_hash.decode("utf-8")  # Paso la contraseña de byte a string
    }

    users[contador]=user_data

    return {"Menssage": f"The user has been registered successful"}


@app_nueva.post("/login")
def login(user_data:Annotated[OAuth2PasswordRequestForm, Depends()]):
    found=None  #No esta encontrado el usuario
    for u in users.values(): # Buscamos al usuario en el diccionario
        if u["email"] == user_data.username:  # Si el email que se busca coincide con uno que esta
            found= u  # encontrado es el usuario
            break
    if found is None: # Si no se lo encuentra
        raise HTTPException(
            status_code=401,
            detail= "Invalid credentials" #Error credenciales invalidas
        )
    
    password_bytes=user_data.password.encode("utf-8") #Pongo a byte la contraseña
    stored_hash_bytes= found["password_hash"].encode("utf-8") # Pongo a byte la contraseña hasheada del usuario
    is_valid=bcrypt.checkpw(password=password_bytes, hashed_password=stored_hash_bytes) # Aca se compara los dos hash, la contraseña escrita y la contraseña guardada


    if not is_valid: #Si no es valida
        raise HTTPException(  
            status_code=401,
            detail="Invalid credentials" # Error credencial invalida
        )
    token=sign(user_data.username)

    return {
        "access_token":token,
        "token_type": "bearer"
    }

def  get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    found=None
    try:
        payload=jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM]) #En algorithms va una lista
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=401,
            detail="Expiro el tiempo"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=401,
            detail="Token invalido"
        )

    email=payload.get("email")
    for u in users.values():
        if u["email"] == email:
            found= u
            break
    if found is None:
        raise HTTPException(
        status_code=401,
        detail= "Invalid credential"
    )

    return found 

    
@app_nueva.get("/me")                                                     #El Depends dice "Antes de ejecutar la funcion ejecuta el oauth2_scheme"
def analizar_token(usuario: Annotated[dict, Depends(get_current_user)]):  #El Annoted dice el tipo de parametro que espero y despues de donde sacarlo que seria el Depends
   return {
       "user_name": usuario["user_name"],
       "email": usuario["email"]
   }


dictionary_task={}
counter_tasks=0
@app_nueva.post("/task")
def task_client(user: Annotated[dict, Depends(get_current_user)] , task:Task):
    global counter_tasks
    counter_tasks += 1

    task_data= {
        "title": task.title,
        "description": task.description,
        "email_owner": user["email"]
    }

    dictionary_task[counter_tasks]= task_data

    return {"Messagge":"The task has been created successfully"}


@app_nueva.get("/task")
def get_task(user:Annotated[dict , Depends(get_current_user)]):
    tasks=[]
    for u in dictionary_task.values():
        if u["email_owner"] == user["email"]:
            tasks.append(u)
    return tasks
            

    
    
        


        

    









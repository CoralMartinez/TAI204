#importaciones

from fastapi import FastAPI, status, HTTPException, Depends #Depends: Configuración de proteccción


import asyncio  

from typing import Optional

from pydantic import BaseModel, Field


from fastapi.middleware.cors import CORSMiddleware

#Librerías OAuth2 para autorización

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

#Librería para JWT
from jose import JWTError, jwt
from datetime import datetime, timedelta

#Instancia del servidor

app =  FastAPI(
    title = "Mi primer API" ,
    description = "Coral Martínez Silvestre" ,
    version = "1.0"
)

#API de Sistema para gestionar lo turnos bancarios que permite: 10: API para gestionar los turnos bancarios que permite:"
#CREAR turno, listar turnos, consultar por ID, marcar como atendido, eliminar turno. 11. MODELO DE DATOS OBLIGATORIOS
#cliente: mínimo 8 caracteres, tipo tramite: depósito, retiro o consulta, fecha de turno futura entre: 09:00 a.m. y 03:00 p.m.
#no permitir más de 5 turnos por día a 1 cliente.

#12. RUTAS PROTEGIDAS CON USUARIO: banco y contraseña: 2468
#Marcar como atendido y eliminar turno

#Preparar y probar todos los endopoints en Postman para su rápida revisión, no es válido entregar en cualquier otra herramienta


#CREAR LA FastAPI o contenedor Docker

#CORS
# BACKEND Y FRONTEND FUNCIONAN 
# EVITAR BLOQUEO DE PETICIONES

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#TABLA FICTICIA

usuarios = [
    {"id":1, "nombre":"Sofía", "tipo":21, "fecha":"2026-03-12"},
    {"id":2, "nombre":"Federico", "tipo":21, "fecha":"2026-03-12"},
    
]


#-------------------------------------------------------------------------------------------
#Configuración de OAuth2 y JWT
#-------------------------------------------------------------------------------------------


SECRET_KEY = "clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#CREAR TOKEN

def crear_token(data: dict):

    datos = data.copy()

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    datos.update({"exp": expire})

    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)

    return token

#ENDPOINT LOGIN 

@app.post("/token", tags=["Autenticación"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    username = form_data.username
    password = form_data.password

    if username != "coral" or password != "123456":
        raise HTTPException(
            status_code=401,
            detail="Credenciales incorrectas"
        )

    access_token = crear_token({"sub": username})

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

#VALIDAR TOKEN

def verificar_token(token: str = Depends(oauth2_scheme)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        usuario = payload.get("sub")

        if usuario is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        return usuario

    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado"
        )


#-------------------------------------------------------------------------------------------
#Modelo Pydantic de validacion
#-------------------------------------------------------------------------------------------

class crear_usuario(BaseModel):
    id:int = Field(...,gt=0, description="identificador  de usuario")
    nombre:str = Field(...,min_length=3, max_length=50, example="Patroclo")
    edad:int = Field(...,ge=1, le=125, description="Edad valida de 1 a 125")

#Endpoints

#--->Rutas

@app.get("/", tags = ["Inicio"])
async def bienvenido():
    return {"mensaje":"Bienvenido a FastAPI para gestionar los turnos bancarios"}


@app.get("/v1/usuarios/", tags=["CRUD HTTP"])
async  def consultaT():
    return{
        "status":"200",
        "total": len(usuarios),
        "Usuarios":usuarios
    }
    
    
@app.post("/v1/usuarios/", tags=["CRUD HTTP"])
async def agregar_usuario(usuario:crear_usuario): 
    for usr in usuarios:
        if usr["id"] == usuario.id: 
            raise HTTPException(
                status_code = 400, #Error de lado del Cliente
                detail = "El turno ya existe"
            )
            
    usuarios.append(usuario)
    return{
        "Mensaje":"Turno agregado", 
        "Usuario":usuario,
        "Status":"200"
    }
    
@app.put("/v1/usuarios/{id}", tags=["CRUD HTTP"])
async def actualizar_usuario(
    id: int,
    usuario: dict,
    usuarioAuth: str = Depends(verificar_token)
):

    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario)

            return {
                "Mensaje": f"Datos actualizados por {usuarioAuth}",
                "Usuario": usr,
                "Status": "200"
            }

    raise HTTPException(
        status_code=400,
        detail="El turno no ha sido encontrado"
    )
  
  
@app.delete("/v1/usuarios/{id}", tags=["CRUD HTTP"])
async def eliminar_usuario(
    id: int,
    usuarioAuth: str = Depends(verificar_token)
):

    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)

            return {
                "Mensaje": f"Se ha eliminado el turno por{usuarioAuth}",
                "Usuario": usr,
                "Status": "200"
            }

    raise HTTPException(
        status_code=400,
        detail="El turno no ha sido encontrado"
    )
            
    
    #BACKEND
    # LEVANTAR SERVIDOR fastAPI
    # C:\TAI204>
    # #uvicorn miAPI.main:app --reload --port 5000
    
    #SI SE BORRA EL CONTENEDOR EN DOCKER
    #docker compose up --build
        
        
        
        
        
    
   
   
   
   
   
   
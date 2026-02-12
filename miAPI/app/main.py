#importaciones

from fastapi import FastAPI 

#librería: fastapi, clase: FastAPI

import asyncio  

from typing import Optional


#Instancia del servidor

app =  FastAPI(
    title = "Mi primer API" ,
    description = "Coral Martínez Silvestre" ,
    version = "1.0"
)

#TABLA FICTICIA

usuarios = [
    {"id":1, "nombre":"Diego", "edad":21},
    {"id":2, "nombre":"Coral", "edad":21},
    {"id":3, "nombre":"Saúl", "edad":21},
    {"id":4, "nombre":"María", "edad":21}
]




#Endpoints

#--->Rutas

#PRIMERA FUNCIÓN
@app.get("/")

#función asincrona: bienvenido

async def bienvenido():
    
    return {"mensaje":"Bienvenido a FastAPI "}

#JSON, REGRESA: IZQUIERDA: Clave/index  DERECHA: valor del mensaje
#{"correo":"correo@ejemplo.com"}

#SEGUNDA FUNCIÓN

@app.get("/holaMundo")

async def Hola():
    
    await asyncio.sleep(5)  # Simulación de una operación asíncrona
    #await---> petición, consulta a una BD, archivo
    
    return {
        "mensaje":"Hola Mundo FastAPI",
        "status":"200"
        }

#Endpoints

@app.get("/", tags = ["Inicio"])
async def bienvenido():
    return {"mensaje":"Bienvenido a FastAPI"}

@app.get("/holaMundo", tags = ["Asincronia"])
async def Hola():
    await asyncio.sleep(5)
    return {
        "mensaje":"Hola Mundo FastAPI",
        "status":"200"
    }
    
@app.get("/v1/usuario/{id}", tags = ["Parametro obligatorio"])
async def consultauno(id:int):
    
    return {
        "mensaje":"Usuario encontrado" ,
        "usuario":id ,
        "status":"200"
    }


@app.get("/v1/usuarios/", tags = ["Parametro opcional"])
async def consultatodos(id:Optional[int] = None):
    if id is not None:
        for usuarioK in usuarios:
            if usuarioK["id"] == id:
                
                return {
                    "mensaje":"Usuario encontrado" ,
                    "usuario":usuarioK ,
                    "status":"200"
                    }
                
        return{
            "mensaje":"Usuario no encontrado" ,
            "status":"200"
            
        }
    
    else: 
        return{
            "mensaje":"No se roporcionó un id"
        }









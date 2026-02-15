#importaciones

from fastapi import FastAPI, status, HTTPException

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
    
@app.get("/v1/ParametroOb/{id}", tags = ["Parametro obligatorio"])
async def consultauno(id:int):
    
    return {
        "mensaje":"Usuario encontrado" ,
        "usuario":id ,
        "status":"200"
    }


@app.get("/v1/ParametroOp/", tags = ["Parametro opcional"])
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

@app.get("/v1/usuarios/", tags=["CRUD HTTP"])
async  def consultaT():
    return{
        "status":"200",
        "total": len(usuarios),
        "Usuarios":usuarios
    }
    
    
@app.post("/v1/usuarios/", tags=["CRUD HTTP"])
async def agregar_usuario(usuario:dict): #diccionario de la BD ficticia
    for usr in usuarios:
        if usr["id"] == usuario.get("id"): #si es igual que lo que se está pidiendo
            raise HTTPException(
                status_code = 400, #Error de lado del Cliente
                detail = "El id ya existe"
            )
            
    usuarios.append(usuario)
    return{
        "Mensaje":"Usario agregado", 
        "Usuario":usuario,
        "Status":"200"
    }
    
    
@app.put("/v1/usuarios/{id}", tags=["CRUD HTTP"])
async def actualizar_usuario(id: int, usuario: dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr.update(usuario)
            
            return{
                "Mensaje":"Usuario actualizado", 
                "Usuario":usr,
                "Status":"200"
            }
            
    raise HTTPException(
        status_code = 400,
        detail = "Usuario no encontrado"
    )
  
  
@app.delete("/v1/usurios/{id}", tags=["CRUD HTTP"])
async def eliminar_usuario(id: int):
    for usr in usuarios:
        if usr["id"] == id:
            usuarios.remove(usr)
            return{
                "Mensaje":"Usuario eliminado",
                "Usuario":usr,
                "Status":"200"
            }
    raise HTTPException(
        status_code = 400,
        detail = "Usuario no encontrado"
    )
            
    
    
        
        
        
        
        
    
   
   
   
   
   
   
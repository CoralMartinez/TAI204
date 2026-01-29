#importaciones

from fastapi import FastAPI 

#librería: fastapi, clase: FastAPI

import asyncio  


#Instancia del servidor

app =  FastAPI()


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
    








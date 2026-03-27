#Importaciones

from fastapi import FastAPI, APIRouter 
from app.routers import usuarios, varios
from app.data.db import engine 
from app.data import usuario
from app.data.usuario import Usuario

usuario.Base.metadata.create_all(bind=engine)

app =  FastAPI(
    title = "Mi primer API" ,
    description = "Coral Martínez Silvestre :) " ,
    version = "1.0"
)

app.include_router(usuarios.router)

app.include_router(varios.routerV)




    #BACKEND
    # LEVANTAR SERVIDOR fastAPI
    # C:\TAI204>
    # #uvicorn miAPI.main:app --reload --port 5000
    
    #SI SE BORRA EL CONTENEDOR EN DOCKER
    #docker compose up --build
    
    #BAJAR O BORRAR EL DOCKER-COMPOSE
    # docker compose down -v
    
    #SUBIR EL DOCKER-COMPOSE
    #docker compose up --build
    
    #cd miAPI
    #uvicorn app.main:app --reload
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.security import HTTPBasic , HTTPBasicCredentials
import secrets

#Seguridad con HTTP BASIC
Security = HTTPBasic()

def verificar_peticion(credenciales: HTTPBasicCredentials = Depends(Security)):
    usuarioAut = secrets.compare_digest(credenciales.username, "Coral")
    raAut = secrets.compare_digest(credenciales.password, "123456")
    
    if not ( usuarioAut and raAut):
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Credenciales no autorizadas"
        )
    return credenciales.username



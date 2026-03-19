from fastapi import FastAPI, status, HTTPException, Depends, APIRouter
from app.data.database import usuarios
from app.models.usuarios import crear_usuario
from app.security.auth import verificar_peticion

router = APIRouter(
    prefix = "/v1/usuarios", tags=['CRUD HTTP']
)
    
@router.get("/")
async def ConsultaT():
    return{
        "status":"200",
        "total":len(usuarios),
        "Usuarios":usuarios
    }

@router.post("/")
async def agregar_usuario(usuario:crear_usuario):
    for usr in usuarios:
        if usr["id"] == usuario.id:
            raise HTTPException(
                status_code = 400,
                detail = "El id ya existe"
            )
    usuarios.append(usuario)
    return{
        "Mensaje": "Usuario agregado",
        "Usuario": usuario,
        "Status" : "200"
    }    

@router.put ("/{id}")
async def actualizar_usuario(id: int, usuario:dict):
    for usr in usuarios:
        if usr["id"] == id:
            usr["nombre"] = usuario.get("nombre")
            usr["edad"] = usuario.get("edad")
            return{
                "mensaje": "Usuario actualizado",
                "Usuario": usr,
                "Status": "200"
            }
    raise HTTPException(
        status_code = 400,
        detail = "El id no existe"
    )

@router.delete("/{id}")
async def eliminar_usuario(id: int, usuarioAuth: str = Depends (verificar_peticion)):
    for usr in usuarios:
        if usr["id"] == id:
         usuarios.remove(usr)
         return{
            "Mensaje": f"Usuario eliminado por {usuarioAuth}"
        }
    raise HTTPException(
        status_code = 400,
        detail = "El id no existe"
    )
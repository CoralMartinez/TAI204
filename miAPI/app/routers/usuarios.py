
from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from app.models.usuarios import crear_usuario
from app.security.auth import verificar_peticion
from app.data.db import get_db
from app.data.usuario import Usuario as usuarioDB

router = APIRouter(
    prefix="/v1/usuarios",
    tags=['CRUD HTTP']
)

#  GET TODOS
@router.get("/")
async def ConsultaT(db: Session = Depends(get_db)):
    
    queryUsuario = db.query(usuarioDB).all()
    
    return {
        "status": "200",
        "total": len(queryUsuario),
        "Usuarios": queryUsuario
    }

# GET POR ID
@router.get("/{id}")
async def obtener_usuario(id: int, db: Session = Depends(get_db)):

    usuario = db.query(usuarioDB).filter(usuarioDB.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return usuario

# POST
@router.post("/")
async def agregar_usuario(usuarioP: crear_usuario, db: Session = Depends(get_db)):
    
    usuarioNuevo = usuarioDB(nombre=usuarioP.nombre, edad=usuarioP.edad)
    db.add(usuarioNuevo)
    db.commit()
    db.refresh(usuarioNuevo)
    
    return {
        "Mensaje": "Usuario agregado",
        "Usuario": usuarioNuevo,
        "Status": "200"
    }

#  PUT
@router.put("/{id}")
async def actualizar_usuario(id: int, usuario: crear_usuario, db: Session = Depends(get_db)):

    usuario_db = db.query(usuarioDB).filter(usuarioDB.id == id).first()

    if not usuario_db:
        raise HTTPException(status_code=404, detail="El id no existe")

    usuario_db.nombre = usuario.nombre
    usuario_db.edad = usuario.edad

    db.commit()

    return {
        "mensaje": "Usuario actualizado",
        "usuario": usuario_db
    }

#  PATCH
@router.patch("/{id}")
async def actualizar_parcial(id: int, datos: dict, db: Session = Depends(get_db)):

    usuario = db.query(usuarioDB).filter(usuarioDB.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="No existe")

    if "nombre" in datos:
        usuario.nombre = datos["nombre"]

    if "edad" in datos:
        usuario.edad = datos["edad"]

    db.commit()

    return {
        "mensaje": "Actualizado parcialmente",
        "usuario": usuario
    }

#  DELETE
@router.delete("/{id}")
async def eliminar_usuario(
    id: int,
    db: Session = Depends(get_db),
    usuarioAuth: str = Depends(verificar_peticion)
):

    usuario = db.query(usuarioDB).filter(usuarioDB.id == id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail="El id no existe")

    db.delete(usuario)
    db.commit()

    return {
        "Mensaje": f"Usuario eliminado por {usuarioAuth}"}
    


from pydantic import BaseModel, Field

#-------------------------------------------------------------------------------------------
#Modelo Pydantic de validacion
#-------------------------------------------------------------------------------------------


class crear_usuario(BaseModel):
    id:int = Field(...,gt=0, description="identificador  de usuario")
    nombre:str = Field(...,min_length=3, max_length=50, example="Patroclo")
    edad:int = Field(...,ge=1, le=125, description="Edad valida de 1 a 125")
    
    
    

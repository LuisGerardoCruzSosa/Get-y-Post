#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel

#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

#Levantamos el server Uvicorn
#-uvicorn crud:app --reload-
#Definimos nuestra entidad: user

class User(BaseModel):
    id:int
    Survived: int
    Pclass: int
    Name: str
    Sex: str
    Age:int
    
#Creamos un objeto en forma de lista con diferentes usuarios (Esto sería una base de datos)  
users_list= [User(id=1, Survived="0",Pclass="3", Name="Braund, Mr. Owen Harris", Sex="male", Age="22"),
             User(id=2, Survived="1",Pclass="1", Name="Cumings, Mrs. John Bradley (Florence Briggs Thayer)", Sex="female", Age="38"),
             User(id=3, Survived="1",Pclass="3", Name="	Heikkinen, Miss. Laina", Sex="female", Age="26"),
             User(id=4, Survived="1",Pclass="1", Name="Futrelle, Mrs. Jacques Heath (Lily May Peel)", Sex="female", Age="35"),
             User(id=5, Survived="0",Pclass="3", Name="Allen, Mr. William Henry", Sex="male", Age="35"),
             User(id=6, Survived="0",Pclass="3", Name="Moran, Mr. James", Sex="female", Age="26"),
             User(id=7, Survived= "0",Pclass= "1",Name ="McCarthy, Mr. Timothy J",Sex= "male",Age= "54"),
             User(id=8, Survived="0",Pclass="3", Name="Palsson, Master. Gosta Leonard", Sex="male", Age="2"),
             User(id=9, Survived="1",Pclass="3", Name="Johnson, Mrs. Oscar W (Elisabeth Vilhelmina Berg", Sex="female", Age="27"),
             User(id=10, Survived="1",Pclass="2", Name="Nasser, Mrs. Nicholas (Adele Achem)", Sex="female", Age="14"),
             User(id=11, Survived="1",Pclass="3", Name="Sandstrom, Miss. Marguerite Rut", Sex="female", Age="4"),
             User(id=12, Survived="1",Pclass="1", Name="Bonnell, Miss. Elizabeth", Sex="female", Age="58"),
             User(id=13, Survived= "0",Pclass= "3",Name ="Saundercock, Mr. William Henry",Sex= "male",Age= "20"),
             User(id=14, Survived="0",Pclass="3", Name="Andersson, Mr. Anders Johan", Sex="male", Age="39"),
             User(id=15, Survived="0",Pclass="3", Name="Vestrom, Miss. Hulda Amanda Adolfina", Sex="female", Age="14"),
             User(id=16, Survived="1",Pclass="2", Name="Hewlett, Mrs. (Mary D Kingcome)", Sex="female", Age="55"),
             User(id=17, Survived="0",Pclass="3", Name="Rice, Master. Eugene", Sex="male", Age="2"),
             User(id=18, Survived="1",Pclass="2", Name="Williams, Mr. Charles Eugene", Sex="male", Age="0"),
             User(id=19, Survived= "0",Pclass= "3",Name ="Vander Planke, Mrs. Julius (Emelia Maria Vandemoortele)",Sex= "female",Age= "31"),
             User(id=20, Survived="1",Pclass="3", Name="Masselmani, Mrs. Fatima", Sex="female", Age="0"),
             User(id=21, Survived="0",Pclass="2", Name="Fynney, Mr. Joseph J", Sex="male", Age="35"),
             User(id=22, Survived="1",Pclass="2", Name="Beesley, Mr. Lawrence", Sex="male", Age="34"),
             User(id=23, Survived="1",Pclass="3", Name="McGowan, Miss. Anna Annie", Sex="female", Age="15"),
             User(id=24, Survived="1",Pclass="1", Name="Sloper, Mr. William Thompson", Sex="male", Age="28"),
             User(id=25, Survived= "0",Pclass= "3",Name ="alsson, Miss. Torborg Danira",Sex= "female",Age= "8")
             ]


#Get
@app.get("/usersclass/")
async def usersclass():
    return (users_list)
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/


#Get con Filtro Path
@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
     # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/1


#Get con Filtro Query
@app.get("/usersclass/")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)  #Función de orden superior
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}

 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass/?id=1
 
 
#Post
@app.post("/usersclass/")
async def usersclass(user:User):
    
    found=False     #Usamos bandera found para verificar si hemos encontrado el usuario  
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:  #Si el Id del usuario guardado es igual al Id del usuario nuevo
            return {"error":"el usuario ya existe"}
    else:
        users_list.append(user)
        return user
    
    #http://127.0.0.1:8000/usersclass/
   

   #PUT
   
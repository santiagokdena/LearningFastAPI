from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title= "My First App using FastAPI"
app.version = "2.0.0"
movies={
    "id":1,
    "title":"El padrino",
    "overview":"Un hombre de la mafia que debe lidiar con sus asuntos familiares pero tambien laborales en un entorno hostil pero tambien acogedor.",
    "rating":8.5,
    "category":"Terror"
}
@app.get('/',tags=["Home"]) #ruta que ira a la dir root
@app.get('/home',tags=["Home"])
def home():
    return "Hello World"
@app.get("/movies",tags=["home"]) 
def home():
    return movies
@app.get("/movies/{i}",tags=["Home"])
def get_movie(i:int):
    return i
